import os
import pandas as pd
from sqlalchemy import create_engine

from src.eda import EDA


# =========================
# 1. Database Connection
# =========================

# توجه:
# اطلاعات اتصال دیتابیس را قبل از اجرا با اطلاعات سیستم خودت تنظیم کنید

engine = create_engine(
    "mysql+pymysql://USERNAME:PASSWORD@localhost:3306/basketball_db"
)


# =========================
# 2. Load Data From SQL View
# =========================

query = """
SELECT *
FROM player_performance_analysis;
"""


df = pd.read_sql(
    query,
    engine
)


# =========================
# 3. Create EDA Object
# =========================

eda = EDA(df)


# =========================
# 4. Create Reports Folder
# =========================

os.makedirs(
    "reports/figures",
    exist_ok=True
)


# =========================
# 5. Basic Report
# =========================

print("Dataset Shape:")
print(eda.shape())


print("\nMissing Values:")
print(eda.missing_values())


print("\nDuplicates:")
print(eda.duplicates())


print("\nStatistics:")
print(eda.statistics())


# =========================
# 6. Player Analysis
# =========================

print("\nTop Players By BPM:")
print(
    eda.top_players("bpm")
)


print("\nTop Players By VORP:")
print(
    eda.top_players("vorp")
)


# =========================
# 7. Team Analysis
# =========================

print("\nTeam Ranking:")
print(
    eda.team_analysis()
)


# =========================
# 8. Save Figures
# =========================

eda.plot_correlation(
    "reports/figures/correlation.png"
)


eda.plot_distribution(
    "age",
    "reports/figures/age_distribution.png"
)


eda.plot_distribution(
    "bpm",
    "reports/figures/bpm_distribution.png"
)