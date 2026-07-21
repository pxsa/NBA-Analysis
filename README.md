# NBA Analysis

پروژه‌ی تحلیل داده‌های NBA — از جمع‌آوری داده با Web Scraping تا ذخیره‌سازی در دیتابیس رابطه‌ای MySQL و تحلیل اکتشافی داده (EDA).

در این پروژه اطلاعات بازیکنان NBA، آمار پیشرفته‌ی فصلی، تیم‌های قهرمان و جوایز MVP از منبع خام استخراج، پاک‌سازی، نرمال‌سازی و در یک دیتابیس رابطه‌ای ذخیره شده‌اند. در نهایت داده‌ها برای تحلیل آماری و مصورسازی مورد بررسی قرار گرفته‌اند.

---

## Features

* **Web Scraping**

  * استخراج HTML خام صفحات بازیکنان و اطلاعات تیم‌ها
  * تبدیل داده‌های خام HTML به فایل‌های ساختاریافته

* **Data Preprocessing**

  * پاک‌سازی و استانداردسازی داده‌ها
  * آماده‌سازی اطلاعات بازیکنان، پوزیشن، کشور، کالج و آمار فصل‌ها

* **Relational Database**

  * طراحی و ذخیره داده‌ها در MySQL
  * استفاده از ۱۱ جدول نرمالایز شده برای مدل‌سازی روابط NBA

* **Exploratory Data Analysis (EDA)**

  * تحلیل آماری داده‌ها
  * بررسی توزیع متغیرها، همبستگی‌ها و عملکرد بازیکنان

---

# Project Structure

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
│   └── phase3_analysis.ipynb
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

# Database Schema

دیتابیس شامل ۱۱ جدول نرمالایز شده است:

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

این جداول ارتباط بازیکنان با تیم‌ها، فصل‌ها، کشور، کالج، پوزیشن و جوایز NBA را مدل می‌کنند.

ساختار کامل دیتابیس در فایل زیر قرار دارد:

```
database/schema.sql
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/pxsa/NBA-Analysis.git
cd NBA-Analysis
```

## 2. Install Requirements

```bash
pip install -r requirements.txt
```

## 3. Environment Variables

فایل `.env-example` را به `.env` تغییر دهید و اطلاعات دیتابیس خود را وارد کنید:

```
DB_USERNAME=root
PASSWORD=your_mysql_password
HOST=localhost
PORT=3306
DATABASE=basketball_db
```

---

# Usage

## 1. Web Scraping

برای اجرای اسکرپینگ:

```bash
python scraping/players_get_html.py
python scraping/players_parse_html.py
python scraping/team.py
```

یا اجرای نسخه Notebook:

```bash
jupyter notebook scraping/
```

---

## 2. Data Preprocessing

برای اجرای مراحل پاک‌سازی داده:

```bash
python src/preprocessing.py
```

یا نسخه Notebook:

```bash
jupyter notebook preprocessing/preprocessing.ipynb
```

---

## 3. Database

ساختار دیتابیس را ابتدا اجرا کنید:

```
database/schema.sql
```

سپس اطلاعات پردازش‌شده در دیتابیس MySQL ذخیره می‌شوند.

---

## 4. Exploratory Data Analysis (EDA)

اجرای تحلیل:

```bash
python run_eda.py
```

خروجی شامل گزارش آماری و نمودارهای تحلیل داده در پوشه:

```
reports/figures/
```

ذخیره می‌شود.

---

# Domain Knowledge

برای آشنایی با مفاهیم NBA استفاده شده در پروژه، به فایل زیر مراجعه کنید:

```
NBA_Domain_Knowledge.md
```

---

# Data Source

داده‌های این پروژه از:

Basketball-Reference.com

جمع‌آوری شده‌اند.

---

# License

این پروژه صرفاً با هدف آموزشی و تمرینی توسعه داده شده است.
