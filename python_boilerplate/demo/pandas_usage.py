from typing import Final

import numpy as np
import pandas as pd
from loguru import logger
from pandas import DataFrame, DatetimeIndex, Series

from python_boilerplate.common.common_function import get_data_dir, get_resources_dir
from python_boilerplate.common.profiling import elapsed_time
from python_boilerplate.common.trace import trace

# 10 minutes to pandas https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#minutes-to-pandas
# CSV & text files https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table

# The CSV dataset is from
# https://github.com/corgis-edu/corgis/blob/master/website/datasets/csv/video_games/video_games.md
video_games_path: Final = get_resources_dir() / "video_games.csv"
sony_published_video_games_path: Final = (
    get_data_dir() / "sony_published_video_games.csv"
)
video_games: Final = pd.read_csv(video_games_path)
logger.info(f"Done reading CSV, file: [{video_games_path}], rows: {len(video_games)}")


def pandas_data_structure_series() -> Series:
    return pd.Series([1, 3, 5, np.nan, 6, 8])


def pandas_data_structure_date_range() -> DatetimeIndex:
    return pd.date_range("2022-01-01", periods=6)


@trace
@elapsed_time()
def look_for_sony_published_games() -> DataFrame:
    all_columns = set(video_games)
    selected_columns = {
        "Title",
        "Metrics.Used Price",
        "Release.Console",
        "Release.Year",
        "Metadata.Publishers",
    }
    dropped_columns = list(all_columns - selected_columns)
    sony_published: Final = video_games[
        video_games["Metadata.Publishers"] == "Sony"
    ].drop(columns=dropped_columns)
    release_year: Final = "Release.Year"
    sony_games_release_year: Final = sony_published[release_year]
    min_release_year = sony_games_release_year.sort_values().min()
    max_release_year = sony_games_release_year.sort_values().max()
    logger.info(
        f"From {min_release_year} to {max_release_year}, Sony has published {len(sony_published)} games"
    )
    game_release_each_year: Final[Series] = (
        sony_published.groupby(release_year)[release_year]
        .count()
        .sort_values(ascending=False)
    )
    for item in game_release_each_year.iteritems():
        logger.info(f"Sony released {item[1]} games in {item[0]}")
    sony_published.to_csv(sony_published_video_games_path, index=False)
    return sony_published


look_for_sony_published_games()
