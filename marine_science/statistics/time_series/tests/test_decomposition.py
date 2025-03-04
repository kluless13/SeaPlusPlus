"""
Tests for time series decomposition functions.
"""

import numpy as np
import pandas as pd
import pytest
from marine_science.statistics.time_series.decomposition import seasonal_decompose, detect_seasonality, check_seasonality

@pytest.fixture
def sample_seasonal_data():
    """Create sample seasonal time series data."""
    # Create 2 years of daily data with annual seasonality
    t = np.linspace(0, 2*np.pi*2, 730)  # 2 years
    seasonal = np.sin(t)  # Annual cycle
    trend = 0.1 * np.arange(len(t))  # Linear trend
    noise = np.random.normal(0, 0.1, len(t))  # Random noise
    data = seasonal + trend + noise
    return pd.Series(data)

def test_seasonal_decompose(sample_seasonal_data):
    """Test seasonal decomposition function."""
    observed, trend, seasonal, residual = seasonal_decompose(
        sample_seasonal_data,
        period=365
    )
    
    # Check shapes
    assert len(observed) == len(sample_seasonal_data)
    assert len(trend) == len(sample_seasonal_data)
    assert len(seasonal) == len(sample_seasonal_data)
    assert len(residual) == len(sample_seasonal_data)
    
    # Check basic properties
    assert isinstance(observed, pd.Series)
    assert isinstance(trend, pd.Series)
    assert isinstance(seasonal, pd.Series)
    assert isinstance(residual, pd.Series)
    
    # Check that components sum to original (approximately)
    reconstructed = trend + seasonal + residual
    np.testing.assert_array_almost_equal(
        observed.dropna(),
        reconstructed.dropna(),
        decimal=10
    )

def test_detect_seasonality(sample_seasonal_data):
    """Test seasonality detection function."""
    period = detect_seasonality(sample_seasonal_data)
    
    # Should detect annual seasonality (365 days)
    assert abs(period - 365) <= 5  # Allow small deviation

def test_seasonality_detection(sample_seasonal_data):
    """Test seasonality statistical test."""
    is_seasonal, p_value = check_seasonality(sample_seasonal_data)
    
    # Should detect seasonality
    assert is_seasonal
    assert p_value < 0.05
    
    # Test with random data (should not be seasonal)
    random_data = pd.Series(np.random.normal(0, 1, 1000))
    is_seasonal, p_value = check_seasonality(random_data)
    assert not is_seasonal
    assert p_value > 0.05 