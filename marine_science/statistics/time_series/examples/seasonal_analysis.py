#!/usr/bin/env python3
"""
Marine Science Time Series Analysis Example

This script demonstrates how to use the marine science time series analysis tools
to analyze sea surface temperature data.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from marine_science.statistics.time_series.decomposition import (
    seasonal_decompose,
    detect_seasonality,
    test_seasonality
)

def generate_sample_sst_data(years=5):
    """Generate synthetic sea surface temperature data."""
    # Generate daily data points
    days = np.arange(years * 365)
    t = days * (2 * np.pi / 365)  # Convert to radians for annual cycle
    
    # Create components
    seasonal = 5 * np.sin(t)  # Annual cycle with 5°C amplitude
    trend = 0.001 * days  # Slight warming trend
    noise = np.random.normal(0, 0.5, len(days))  # Random variations
    
    # Combine components
    sst = 20 + seasonal + trend + noise  # Base temperature of 20°C
    dates = pd.date_range('2018-01-01', periods=len(days), freq='D')
    return pd.Series(sst, index=dates, name='Sea Surface Temperature (°C)')

def plot_time_series(data, title):
    """Plot a time series with proper formatting."""
    plt.figure(figsize=(12, 6))
    data.plot()
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_decomposition(observed, trend, seasonal, residual):
    """Plot the decomposition components."""
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 10))
    
    observed.plot(ax=ax1)
    ax1.set_title('Observed Data')
    ax1.grid(True)
    
    trend.plot(ax=ax2)
    ax2.set_title('Trend')
    ax2.grid(True)
    
    seasonal.plot(ax=ax3)
    ax3.set_title('Seasonal')
    ax3.grid(True)
    
    residual.plot(ax=ax4)
    ax4.set_title('Residual')
    ax4.grid(True)
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the analysis."""
    # Generate sample data
    print("Generating sample SST data...")
    sst_series = generate_sample_sst_data()
    
    # Plot the raw data
    plot_time_series(sst_series, 'Synthetic Sea Surface Temperature Data')
    
    # Detect and test seasonality
    print("\nAnalyzing seasonality...")
    period = detect_seasonality(sst_series)
    print(f'Detected seasonal period: {period} days')
    
    is_seasonal, p_value = test_seasonality(sst_series)
    print(f'Seasonality test p-value: {p_value:.2e}')
    print(f'Data shows significant seasonality: {is_seasonal}')
    
    # Perform seasonal decomposition
    print("\nPerforming seasonal decomposition...")
    observed, trend, seasonal, residual = seasonal_decompose(
        sst_series,
        period=365
    )
    
    # Plot decomposition
    plot_decomposition(observed, trend, seasonal, residual)
    
    # Analyze one complete seasonal cycle
    print("\nAnalyzing annual seasonal pattern...")
    one_year = seasonal[0:365]
    months = pd.date_range('2018-01-01', '2018-12-31', freq='M')
    
    plt.figure(figsize=(12, 6))
    one_year.plot()
    plt.title('Annual Seasonal Pattern')
    plt.grid(True)
    plt.xticks(months, [d.strftime('%B') for d in months], rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main() 