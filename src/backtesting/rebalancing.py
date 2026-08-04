"""
                        rebalancing.py

                        Part of Portfolio Analytics Platform.
                        
Portfolio rebalancing.
"""

from __future__ import annotations

import numpy as np


class Rebalancer:
    """
    Simple periodic rebalancer.
    """

    def rebalance(
        self,
        current_weights: np.ndarray,
        target_weights: np.ndarray,
    ) -> np.ndarray:
        
        """
        Rebalance portfolio.
        """

        return target_weights.copy()