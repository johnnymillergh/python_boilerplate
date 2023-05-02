import arrow
from arrow import Arrow


def string_to_datetime(datetime: str) -> Arrow:
    return arrow.get(datetime)


def convert_time_zone(source: Arrow, target_time_zone: str) -> Arrow:
    return source.to(target_time_zone)
