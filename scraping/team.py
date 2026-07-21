#!/usr/bin/env python
# coding: utf-8

# # Downloading HTML files

# In[33]:


import requests
from bs4 import BeautifulSoup, Comment
import pandas as pd
import time
from pathlib import Path
import pandas as pd
import os


# In[2]:


YEARS = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
PATH = '../Data/raw_html'
PROCESSED_DATA_PATH = '../Data/raw_data'
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36"
    )
}


# In[3]:


#  html mpv (NBA Awards Voting)
save_folder = Path(os.path.join(PATH, 'awards'))
save_folder.mkdir(parents=True, exist_ok=True)

for year in YEARS:
    url = f"https://www.basketball-reference.com/awards/awards_{year}.html"
    file_path = save_folder / f"awards_{year}.html"

    # اگر فایل قبلاً سالم ذخیره شده، دوباره دانلودش نکن
    if file_path.exists() and file_path.stat().st_size > 0:
        print(f"Skipped: {file_path.name}")
        continue

    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()

        file_path.write_bytes(response.content)

        print(
            f"Saved: {file_path.name} | "
            f"status={response.status_code} | "
            f"size={file_path.stat().st_size} bytes"
        )

        # فاصله بین درخواست‌ها
        time.sleep(3)

    except requests.RequestException as error:
        print(f"Failed for {year}: {error}")


# In[5]:


#چک کردن اینکه کد ها ذخیره شدن
saved_files = sorted(save_folder.glob("*.html"))

for file in saved_files:
    print(file.name, file.stat().st_size)


# In[6]:


# html season stats

save_folder = Path(os.path.join(PATH, 'advanced_stats'))
save_folder.mkdir(parents=True, exist_ok=True)


for year in YEARS:
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_advanced.html"
    file_path = save_folder / f"NBA_{year}_advanced.html"

    if file_path.exists() and file_path.stat().st_size > 0:
        print(f"Skipped: {file_path.name}")
        continue

    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()

        file_path.write_bytes(response.content)

        print(
            f"Saved: {file_path.name} | "
            f"status={response.status_code} | "
            f"size={file_path.stat().st_size} bytes"
        )

        time.sleep(3)

    except requests.RequestException as error:
        print(f"Failed for {year}: {error}")


# In[7]:


#بررسی فایل ها

saved_files = sorted(save_folder.glob("*.html"))

for file in saved_files:
    print(file.name, file.stat().st_size)


# In[8]:


#تیم های قهرمان html
save_folder = Path(os.path.join(PATH, 'league_summary'))
save_folder.mkdir(parents=True, exist_ok=True)


for year in YEARS:
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}.html"
    file_path = save_folder / f"NBA_{year}.html"

    if file_path.exists() and file_path.stat().st_size > 0:
        print(f"Skipped: {file_path.name}")
        continue

    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()

        file_path.write_bytes(response.content)

        print(
            f"Saved: {file_path.name} | "
            f"status={response.status_code} | "
            f"size={file_path.stat().st_size} bytes"
        )

        time.sleep(3)

    except requests.RequestException as error:
        print(f"Failed for {year}: {error}")




# In[9]:


#بررسی
saved_files = sorted(save_folder.glob("*.html"))

for file in saved_files:
    print(file.name, file.stat().st_size)


# In[10]:


# html champion team 
save_folder = Path(os.path.join(PATH, 'champion_teams'))
save_folder.mkdir(parents=True, exist_ok=True)

# سال پایان فصل: کد تیم قهرمان
champions = {
    2020: "LAL",  # Los Angeles Lakers — 2019-20
    2021: "MIL",  # Milwaukee Bucks — 2020-21
    2022: "GSW",  # Golden State Warriors — 2021-22
    2023: "DEN",  # Denver Nuggets — 2022-23
    2024: "BOS",  # Boston Celtics — 2023-24
    2025: "OKC",  # Oklahoma City Thunder — 2024-25
    2026: "NYK",  # New York Knicks — 2025-26
}

for year, team_code in champions.items():
    url = (
        f"https://www.basketball-reference.com/"
        f"teams/{team_code}/{year}.html"
    )

    file_path = save_folder / f"{team_code}_{year}.html"

    # اگر فایل قبلاً سالم ذخیره شده، دوباره درخواست نزن
    if file_path.exists() and file_path.stat().st_size > 0:
        print(f"Skipped: {file_path.name}")
        continue

    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()

        file_path.write_bytes(response.content)

        print(
            f"Saved: {file_path.name} | "
            f"status={response.status_code} | "
            f"size={file_path.stat().st_size} bytes"
        )

        time.sleep(3)

    except requests.RequestException as error:
        print(
            f"Failed: season={year}, team={team_code} | "
            f"{error}"
        )


# In[11]:


#بررسی
saved_files = sorted(save_folder.glob("*.html"))
for file in saved_files:
    print(file.name, file.stat().st_size)


# # Using BS4 to Scrapping data

# In[12]:


SEASONS = {
    2020: "2019-20",
    2021: "2020-21",
    2022: "2021-22",
    2023: "2022-23",
    2024: "2023-24",
    2025: "2024-25",
    2026: "2025-26",
}

output_folder = Path(PROCESSED_DATA_PATH)
output_folder.mkdir(parents=True, exist_ok=True)


# ## Awards

# In[13]:


# for all seasons (mvp)
# پوشه HTMLهای Awards
awards_folder = Path(os.path.join(PATH, 'awards'))

all_mvp_players = []

for year, season in SEASONS.items():

    # 1) مسیر فایل همان فصل
    file_path = awards_folder / f"awards_{year}.html"

    # 2) خواندن HTML ذخیره‌شده
    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()

    # 3) پارس HTML
    soup = BeautifulSoup(html, "html.parser")

    # 4) پیدا کردن جدول MVP
    mvp_table = soup.find("table", id="mvp")

    if mvp_table is None:
        print(f"MVP table not found for {season}")
        continue

    # 5) گرفتن ردیف‌های بازیکنان
    rows = mvp_table.find("tbody").find_all("tr")

    # 6) استخراج بازیکنان همان فصل
    for row in rows:
        rank_cell = row.find("th", {"data-stat": "rank"})
        player_cell = row.find("td", {"data-stat": "player"})
        team_cell = row.find("td", {"data-stat": "team_id"})
        share_cell = row.find("td", {"data-stat": "award_share"})

        if player_cell is None:
            continue

        player_link_tag = player_cell.find("a")

        player_record = {
            "season": season,
            "mvp_rank": rank_cell.get_text(strip=True) if rank_cell else None,
            "player_id": player_cell.get("data-append-csv"),
            "player_name": player_cell.get_text(strip=True),
            "player_url": player_link_tag.get("href") if player_link_tag else None,
            "team": team_cell.get_text(strip=True) if team_cell else None,
            "mvp_share": share_cell.get_text(strip=True) if share_cell else None
        }

        all_mvp_players.append(player_record)

    print(f"{season}: {len(rows)} rows processed")


# In[14]:


mvp_all_seasons_df = pd.DataFrame(all_mvp_players)


# In[15]:


# THIS LINE PREVENT NAN BECAUSE SOME RANK CONTAINS LETTER `T`
mvp_all_seasons_df["mvp_rank"] = (
    mvp_all_seasons_df["mvp_rank"]
    .apply(lambda x: x.replace("T", "") if isinstance(x, str) else x)
)


mvp_all_seasons_df["mvp_rank"] = pd.to_numeric(
    mvp_all_seasons_df["mvp_rank"],
    errors="coerce"
)

mvp_all_seasons_df["mvp_share"] = pd.to_numeric(
    mvp_all_seasons_df["mvp_share"],
    errors="coerce"
)


# In[16]:


mvp_all_seasons_df
mvp_all_seasons_df.groupby("season").size()


# In[17]:


output_folder = Path(PROCESSED_DATA_PATH)
output_folder.mkdir(exist_ok=True)

output_path = output_folder / "mvp_all_seasons.csv"

mvp_all_seasons_df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print(output_path.resolve())


# In[18]:


mvp_all_seasons_df.isna().sum()


# ## Advance Stats

# In[38]:


advanced_folder = Path(os.path.join(PATH, 'advanced_stats'))
output_folder = Path(PROCESSED_DATA_PATH)
output_folder.mkdir(parents=True, exist_ok=True)


# -----------------------------
# پارس یک ردیف بازیکن
# -----------------------------

def parse_player_row(row, season):

    def text(selector):
        element = row.select_one(selector)

        if element is None:
            return None

        return " ".join(
            element.get_text(" ", strip=True).split()
        )

    player_cell = row.select_one(
        'td[data-stat="name_display"], '
        'th[data-stat="name_display"]'
    )

    if player_cell is None:
        return None

    player_link = player_cell.select_one("a")

    player_id = player_cell.get("data-append-csv")

    player_relative_url = (
        player_link.get("href")
        if player_link is not None
        else None
    )

    player_url = (
        f"https://www.basketball-reference.com{player_relative_url}"
        if player_relative_url
        else None
    )

    return {
        "season": season,
        "player_id": player_id,
        "player_name": text(
            'td[data-stat="name_display"], '
            'th[data-stat="name_display"]'
        ),
        "player_url": player_url,
        "age": text('td[data-stat="age"]'),
        "team": text('td[data-stat="team_name_abbr"]'),
        "position": text('td[data-stat="pos"]'),
        "games": text('td[data-stat="games"]'),
        "games_started": text('td[data-stat="games_started"]'),
        "minutes": text('td[data-stat="mp"]'),
        "win_shares": text('td[data-stat="ws"]'),
        "ws_per_48": text('td[data-stat="ws_per_48"]'),
        "bpm": text('td[data-stat="bpm"]'),
        "vorp": text('td[data-stat="vorp"]'),
    }

def find_advanced_table(soup):

    table = soup.select_one("table#advanced")

    if table is not None:
        return table

    comments = soup.find_all(
        string=lambda text: isinstance(text, Comment)
    )

    for comment in comments:

        if 'id="advanced"' not in comment:
            continue

        comment_soup = BeautifulSoup(comment, "html.parser")
        table = comment_soup.select_one("table#advanced")

        if table is not None:
            return table

    return None
# -----------------------------
# استخراج پنج فصل
# -----------------------------

all_advanced_records = []

for year, season in SEASONS.items():

    file_path = advanced_folder / f"NBA_{year}_advanced.html"

    if not file_path.exists():
        print(f"File not found: {file_path}")
        continue

    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    advanced_table = find_advanced_table(soup)

    if advanced_table is None:
        print(f"Advanced table not found for {season}")
        continue

    rows = advanced_table.select("tbody tr")

    season_count = 0

    for row in rows:
        record = parse_player_row(row, season)

        if record is None:
            continue

        if record["player_id"] is None:
            continue

        all_advanced_records.append(record)
        season_count += 1

    print(f"{season}: {season_count} valid rows extracted")


# -----------------------------
# ساخت DataFrame
# -----------------------------

advanced_raw_df = pd.DataFrame(all_advanced_records)

numeric_columns = [
    "age",
    "games",
    "games_started",
    "minutes",
    "win_shares",
    "ws_per_48",
    "bpm",
    "vorp",
]

for column in numeric_columns:
    advanced_raw_df[column] = pd.to_numeric(
        advanced_raw_df[column],
        errors="coerce"
    )


# -----------------------------
# مدیریت بازیکنان چندتیمی
# -----------------------------

def choose_player_season_row(group):

    team_values = group["team"].fillna("")

    total_team_mask = team_values.str.match(r"^\d+TM$")

    if total_team_mask.any():
        return group.loc[total_team_mask].iloc[0]

    return group.sort_values(
        by=["minutes", "games"],
        ascending=False,
        na_position="last"
    ).iloc[0]


advanced_clean_df = (
    advanced_raw_df
    .groupby(["season", "player_id"], group_keys=True)
    .apply(choose_player_season_row)
    .reset_index()          # brings season & player_id back as columns
)

# -----------------------------
# مرتب‌سازی و کنترل
# -----------------------------

advanced_clean_df = advanced_clean_df.sort_values(
    by=["season", "win_shares"],
    ascending=[True, False],
    na_position="last"
).reset_index(drop=True)

print("\nRaw rows per season:")
print(advanced_raw_df.groupby("season").size())

print("\nUnique players per season:")
print(advanced_clean_df.groupby("season").size())

display(advanced_clean_df.head(10))


# -----------------------------
# ذخیره فایل‌ها
# -----------------------------

raw_path = output_folder / "advanced_stats_all_rows.csv"
clean_path = output_folder / "advanced_stats_all_seasons.csv"

advanced_raw_df.to_csv(
    raw_path,
    index=False,
    encoding="utf-8-sig"
)

advanced_clean_df.to_csv(
    clean_path,
    index=False,
    encoding="utf-8-sig"
)

print("\nSaved raw file:")
print(raw_path.resolve())

print("\nSaved cleaned file:")
print(clean_path.resolve())


# In[42]:


advanced_clean_df.info()


# In[43]:


advanced_raw_df.info()


# ## Champion

# In[45]:


# --------------------------------
# مسیر فایل‌ها و اطلاعات قهرمانان
# --------------------------------
champion_folder = Path(os.path.join(PATH, 'champion_teams'))
output_folder = Path(PROCESSED_DATA_PATH)
output_folder.mkdir(parents=True, exist_ok=True)

champion_files = [
    {
        "season": "2020-21",
        "champion_team": "Milwaukee Bucks",
        "team_code": "MIL",
        "file_name": "MIL_2021.html",
    },
    {
        "season": "2021-22",
        "champion_team": "Golden State Warriors",
        "team_code": "GSW",
        "file_name": "GSW_2022.html",
    },
    {
        "season": "2022-23",
        "champion_team": "Denver Nuggets",
        "team_code": "DEN",
        "file_name": "DEN_2023.html",
    },
    {
        "season": "2023-24",
        "champion_team": "Boston Celtics",
        "team_code": "BOS",
        "file_name": "BOS_2024.html",
    },
    {
        "season": "2024-25",
        "champion_team": "Oklahoma City Thunder",
        "team_code": "OKC",
        "file_name": "OKC_2025.html",
    },
    {
        "season": "2025-26",
        "champion_team": "New York Knicks",
        "team_code": "NYK",
        "file_name": "NYK_2026.html",
    },
]

# --------------------------------
# تبدیل یک ردیف roster به یک رکورد
# --------------------------------

def parse_roster_row(row, season, champion_team, team_code):

    def txt(data_stat):
        element = row.find(
            ["td", "th"],
            {"data-stat": data_stat},
        )
        if element is None:
            return None

        return " ".join(element.get_text(" ", strip=True).split())


    player_cell = row.find(
        ["td", "th"],
        {"data-stat": "player"},
    )

    if player_cell is None:
        return None

    player_link = player_cell.find("a")

    player_id = player_cell.get("data-append-csv")

    # اگر شناسه مستقیماً موجود نبود، از لینک استخراج شود
    if player_id is None and player_link is not None:
        href = player_link.get("href")

        if href:
            player_id = Path(href).stem

    relative_url = (
        player_link.get("href")
        if player_link is not None
        else None
    )

    player_url = (
        f"https://www.basketball-reference.com{relative_url}"
        if relative_url
        else None
    )

    return {
        "season": season,
        "champion_team": champion_team,
        "team_code": team_code,
        "player_id": player_id,
        "player_name": txt("player"),
        "player_url": player_url,
        "number": txt("number"),
        "position": txt("pos"),
        "height": txt("height"),
        "weight": txt("weight"),
        "birth_date": txt("birth_date"),
        "birth_place": txt("flag"),
        "experience": txt("years_experience"),
        "college": txt("college"),
    }


# --------------------------------
# خواندن چهار فایل و استخراج بازیکنان
# --------------------------------

champion_records = []

for champion in champion_files:

    file_path = champion_folder / champion["file_name"]

    if not file_path.exists():
        print(f"File not found: {file_path}")
        continue

    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    roster_table = soup.find("table", id="roster")

    if roster_table is None:
        print(f"Roster table not found: {champion['season']}")
        continue

    tbody = roster_table.find("tbody")

    if tbody is None:
        print(f"tbody not found: {champion['season']}")
        continue

    rows = tbody.find_all("tr")

    season_count = 0

    for row in rows:
        record = parse_roster_row(
            row=row,
            season=champion["season"],
            champion_team=champion["champion_team"],
            team_code=champion["team_code"],
        )

        if record is None:
            continue

        if record["player_id"] is None:
            continue

        champion_records.append(record)
        season_count += 1

    print(
        f"{champion['season']} | "
        f"{champion['champion_team']}: "
        f"{season_count} players extracted"
    )


# --------------------------------
# ساخت DataFrame
# --------------------------------

champion_roster_df = pd.DataFrame(champion_records)

champion_roster_df["weight"] = pd.to_numeric(
    champion_roster_df["weight"],
    errors="coerce",
)

champion_roster_df["birth_date"] = pd.to_datetime(
    champion_roster_df["birth_date"],
    errors="coerce",
)

print("\nPlayers per champion team:")
print(
    champion_roster_df
    .groupby(["season", "champion_team"])
    .size()
)

display(champion_roster_df.head(10))


# --------------------------------
# اتصال به Advanced برای سن و بازی
# --------------------------------

advanced_for_merge = advanced_clean_df[
    [
        "season",
        "player_id",
        "age",
        "games",
        "minutes",
        "win_shares",
    ]
].copy()

champion_players_df = champion_roster_df.merge(
    advanced_for_merge,
    on=["season", "player_id"],
    how="left",
    validate="one_to_one",
)

print("\nMissing advanced matches:")
print(
    champion_players_df[
        champion_players_df["games"].isna()
    ][
        [
            "season",
            "champion_team",
            "player_name",
            "player_id",
        ]
    ]
)

display(champion_players_df.head(10))


# --------------------------------
# ذخیره خروجی‌ها
# --------------------------------

roster_path = output_folder / "champion_rosters.csv"
final_path = output_folder / "champion_players_all_seasons.csv"

champion_roster_df.to_csv(
    roster_path,
    index=False,
    encoding="utf-8-sig",
)

champion_players_df.to_csv(
    final_path,
    index=False,
    encoding="utf-8-sig",
)

print("\nSaved roster file:")
print(roster_path.resolve())

print("\nSaved merged file:")
print(final_path.resolve())


# In[46]:


champion_roster_df.info()


# In[47]:


champion_players_df.info()


# In[ ]:




