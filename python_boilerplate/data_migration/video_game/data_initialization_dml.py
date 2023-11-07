from loguru import logger

from python_boilerplate.demo.pandas_usage import video_games
from python_boilerplate.repository.model.video_game import VideoGame


def execute() -> None:
    count = VideoGame.select().count()
    if count == 1212:
        logger.info(f"Count of video_game: {count}")
        return
    video_game_list = []
    for index, row in video_games.iterrows():
        video_game_list.append(
            {
                "title": row["Title"],
                "handheld": 1 if row["Features.Handheld?"] else 0,
                "max_players": row["Features.Max Players"],
                "multiplatform": 1 if row["Features.Multiplatform?"] else 0,
                "online": 1 if row["Features.Online?"] else 0,
                "genres": row["Metadata.Genres"],
                "licensed": 1 if row["Metadata.Licensed?"] else 0,
                "publishers": row["Metadata.Publishers"],
                "sequel": 1 if row["Metadata.Sequel?"] else 0,
                "review_score": row["Metrics.Review Score"],
                "sales": row["Metrics.Sales"],
                "used_price": row["Metrics.Used Price"],
                "console": row["Release.Console"],
                "rating": row["Release.Rating"],
                "re_release": 1 if row["Release.Re-release?"] else 0,
                "year": row["Release.Year"],
            }
        )
    logger.info(f"Length of video_game_list: {len(video_game_list)}")
    VideoGame.insert_many(rows=video_game_list).execute()
    logger.info(f"Done inserting {VideoGame.select().count()} {VideoGame}")
