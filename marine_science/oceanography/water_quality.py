#!/usr/bin/env python3
"""
Water Quality Analysis Module

This module provides tools for analyzing and processing water quality data
including temperature, salinity, pH, dissolved oxygen, and turbidity.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Union
from scipy import stats

class WaterQualityAnalyzer:
    """Class for analyzing water quality parameters."""
    
    def __init__(self):
        self.parameter_ranges = {
            'temperature': {'min': -2, 'max': 35, 'unit': '°C'},
            'salinity': {'min': 0, 'max': 45, 'unit': 'PSU'},
            'ph': {'min': 6.5, 'max': 8.5, 'unit': 'pH'},
            'dissolved_oxygen': {'min': 0, 'max': 15, 'unit': 'mg/L'},
            'turbidity': {'min': 0, 'max': 50, 'unit': 'NTU'}
        }

    def validate_data(
        self,
        data: pd.DataFrame,
        parameters: Optional[List[str]] = None
    ) -> Dict[str, Dict[str, int]]:
        """
        Validate water quality parameters against acceptable ranges.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing water quality parameters
        parameters : Optional[List[str]]
            List of parameters to validate. If None, validates all available parameters.

        Returns
        -------
        Dict[str, Dict[str, int]]
            Dictionary containing validation results for each parameter
        """
        if parameters is None:
            parameters = [col for col in data.columns 
                        if col.lower() in self.parameter_ranges]

        results = {}
        for param in parameters:
            param_lower = param.lower()
            if param_lower not in self.parameter_ranges:
                continue

            ranges = self.parameter_ranges[param_lower]
            param_data = data[param]
            
            results[param] = {
                'total': len(param_data),
                'missing': param_data.isna().sum(),
                'below_range': sum(param_data < ranges['min']),
                'above_range': sum(param_data > ranges['max']),
                'within_range': sum((param_data >= ranges['min']) & 
                                  (param_data <= ranges['max']))
            }

        return results

    def calculate_statistics(
        self,
        data: pd.DataFrame,
        parameters: Optional[List[str]] = None
    ) -> Dict[str, Dict[str, float]]:
        """
        Calculate basic statistics for water quality parameters.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing water quality parameters
        parameters : Optional[List[str]]
            List of parameters to analyze. If None, analyzes all available parameters.

        Returns
        -------
        Dict[str, Dict[str, float]]
            Dictionary containing statistics for each parameter
        """
        if parameters is None:
            parameters = [col for col in data.columns 
                        if col.lower() in self.parameter_ranges]

        stats_dict = {}
        for param in parameters:
            param_data = data[param].dropna()
            
            stats_dict[param] = {
                'mean': param_data.mean(),
                'std': param_data.std(),
                'min': param_data.min(),
                'max': param_data.max(),
                'median': param_data.median(),
                'skewness': stats.skew(param_data),
                'kurtosis': stats.kurtosis(param_data)
            }

        return stats_dict

    def detect_anomalies(
        self,
        data: pd.DataFrame,
        parameter: str,
        method: str = 'zscore',
        threshold: float = 3.0
    ) -> pd.Series:
        """
        Detect anomalies in water quality parameters.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing water quality parameters
        parameter : str
            Parameter to analyze for anomalies
        method : str
            Method to use for anomaly detection ('zscore' or 'iqr')
        threshold : float
            Threshold for anomaly detection

        Returns
        -------
        pd.Series
            Boolean series indicating anomalies
        """
        param_data = data[parameter].dropna()
        
        if method == 'zscore':
            z_scores = np.abs(stats.zscore(param_data))
            return pd.Series(z_scores > threshold, index=param_data.index)
        
        elif method == 'iqr':
            Q1 = param_data.quantile(0.25)
            Q3 = param_data.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            return (param_data < lower_bound) | (param_data > upper_bound)
        
        else:
            raise ValueError("Method must be either 'zscore' or 'iqr'") 