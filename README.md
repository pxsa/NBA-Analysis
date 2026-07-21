# NBA Analysis

An end-to-end NBA data project — from web scraping, through storage in a relational MySQL database, to exploratory data analysis (EDA).

Player information, seasonal advanced stats, championship team rosters, and MVP award data are scraped from the source, cleaned, normalized, and stored in a relational database. The resulting data is then explored through statistical analysis and visualization.

---

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

---

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

---

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

---

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

---

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

The output — statistical reports and data visualizations — is saved to:

```
reports/figures/
```

Additional plots from the notebook-based analysis are available in:

```
analysis/plots/
```

---

## Domain Knowledge

For background on the NBA concepts used throughout this project, see:

```
NBA_Domain_Knowledge.md
```

---

## Data Source

Data for this project was collected from [Basketball-Reference.com](https://www.basketball-reference.com).

---

## License

This project was developed strictly for educational and practice purposes.