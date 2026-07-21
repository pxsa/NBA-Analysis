# NBA Analysis

An end-to-end NBA data project — from web scraping, through storage in a relational MySQL database, to exploratory data analysis (EDA).

Player information, seasonal advanced stats, championship team rosters, and MVP award data are scraped from the source, cleaned, normalized, and stored in a relational database. The resulting data is then explored through statistical analysis and visualization.

## Content

- [Features](#features)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Domain Knowledge](#domain-knowledge)
- [Data Source](#data-source)

## Features

- **Web Scraping**
  - Extraction of raw HTML from player pages and team pages
  - Conversion of raw HTML into structured data files

- **Data Preprocessing**
  - Cleaning and standardizing the data
  - Preparing player information, position, country, college, and season stats

- **Relational Database**
  - Schema design and storage in MySQL
  - 11 normalized tables modeling the relationships within NBA data

- **Exploratory Data Analysis (EDA)**
  - Statistical analysis of the data
  - Examination of variable distributions, correlations, and player performance



## Project Structure

```
NBA-Analysis/
│
├── Data/
│   ├── raw_data/
│   │   ├── players.csv
│   │   ├── advanced_stats_all_seasons.csv
│   │   ├── champion_players_all_seasons.csv
│   │   └── mvp_all_seasons.csv
│   │
│   ├── raw_html/
│   │   ├── advanced_stats/
│   │   ├── awards/
│   │   ├── champion_teams/
│   │   └── league_summary/
│   │
│   └── sample/
│
├── database/
│   ├── schema.sql
│   └── DataBase.ipynb
│
├── preprocessing/
│   └── preprocessing.ipynb
│
├── scraping/
│   ├── players_get_html.ipynb
│   ├── players_get_html.py
│   ├── players_parse_html.ipynb
│   ├── players_parse_html.py
│   ├── team.ipynb
│   └── team.py
│
├── analysis/
│   ├── analysis.ipynb
│   ├── phase3_analysis.ipynb
│   └── plots/
│
├── src/
│   ├── eda.py
│   └── preprocessing.py
│
├── reports/
│   └── figures/
│
├── run_eda.py
├── requirements.txt
├── .env-example
├── NBA_Domain_Knowledge.md
└── README.md
```



## Database Schema

The database consists of 11 normalized tables:

```
country
college
position
season
team
player
player_college
player_position
player_season_stats
mvp_award
champion_team_player
```

These tables model the relationships between players, teams, seasons, countries, colleges, and NBA awards.

The full database structure is defined in:

```
database/schema.sql
```


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pxsa/NBA-Analysis.git
cd NBA-Analysis
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Rename `.env-example` to `.env` and fill in your database credentials:

```
DB_USERNAME=root
PASSWORD=your_mysql_password
HOST=localhost
PORT=3306
DATABASE=basketball_db
```



## Usage

### 1. Web Scraping

To run the scraping scripts:

```bash
python scraping/players_get_html.py
python scraping/players_parse_html.py
python scraping/team.py
```

Or run the notebook versions:

```bash
jupyter notebook scraping/
```

### 2. Data Preprocessing

To run the cleaning pipeline:

```bash
python src/preprocessing.py
```

Or the notebook version:

```bash
jupyter notebook preprocessing/preprocessing.ipynb
```

### 3. Database

First execute the schema to set up the database structure:

```
database/schema.sql
```

The processed data is then loaded into the MySQL database.

### 4. Exploratory Data Analysis (EDA)

To run the analysis:

```bash
python run_eda.py
```

The output — statistical reports and data visualizations — is saved to `reports/figures/`, with the notebook-based analysis figures available in `analysis/plots/`.



## Results

> **Note:** The captions below are placeholders inferred from figure filenames and section labels (`h1`, `h2`, `q1`, `q2`). Since I haven't reviewed the actual notebook output, edit each caption to reflect your real findings before publishing.

### General EDA

Overview of feature distributions, position breakdowns, and trends across seasons.

<p align="center">
  <img src="analysis/plots/eda_distributions.png" width="90%" alt="Distribution of key numeric features">
</p>

*Distribution of key numeric features across the full player-season dataset.*

<p align="center">
  <img src="analysis/plots/eda_positions.png" width="90%" alt="Breakdown by player position">
</p>

*Breakdown of players by position.*

<p align="center">
  <img src="analysis/plots/eda_season_trend.png" width="90%" alt="Trends across NBA seasons">
</p>

*Trends across the seasons covered by this dataset (2019-20 through 2025-26).*

### Categorical Feature Distributions

<table>
<tr>
<td><img src="analysis/plots/position_code_bar_chart.png" width="100%"></td>
<td><img src="analysis/plots/height_bin_bar_chart.png" width="100%"></td>
</tr>
<tr>
<td align="center"><em>Player counts by position</em></td>
<td align="center"><em>Player counts by height bin</em></td>
</tr>
<tr>
<td><img src="analysis/plots/shoots_bar_chart.png" width="100%"></td>
<td><img src="analysis/plots/season_name_bar_chart.png" width="100%"></td>
</tr>
<tr>
<td align="center"><em>Player counts by shooting hand</em></td>
<td align="center"><em>Player counts by season</em></td>
</tr>
<tr>
<td><img src="analysis/plots/low_sample_bar_chart.png" width="100%"></td>
<td></td>
</tr>
<tr>
<td align="center"><em>Players flagged as low-sample (limited minutes/games)</em></td>
<td></td>
</tr>
</table>

### Q1 — Height Analysis

<p align="center">
  <img src="analysis/plots/q1_height_dist.png" width="48%" alt="Height distribution">
  <img src="analysis/plots/q1_height_KDE.png" width="48%" alt="Height KDE">
</p>

*Distribution and KDE of player height (cm) across the dataset.*

### Q2 — Champions vs. Top-15

<p align="center">
  <img src="analysis/plots/q2_champ_vs_top15.png" width="90%" alt="Champions vs top 15 comparison">
</p>

*Comparison between championship-roster players and the top-15 players by performance metric.*

### H1 — Agility Hypothesis

<p align="center">
  <img src="analysis/plots/h1_agility_boxplot.png" width="70%" alt="Agility boxplot">
</p>

*Boxplot comparing the `agility` feature across groups tested in Hypothesis 1.*

### H2 — Innate Ability Hypothesis

<p align="center">
  <img src="analysis/plots/h2_innate_ability_boxplot.png" width="70%" alt="Innate ability boxplot">
</p>

*Boxplot comparing the `innate_ability` feature across groups tested in Hypothesis 2.*

For the full statistical write-up — hypotheses, test statistics, and p-values — see `analysis/analysis.ipynb` and `analysis/phase3_analysis.ipynb`.



## Domain Knowledge

For background on the NBA concepts used throughout this project, see:

```
NBA_Domain_Knowledge.md
```



## Data Source

Data for this project was collected from [Basketball-Reference.com](https://www.basketball-reference.com).
