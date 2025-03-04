 #!/usr/bin/env python3
"""
Habitat Impact Analysis Module

This module provides tools for analyzing and assessing impacts on marine habitats,
including habitat quality assessment, impact scoring, and recovery potential evaluation.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Union
from scipy import stats

class HabitatImpactAnalyzer:
    """Class for analyzing impacts on marine habitats."""

    def __init__(self):
        self.impact_weights = {
            'physical_damage': 0.3,
            'water_quality': 0.25,
            'biodiversity_loss': 0.25,
            'ecosystem_function': 0.2
        }
        
        self.recovery_factors = {
            'habitat_type': {
                'coral_reef': 0.2,
                'seagrass': 0.4,
                'mangrove': 0.3,
                'rocky_shore': 0.6,
                'sandy_beach': 0.7
            },
            'impact_severity': {
                'low': 0.8,
                'medium': 0.5,
                'high': 0.2
            },
            'protection_status': {
                'none': 0.3,
                'partial': 0.6,
                'full': 0.9
            }
        }

    def calculate_impact_score(
        self,
        data: pd.DataFrame,
        weights: Optional[Dict[str, float]] = None
    ) -> pd.Series:
        """
        Calculate overall impact score for habitat sites.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing impact metrics
        weights : Optional[Dict[str, float]]
            Custom weights for different impact types

        Returns
        -------
        pd.Series
            Impact scores for each site
        """
        if weights is None:
            weights = self.impact_weights

        # Normalize the data
        normalized_data = data.copy()
        for column in weights.keys():
            if column in data.columns:
                max_val = data[column].max()
                if max_val > 0:
                    normalized_data[column] = data[column] / max_val

        # Calculate weighted sum
        impact_score = pd.Series(0.0, index=data.index)
        for metric, weight in weights.items():
            if metric in normalized_data.columns:
                impact_score += normalized_data[metric] * weight

        return impact_score

    def assess_recovery_potential(
        self,
        habitat_type: str,
        impact_severity: str,
        protection_status: str
    ) -> float:
        """
        Assess habitat recovery potential based on various factors.

        Parameters
        ----------
        habitat_type : str
            Type of marine habitat
        impact_severity : str
            Severity of impact (low/medium/high)
        protection_status : str
            Level of protection (none/partial/full)

        Returns
        -------
        float
            Recovery potential score (0-1)
        """
        factors = self.recovery_factors
        
        habitat_score = factors['habitat_type'].get(habitat_type, 0.0)
        severity_score = factors['impact_severity'].get(impact_severity, 0.0)
        protection_score = factors['protection_status'].get(protection_status, 0.0)
        
        # Weighted combination of factors
        recovery_score = (
            0.4 * habitat_score +
            0.3 * severity_score +
            0.3 * protection_score
        )
        
        return min(max(recovery_score, 0.0), 1.0)

    def prioritize_conservation_actions(
        self,
        impact_scores: pd.Series,
        recovery_potential: pd.Series,
        biodiversity_value: pd.Series
    ) -> pd.DataFrame:
        """
        Prioritize conservation actions based on multiple criteria.

        Parameters
        ----------
        impact_scores : pd.Series
            Impact scores for each site
        recovery_potential : pd.Series
            Recovery potential scores for each site
        biodiversity_value : pd.Series
            Biodiversity value scores for each site

        Returns
        -------
        pd.DataFrame
            Prioritization scores and rankings
        """
        # Normalize all scores to 0-1 scale
        normalized_impact = impact_scores / impact_scores.max()
        normalized_recovery = recovery_potential / recovery_potential.max()
        normalized_biodiversity = biodiversity_value / biodiversity_value.max()
        
        # Calculate priority score
        # Higher impact, higher recovery potential, and higher biodiversity
        # value lead to higher priority
        priority_score = (
            0.4 * normalized_impact +
            0.3 * normalized_recovery +
            0.3 * normalized_biodiversity
        )
        
        # Create results DataFrame
        results = pd.DataFrame({
            'impact_score': normalized_impact,
            'recovery_potential': normalized_recovery,
            'biodiversity_value': normalized_biodiversity,
            'priority_score': priority_score
        })
        
        # Add rankings
        results['priority_rank'] = results['priority_score'].rank(
            ascending=False,
            method='min'
        )
        
        return results.sort_values('priority_score', ascending=False)

    def calculate_cumulative_impact(
        self,
        impact_data: pd.DataFrame,
        temporal_weights: Optional[pd.Series] = None
    ) -> pd.Series:
        """
        Calculate cumulative impact over time.

        Parameters
        ----------
        impact_data : pd.DataFrame
            Time series of impact measurements
        temporal_weights : Optional[pd.Series]
            Weights for different time periods

        Returns
        -------
        pd.Series
            Cumulative impact scores
        """
        if temporal_weights is None:
            # Default to exponential decay weights
            times = np.arange(len(impact_data))
            temporal_weights = pd.Series(
                np.exp(-0.1 * times),
                index=impact_data.index
            )
        
        # Calculate weighted sum of impacts over time
        cumulative_impact = (impact_data * temporal_weights).sum()
        
        return cumulative_impact