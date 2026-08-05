"""
                        optimizer_factory.py

                        Part of Portfolio Analytics Platform.

Optimizer Factory.
"""

from __future__ import annotations

from .equal_weight import EqualWeightOptimizer
from .markowitz import MarkowitzOptimizer
from .maximum_sharpe import MaximumSharpeOptimizer
from .minimum_variance import MinimumVarianceOptimizer


class OptimizerFactory:
    """
    Factory class for portfolio optimizers.
    """

    _OPTIMIZERS = {
        "equal_weight": EqualWeightOptimizer,
        "minimum_variance": MinimumVarianceOptimizer,
        "maximum_sharpe": MaximumSharpeOptimizer,
        "markowitz": MarkowitzOptimizer,
    }

    @classmethod
    def create(
        cls,
        optimizer_name: str,
    ):

        optimizer_name = optimizer_name.lower()

        if optimizer_name not in cls._OPTIMIZERS:
            raise ValueError(
                f"Unknown optimizer '{optimizer_name}'. "
                f"Available optimizers: "
                f"{list(cls._OPTIMIZERS.keys())}"
            )

        return cls._OPTIMIZERS[
            optimizer_name
        ]()