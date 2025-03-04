#!/usr/bin/env python3
"""
Biodiversity Analysis Module

This module provides tools for analyzing marine biodiversity data,
including species richness, diversity indices, and community analysis.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Union
from scipy import stats

class BiodiversityAnalyzer:
    """Class for analyzing marine biodiversity data."""

    def calculate_richness(
        self,
        data: pd.DataFrame,
        species_col: str = 'species',
        groupby_col: Optional[str] = None
    ) -> Union[int, pd.Series]:
        """
        Calculate species richness (number of unique species).

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing species data
        species_col : str
            Column name containing species information
        groupby_col : Optional[str]
            Column to group by (e.g., site, date)

        Returns
        -------
        Union[int, pd.Series]
            Species richness value(s)
        """
        if groupby_col:
            return data.groupby(groupby_col)[species_col].nunique()
        return data[species_col].nunique()

    def shannon_diversity(
        self,
        data: pd.DataFrame,
        species_col: str = 'species',
        abundance_col: str = 'abundance',
        groupby_col: Optional[str] = None
    ) -> Union[float, pd.Series]:
        """
        Calculate Shannon diversity index.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing species data
        species_col : str
            Column name containing species information
        abundance_col : str
            Column name containing abundance information
        groupby_col : Optional[str]
            Column to group by (e.g., site, date)

        Returns
        -------
        Union[float, pd.Series]
            Shannon diversity index value(s)
        """
        def _shannon(df):
            abundances = df[abundance_col].values
            total = abundances.sum()
            proportions = abundances / total
            return -np.sum(proportions * np.log(proportions))

        if groupby_col:
            grouped = data.groupby([groupby_col, species_col])[abundance_col].sum()
            return grouped.groupby(level=0).apply(
                lambda x: _shannon(x.reset_index())
            )
        
        return _shannon(data)

    def simpson_diversity(
        self,
        data: pd.DataFrame,
        species_col: str = 'species',
        abundance_col: str = 'abundance',
        groupby_col: Optional[str] = None
    ) -> Union[float, pd.Series]:
        """
        Calculate Simpson diversity index.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing species data
        species_col : str
            Column name containing species information
        abundance_col : str
            Column name containing abundance information
        groupby_col : Optional[str]
            Column to group by (e.g., site, date)

        Returns
        -------
        Union[float, pd.Series]
            Simpson diversity index value(s)
        """
        def _simpson(df):
            abundances = df[abundance_col].values
            total = abundances.sum()
            proportions = abundances / total
            return 1 - np.sum(proportions ** 2)

        if groupby_col:
            grouped = data.groupby([groupby_col, species_col])[abundance_col].sum()
            return grouped.groupby(level=0).apply(
                lambda x: _simpson(x.reset_index())
            )
        
        return _simpson(data)

    def jaccard_similarity(
        self,
        data: pd.DataFrame,
        site1: str,
        site2: str,
        species_col: str = 'species',
        site_col: str = 'site'
    ) -> float:
        """
        Calculate Jaccard similarity index between two sites.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing species data
        site1 : str
            First site to compare
        site2 : str
            Second site to compare
        species_col : str
            Column name containing species information
        site_col : str
            Column name containing site information

        Returns
        -------
        float
            Jaccard similarity index
        """
        species1 = set(data[data[site_col] == site1][species_col])
        species2 = set(data[data[site_col] == site2][species_col])
        
        intersection = len(species1.intersection(species2))
        union = len(species1.union(species2))
        
        return intersection / union if union > 0 else 0.0

    def rarefaction_curve(
        self,
        data: pd.DataFrame,
        species_col: str = 'species',
        abundance_col: str = 'abundance',
        n_points: int = 100
    ) -> pd.DataFrame:
        """
        Generate rarefaction curve data.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing species data
        species_col : str
            Column name containing species information
        abundance_col : str
            Column name containing abundance information
        n_points : int
            Number of points to calculate

        Returns
        -------
        pd.DataFrame
            DataFrame containing rarefaction curve data
        """
        total_abundance = data[abundance_col].sum()
        sample_sizes = np.linspace(1, total_abundance, n_points, dtype=int)
        
        species_counts = data.groupby(species_col)[abundance_col].sum()
        
        def _calculate_richness(n):
            probs = 1 - np.prod([
                1 - count/total_abundance for count in species_counts
            ], axis=0) ** n
            return np.sum(probs)
        
        richness = [_calculate_richness(n) for n in sample_sizes]
        
        return pd.DataFrame({
            'sample_size': sample_sizes,
            'expected_richness': richness
        }) 