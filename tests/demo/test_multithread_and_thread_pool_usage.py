import pandas as pd

from python_boilerplate.demo.multithread_and_thread_pool_usage import (
    COLUMN_NAMES,
    ROW_ARRAY,
    async_generate_data_frame,
)


def test_async_generate_data_frame():
    data_frame = async_generate_data_frame()
    assert data_frame is not None
    assert isinstance(data_frame, pd.DataFrame)
    assert len(data_frame) > 0
    assert len(data_frame) == sum(ROW_ARRAY)
    assert len(data_frame.columns) == len(COLUMN_NAMES)
    assert set(data_frame.columns) == set(COLUMN_NAMES)
