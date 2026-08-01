"""
                        equal_weight.py

                        Part of Portfolio Analytics Platform.
                        
Equal Weight portfolio.
"""

from __future__ import annotations

import numpy as np


class EqualWeightOptimizer:

    def optimize(
        self,
        n_assets: int,
    ) -> np.ndarray:

        return np.ones(
            n_assets
        ) / n_assets