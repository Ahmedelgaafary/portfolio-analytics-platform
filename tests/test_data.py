"""
                        test_data.py

                        Part of Portfolio Analytics Platform.
                        """
import pandas as pd

from src.data_processing.cache import CacheManager


def test_cache_save_load(tmp_path):

    cache = CacheManager(tmp_path)

    df = pd.DataFrame(
        {
            "A": [1, 2, 3]
        }
    )

    cache.save(
        "TEST",
        df,
    )

    loaded = cache.load(
        "TEST"
    )

    pd.testing.assert_frame_equal(
        df,
        loaded,
    )