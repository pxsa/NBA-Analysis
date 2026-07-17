from src.database import Database
from src.queries import PLAYER_STATS
from src.eda import EDA


db = Database(
    "mysql+pymysql://user:password@localhost/nba"
)


players = db.read_query(
    PLAYER_STATS
)


eda = EDA(players)


eda.overview()

print(
    eda.missing_values()
)

print(
    eda.statistics()
)