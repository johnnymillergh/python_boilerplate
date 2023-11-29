from python_boilerplate.data_migration.video_game.data_initialization_dml import (
    execute as execute_video_game,
)


def init_db_data() -> None:
    # Executing db init
    execute_video_game()
