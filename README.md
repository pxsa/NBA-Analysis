# NBA Analysis

پروژه‌ی تحلیل داده‌های NBA — از اسکرپینگ خام سایت تا دیتابیس نرمالایز‌شده و داشبورد EDA.

این پروژه اطلاعات بازیکنان، آمار پیشرفته‌ی فصلی، تیم‌های قهرمان، و رأی‌های MVP لیگ NBA را از منبع خام جمع‌آوری، تمیزکاری، در یک دیتابیس رابطه‌ای MySQL ذخیره، و در نهایت با تحلیل اکتشافی داده (EDA) بررسی می‌کند.

---

## Features

- **Web Scraping**: استخراج HTML خام صفحات بازیکنان، آمار پیشرفته، تیم‌های قهرمان، و خلاصه‌ی هر فصل لیگ
- **Data Preprocessing**: تمیزکاری و نرمالایز کردن داده‌های خام (استانداردسازی پوزیشن، ملیت، کالج، و...)
- **Relational Database**: ذخیره‌ی داده‌ها در یک دیتابیس MySQL با ۱۱ جدول نرمالایز‌شده
- **Exploratory Data Analysis (EDA)**: تحلیل آماری و مصورسازی داده (توزیع سن، BPM، همبستگی متغیرها و...)

---

## Project Structure

```
NBA-Analysis-master/
│
├── Data/
│   ├── raw_data/              # فایل‌های CSV خام قبل از تمیزکاری
│   │   ├── players.csv
│   │   ├── advanced_stats_all_seasons.csv
│   │   ├── champion_players_all_seasons.csv
│   │   └── mvp_all_seasons.csv
│   ├── raw_html/               # صفحات HTML خام اسکرپ‌شده (قبل از پارس)
│   │   ├── advanced_stats/
│   │   ├── awards/
│   │   ├── champion_teams/
│   │   └── league_summary/
│   └── sample/                 # نمونه‌ی کوچک داده برای تست سریع
│
├── database/
│   └── schema.sql              # ساختار دیتابیس MySQL (۱۱ جدول)
│
├── preprocessing/
│   └── preprocessing.ipynb     # تمیزکاری داده + نوشتن در دیتابیس (to_sql)
│
├── scraping/
│   ├── players_get_html.ipynb  # دانلود HTML خام صفحات بازیکنان
│   └── players_parse_html.ipynb# پارس HTML به CSV ساختاریافته
│
├── reports/
│   └── figures/                # نمودارهای خروجی EDA (توزیع سن، BPM، همبستگی)
│
├── src/
│   └── eda.py                  # کلاس‌های OOP برای تحلیل اکتشافی داده
│
├── EDA.ipynb                   # اجرای تعاملی EDA
├── run_eda.py                  # اجرای EDA به‌صورت اسکریپت مستقل
├── requirements.txt
├── .env-example                # نمونه‌ی متغیرهای محیطی (بدون اطلاعات حساس)
├── NBA_Domain_Knowledge.md     # مستندات دانش حوزه NBA (برای فهم مفاهیم پروژه)
└── README.md
```

---

## Database Schema

دیتابیس شامل ۱۱ جدول نرمالایز‌شده است که رابطه‌ی بازیکنان با کشور، کالج، پوزیشن، فصل، تیم، و جوایز را مدل می‌کند:

`country` · `college` · `position` · `season` · `team` · `player` · `player_college` · `player_position` · `player_season_stats` · `mvp_award` · `champion_team_player`

ساختار کامل در [`database/schema.sql`](database/schema.sql) موجود است.

---

## Installation

### 1. Clone کردن ریپو

```bash
git clone https://github.com/pxsa/NBA-Analysis.git
cd NBA-Analysis
```

### 2. نصب پیش‌نیازها

```bash
pip install -r requirements.txt
```

### 3. تنظیم متغیرهای محیطی

فایل `.env-example` را کپی کرده و به `.env` تغییر نام دهید، سپس مقادیر را با اطلاعات دیتابیس خودتان پر کنید:

```bash
cp .env-example .env
```

```
DB_USERNAME=root
PASSWORD=your_mysql_password
HOST=localhost
PORT=3306
DATABASE=basketball_db
```

### 4. ساخت دیتابیس

اسکریپت `database/schema.sql` را روی MySQL Server خودتان اجرا کنید (با MySQL Workbench، DataGrip، یا خط فرمان) تا جدول‌های خالی ساخته شوند.

---

## Usage

### مرحله 1: اسکرپینگ (اختیاری — داده‌ی خام از قبل در Data/raw_data/ موجود است)

```bash
jupyter notebook scraping/players_get_html.ipynb
jupyter notebook scraping/players_parse_html.ipynb
```

### مرحله 2: تمیزکاری و پر کردن دیتابیس

```bash
jupyter notebook preprocessing/preprocessing.ipynb
```
این نوت‌بوک را از ابتدا تا انتها اجرا کنید (Run All) — داده‌های خام را می‌خواند، تمیز می‌کند، و در دیتابیس MySQL می‌نویسد.

### مرحله 3: تحلیل اکتشافی داده (EDA)

```bash
python run_eda.py
```
یا به‌صورت تعاملی:
```bash
jupyter notebook EDA.ipynb
```

خروجی شامل گزارش متنی (eda_report.txt) و نمودارها (در reports/figures/) خواهد بود.

---

## Learn More

برای آشنایی با اصطلاحات و قوانین NBA که در این پروژه استفاده شده‌اند، به [`NBA_Domain_Knowledge.md`](NBA_Domain_Knowledge.md) مراجعه کنید.

---

## Data Source

داده‌ها از [Basketball-Reference.com](https://www.basketball-reference.com) استخراج شده‌اند.

---

## License

این پروژه صرفاً برای اهداف آموزشی ساخته شده است.
