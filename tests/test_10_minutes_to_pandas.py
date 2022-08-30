import os
from typing import Hashable, Iterable

import numpy as np
import pandas as pd
from loguru import logger
from pandas import DataFrame, DatetimeIndex, Series

from python_boilerplate.function_collection import get_resources_dir

# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#minutes-to-pandas


def test_pandas_data_structure_series() -> None:
    series: Series = pd.Series([1, 3, 5, np.nan, 6, 8])
    assert series.dtype == np.dtype("float64")
    assert len(series) == 6
    logger.info(f"series:\n{series}")


def test_pandas_data_structure_date_range() -> None:
    dates: DatetimeIndex = pd.date_range("2022-01-01", periods=6)
    assert dates.dtype == np.dtype("datetime64[ns]")
    assert len(dates) == 6
    date1 = dates.array[0].date()
    logger.info(f"date 1: {date1}")
    logger.info(f"dates:\n{dates}")


def test_pandas_reading_csv() -> None:
    """
    Read a csv file.

    See the CSV & text files https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table
    """
    # The CSV dataset is from
    # https://github.com/corgis-edu/corgis/blob/master/website/datasets/csv/video_games/video_games.md
    video_games: DataFrame = pd.read_csv(
        f"{get_resources_dir()}{os.path.sep}video_games.csv"
    )
    logger.info(f"video_games:\n{video_games}")
    logger.info(f"Head of video_games:\n{video_games.head()}")
    logger.info(f"Tail of video_games:\n{video_games.tail()}")
    logger.info(f"video_games.columns:\n{video_games.columns}")
    logger.info(f"video_games.index:\n{video_games.index}")
    logger.info(f"video_games.info():\n{video_games.info()}")
    logger.info(f"video_games.iloc[1]:\n{video_games.iloc[1]}")
    iterable_video_games: Iterable[tuple[Hashable, Series]] = video_games.iterrows()
    for index, row in iterable_video_games:
        logger.info(f"index: {index}, title: {row['Title']}")
        if index == 5:
            break
    assert video_games is not None
    assert video_games.iloc[1]["Release.Console"] == "Sony PSP"
