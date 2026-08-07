from src.utils.helpers import Helpers
from src.utils.validators import Validator

import numpy as np
import pandas as pd


def test_validate_weights():

    Validator.validate_weights(
        np.array(
            [0.4, 0.6]
        )
    )


def test_validate_dataframe():

    Validator.validate_dataframe(
        pd.DataFrame(
            {"A": [1]}
        )
    )


def test_timestamp():

    assert isinstance(
        Helpers.timestamp(),
        str,
    )


def test_flatten():

    d = {
        "a": {
            "b": 1
        }
    }

    result = Helpers.flatten_dict(d)

    assert result["a.b"] == 1