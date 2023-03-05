import random
from concurrent.futures import wait

import pandas as pd
from faker import Faker
from loguru import logger
from pandas import DataFrame

from python_boilerplate.__main__ import startup
from python_boilerplate.common.asynchronization import async_function
from python_boilerplate.common.common_function import get_data_dir
from python_boilerplate.common.profiling import elapsed_time

COLUMN_NAMES = [
    "full_name",
    "email",
    "company",
    "job",
]

OUTPUT_CSV_PATH = get_data_dir() / "multithread_generated_data.csv"
ROW_ARRAY = [random.randint(200, 1000) for _ in range(10)]


@async_function
@elapsed_time()
def generate_data_frame(rows: int) -> DataFrame:
    logger.info(f"Generating {rows} rows of data...")
    data_array = []
    faker = Faker()
    for _ in range(rows):
        data_array.append(
            {
                COLUMN_NAMES[0]: faker.name(),
                COLUMN_NAMES[1]: faker.email(),
                COLUMN_NAMES[2]: faker.company(),
                COLUMN_NAMES[3]: faker.job(),
            }
        )
    return DataFrame(data_array)


@elapsed_time()
def async_generate_data_frame() -> DataFrame:
    total_rows = sum(ROW_ARRAY)
    logger.info(f"Going to generate {total_rows} rows of data in asynchronous way")
    futures = [generate_data_frame(row) for row in ROW_ARRAY]
    logger.info(
        f"Submitted {len(futures)} tasks to ThreadPoolExecutor, waiting for them to complete..."
    )
    # noinspection PyTypeChecker
    wait(futures)
    logger.warning(f"All tasks completed in {futures}")
    result = DataFrame(columns=COLUMN_NAMES)
    for future in futures:
        result = pd.concat([result, future.result()])
    logger.info(f"Merged all DataFrame, length: {len(result)}")
    result.to_csv(OUTPUT_CSV_PATH, index=False)
    logger.info(f"Done writing file [{OUTPUT_CSV_PATH}], length: {len(result)}")
    return result


if __name__ == "__main__":
    startup()
    async_generate_data_frame()
