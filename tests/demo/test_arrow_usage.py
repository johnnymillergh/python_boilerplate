import arrow
from loguru import logger

from python_boilerplate.demo.arrow_usage import convert_time_zone, string_to_datetime


def test_string_to_datetime():
    datetime = string_to_datetime("2022-01-01 15:15:00")
    assert datetime is not None
    tzinfo = datetime.tzinfo
    assert tzinfo is not None
    logger.info(f"Parsed time zone: {tzinfo}")
    now = arrow.now()
    assert datetime < now
    logger.info(f"Now: {now}, datetime: {datetime}")


def test_convert_time_zone():
    now = arrow.now()
    converted = convert_time_zone(now, "UTC+0")
    logger.info(f"Now: {now}, converted UTC+0: {converted}")
    assert converted is not None
    converted = convert_time_zone(converted, "UTC+1")
    tzinfo = converted.tzinfo
    assert tzinfo is not None
    logger.info(f"Now: {now}, converted UTC+1: {converted}")
    assert converted is not None
    converted = convert_time_zone(converted.shift(days=-1), "UTC+2")
    logger.info(f"Now: {now}, converted UTC+2: {converted}")
    assert converted is not None
    assert converted < now
    logger.info(f"Now: {now}, converted: {converted}")
