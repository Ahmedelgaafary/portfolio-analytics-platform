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
    
#---------------------------------------------------------
#Test preprocessing module
#---------------------------------------------------------
from src.data_processing.preprocessing import DataPreprocessor

import pandas as pd


def test_remove_duplicates():

    df = pd.DataFrame(
        {"Close": [1, 2, 3]}
    )

    df.index = [0, 0, 1]

    processor = DataPreprocessor()

    cleaned = processor.remove_duplicates(df)

    assert len(cleaned) == 2
