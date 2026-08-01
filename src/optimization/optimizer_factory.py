"""
                        optimizer_factory.py

                        Part of Portfolio Analytics Platform.
                        """

from .equal_weight import EqualWeightOptimizer
from .markowitz import MarkowitzOptimizer
from .maximum_sharpe import MaximumSharpeOptimizer
from .minimum_variance import MinimumVarianceOptimizer


class OptimizerFactory:

    @staticmethod
    def create(name: str):

        optimizers = {
            "equal_weight": EqualWeightOptimizer,
            "minimum_variance": MinimumVarianceOptimizer,
            "maximum_sharpe": MaximumSharpeOptimizer,
            "markowitz": MarkowitzOptimizer,
        }

        if name not in optimizers:

            raise ValueError(
                f"Unknown optimizer: {name}"
            )

        return optimizers[name]()