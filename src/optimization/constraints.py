"""
                        constraints.py

                        Part of Portfolio Analytics Platform.
Optimization constraints.
"""

from __future__ import annotations

import numpy as np


class Constraints:
    """
    Common optimization constraints.
    """

    @staticmethod
    def weight_sum():
        """
        Sum of portfolio weights must equal one.
        """
        return {
            "type": "eq",
            "fun": lambda w: np.sum(w) - 1.0,
        }

    @staticmethod
    def bounds(
        n_assets: int,
        minimum: float = 0.0,
        maximum: float = 1.0,
    ):
        """
        Weight bounds.
        """
        return [(minimum, maximum)] * n_assets