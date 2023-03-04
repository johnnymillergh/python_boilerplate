from concurrent.futures import Future, wait
from typing import Any, Final

import numpy as np
import pandas as pd
from faker import Faker
from loguru import logger
from pandas import DataFrame, DatetimeIndex, Series

from python_boilerplate.__main__ import startup
from python_boilerplate.common.asynchronization import async_function
from python_boilerplate.common.common_function import get_data_dir, get_resources_dir
from python_boilerplate.common.profiling import elapsed_time
from python_boilerplate.common.trace import async_trace

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

faker = Faker()


def pandas_data_structure_series() -> Series:
    return pd.Series([1, 3, 5, np.nan, 6, 8])


def pandas_data_structure_date_range() -> DatetimeIndex:
    return pd.date_range("2022-01-01", periods=6)


@async_trace
@elapsed_time("INFO")
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
        (video_games["Metadata.Publishers"] == "Sony")
        & (video_games["Features.Max Players"] > 1)
        & (video_games["Title"].str.contains("t"))
    ].drop(columns=dropped_columns)
    release_year: Final = "Release.Year"
    sony_games_release_year: Final = sony_published[release_year]
    min_release_year = sony_games_release_year.sort_values().min()
    max_release_year = sony_games_release_year.sort_values().max()
    logger.info(
        f"From {min_release_year} to {max_release_year}, Sony has published {len(sony_published)} games, "
        f"those are multi-player, title with 't'"
    )
    game_release_each_year: Final[Series] = (
        sony_published.groupby(release_year)[release_year]
        .count()
        .sort_values(ascending=False)
    )
    for item in game_release_each_year.items():
        logger.info(f"Sony released {item[1]} games in {item[0]}")
    sony_published.to_csv(sony_published_video_games_path, index=False)
    return sony_published


@async_function
@elapsed_time("DEBUG")
def generate_random_data(row_count: int) -> DataFrame:
    rows: list[dict[str, Any]] = []
    for _ in range(row_count):
        rows.append(
            {
                "full_name": faker.name(),
                "age": faker.random.randint(18, 100),
                "phone_number": faker.phone_number(),
                "address": faker.address(),
                "zipcode": faker.zipcode(),
                "country": faker.country(),
            }
        )
    return pd.DataFrame(rows)


# noinspection PyTypeChecker
@elapsed_time("DEBUG")
def submit_parallel_tasks() -> list[DataFrame]:
    futures: list[Future] = []
    for _ in range(5):
        futures.append(generate_random_data(5000))
    wait(futures)
    logger.info(f"All {len(futures)} tasks has done")
    return [future.result() for future in futures]


@elapsed_time("DEBUG")
def merge_results(dataframes: list[DataFrame]) -> DataFrame:
    result_list: DataFrame = pd.DataFrame(
        columns=["full_name", "age", "phone_number", "address", "zipcode", "country"]
    )
    for dataframe in dataframes:
        result_list = pd.concat([result_list, dataframe])
    return result_list


def data_generation():
    futures = submit_parallel_tasks()
    result_data_pd: DataFrame = merge_results(futures)  # type: ignore
    logger.info(f"Finished merging data\n{result_data_pd}")
    random_data_path = get_data_dir() / "random_data.csv"
    result_data_pd.to_csv(random_data_path, index=False)
    logger.info(
        f"Done writing data file [{random_data_path}], rows: {len(result_data_pd)}"
    )


if __name__ == "__main__":
    startup()
    look_for_sony_published_games()
