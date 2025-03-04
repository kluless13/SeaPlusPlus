"""
Marine Science Time Series Analysis Module

This module provides tools for analyzing time series data in marine science applications.
"""

from .decomposition import seasonal_decompose, detect_seasonality

__all__ = [
    'seasonal_decompose',
    'detect_seasonality',
]

__version__ = '0.1.0' 