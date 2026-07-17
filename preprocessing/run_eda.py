import os
import pandas as pd
from sqlalchemy import create_engine

from src.eda import EDA


# ==========================================
# 1. Database Connection
# ==========================================
# تنظیمات اتصال به MySQL Database
# قبل از اجرا باید USERNAME و PASSWORD
# با اطلاعات دیتابیس سیستم خودتان جایگزین شود

engine = create_engine(
    "mysql+pymysql://USERNAME:PASSWORD@localhost:3306/basketball_db"
)


# ==========================================
# 2. Load Data From SQL View
# ==========================================
# داده نهایی مورد نیاز برای تحلیل
# از View ساخته شده در SQL خوانده می‌شود

query = """
SELECT *
FROM player_performance_analysis;
"""


df = pd.read_sql(
    query,
    engine
)


# ==========================================
# 3. Initialize EDA Class
# ==========================================
# ساخت آبجکت EDA
# تمام تحلیل‌ها از طریق این کلاس انجام می‌شود

eda = EDA(df)



# ==========================================
# 4. Create Output Folder
# ==========================================
# ساخت پوشه برای ذخیره نمودارها

os.makedirs(
    "reports/figures",
    exist_ok=True
)



# ==========================================
# 5. Data Quality Analysis
# ==========================================

print("Dataset Shape:")
print(eda.shape())


print("\nMissing Values:")
print(eda.missing_values())


print("\nDuplicates:")
print(eda.duplicates())


print("\nData Types:")
print(eda.data_types())


print("\nOutlier Summary:")
print(eda.outlier_summary())



# ==========================================
# 6. Statistical Analysis
# ==========================================

print("\nStatistical Summary:")
print(eda.statistics())



# ==========================================
# 7. Player Performance Analysis
# ==========================================
# بررسی بهترین بازیکنان بر اساس Metric های مختلف

print("\nTop Players By BPM:")
print(
    eda.top_players("bpm")
)


print("\nTop Players By VORP:")
print(
    eda.top_players("vorp")
)



# ==========================================
# 8. Team Performance Analysis
# ==========================================
# رتبه‌بندی تیم‌ها بر اساس مجموع Win Shares

print("\nTeam Ranking:")
print(
    eda.team_analysis()
)



# ==========================================
# 9. Visualization
# ==========================================
# ذخیره نمودارهای EDA

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



print("\nEDA Analysis Completed Successfully!")