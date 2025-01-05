from importlib import metadata as importlib_metadata
from importlib.metadata import Distribution, PackagePath
from pathlib import Path

import humanize
from loguru import logger


def calculate_distribution(dist: Distribution) -> int:
    # noinspection PyUnresolvedReferences,PyProtectedMember
    distribution_parent: Path = dist._path.parent  # type: ignore # noqa: SLF001, PGH003
    files_in_distribution: list[PackagePath] = dist.files if dist.files is not None else []
    total_size = 0
    logger.debug(f"{dist.metadata['name']} has {len(files_in_distribution)} files")
    for file in files_in_distribution:
        file_path = distribution_parent / str(file)
        if file_path.is_file():
            total_size += file_path.stat().st_size
    return total_size


def list_python_dependencies() -> None:
    distributions = list(importlib_metadata.distributions())
    logger.info(f"Size of dists: {len(distributions)}")
    total_size = 0
    for dist in distributions:
        size_in_bytes = calculate_distribution(dist)
        total_size += size_in_bytes
        logger.info(f"{dist.metadata['name']}: {humanize.naturalsize(size_in_bytes)}")
        logger.info("-" * 40)
    logger.info(f"Total dependency size: {humanize.naturalsize(total_size)}")


if __name__ == "__main__":
    list_python_dependencies()
