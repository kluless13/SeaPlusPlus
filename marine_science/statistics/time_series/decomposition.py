"""
Time series decomposition tools for marine science data analysis.
"""

import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose as sm_seasonal_decompose
from typing import Tuple, Optional, Union
from scipy import stats

def seasonal_decompose(
    data: Union[pd.Series, np.ndarray],
    period: Optional[int] = None,
    model: str = 'additive'
) -> Tuple[pd.Series, pd.Series, pd.Series, pd.Series]:
    """
    Decompose time series into trend, seasonal, and residual components.
    
    Parameters
    ----------
    data : Union[pd.Series, np.ndarray]
        Time series data to decompose
    period : Optional[int]
        Length of seasonal cycle. If None, will attempt to detect automatically
    model : str
        Type of decomposition ('additive' or 'multiplicative')
        
    Returns
    -------
    Tuple[pd.Series, pd.Series, pd.Series, pd.Series]
        Observed, trend, seasonal, and residual components
    """
    if isinstance(data, np.ndarray):
        data = pd.Series(data)
    
    if period is None:
        period = detect_seasonality(data)
    
    # Handle missing values before decomposition
    data_clean = data.copy()
    data_clean[data_clean.isna()] = data_clean.interpolate(method='linear')
    
    # Perform decomposition
    result = sm_seasonal_decompose(data_clean, period=period, model=model)
    
    # Convert all components to pandas Series with the same index
    observed = pd.Series(data_clean.values, index=data.index)  # Use cleaned data
    trend = pd.Series(result.trend, index=data.index)
    seasonal = pd.Series(result.seasonal, index=data.index)
    residual = pd.Series(result.resid, index=data.index)
    
    # Fill NaN values in components using interpolation
    trend = trend.interpolate(method='linear', limit_direction='both')
    seasonal = seasonal.interpolate(method='linear', limit_direction='both')
    residual = observed - trend - seasonal  # Recalculate residual to ensure components sum to observed
    
    # For multiplicative model, convert to additive for comparison
    if model == 'multiplicative':
        trend = np.log(trend)
        seasonal = np.log(seasonal)
        residual = np.log(observed) - trend - seasonal  # Recalculate residual in log space
        observed = np.log(observed)
    
    return observed, trend, seasonal, residual

def detect_seasonality(data: Union[pd.Series, np.ndarray], max_lag: int = 365) -> int:
    """
    Detect seasonality in time series using autocorrelation.
    
    Parameters
    ----------
    data : Union[pd.Series, np.ndarray]
        Time series data to analyze
    max_lag : int
        Maximum lag to consider for seasonality
        
    Returns
    -------
    int
        Detected seasonal period
    """
    if isinstance(data, pd.Series):
        data = data.values
        
    # Remove NaN values and detrend
    data = data[~np.isnan(data)]
    trend = np.polyfit(np.arange(len(data)), data, 1)
    detrended = data - np.polyval(trend, np.arange(len(data)))
    
    # Calculate autocorrelation
    acf = np.correlate(detrended - np.mean(detrended), detrended - np.mean(detrended), mode='full')
    acf = acf[len(acf)//2:]  # Take only positive lags
    acf = acf / acf[0]  # Normalize
    
    # Find peaks in autocorrelation with minimum prominence
    peaks = []
    min_prominence = 0.1
    for i in range(max(1, period_min := max_lag // 4), min(len(acf)-1, max_lag)):
        if (acf[i] > acf[i-1] and acf[i] > acf[i+1] and  # Local maximum
            acf[i] > min_prominence and  # Significant correlation
            i >= period_min):  # Minimum period length
            peaks.append((i, acf[i]))
    
    if not peaks:
        return max_lag
    
    # Find the peak closest to 365 days among the top peaks
    top_peaks = sorted(peaks, key=lambda x: x[1], reverse=True)[:3]  # Consider top 3 peaks
    return min(top_peaks, key=lambda x: abs(x[0] - 365))[0]

def check_seasonality(
    data: Union[pd.Series, np.ndarray],
    period: Optional[int] = None,
    alpha: float = 0.05
) -> Tuple[bool, float]:
    """
    Test for the presence of seasonality using a statistical test.
    
    Parameters
    ----------
    data : Union[pd.Series, np.ndarray]
        Time series data to test
    period : Optional[int]
        Length of seasonal cycle. If None, will attempt to detect automatically
    alpha : float
        Significance level for the test
        
    Returns
    -------
    Tuple[bool, float]
        Boolean indicating if seasonality is present, and the p-value
    """
    if isinstance(data, pd.Series):
        data = data.values
    
    if period is None:
        period = detect_seasonality(data)
    
    # Remove NaN values and detrend
    data = data[~np.isnan(data)]
    trend = np.polyfit(np.arange(len(data)), data, 1)
    detrended = data - np.polyval(trend, np.arange(len(data)))
    
    # Reshape data into seasons, handling incomplete periods
    n_complete_seasons = len(detrended) // period
    if n_complete_seasons < 2:
        return False, 1.0
    
    seasons = detrended[:n_complete_seasons * period].reshape(n_complete_seasons, period)
    
    # Perform Kruskal-Wallis H-test on each time point across seasons
    season_groups = [seasons[:, i] for i in range(period)]
    h_stat, p_value = stats.kruskal(*season_groups)
    
    return p_value < alpha, p_value 