import pandas as pd
from pandas import DataFrame

from python_boilerplate.common.profiling import cpu_profile, elapsed_time, mem_profile
from python_boilerplate.demo.multithread_and_thread_pool_usage import (
    COLUMN_NAMES,
    ROW_ARRAY,
    async_generate_data_frame,
)


@elapsed_time("INFO")
@mem_profile("INFO")
@cpu_profile("INFO")
def test_async_generate_data_frame() -> None:
    data_frame: DataFrame = async_generate_data_frame()
    assert data_frame is not None
    assert isinstance(data_frame, pd.DataFrame)
    assert len(data_frame) > 0
    assert len(data_frame) == sum(ROW_ARRAY)
    assert len(data_frame.columns) == len(COLUMN_NAMES)
    assert set(data_frame.columns) == set(COLUMN_NAMES)
