
## 1. NBA چیست؟

NBA (National Basketball Association) بزرگ‌ترین لیگ بسکتبال حرفه‌ای جهان است.

- دارای ۳۰ تیم است.
- در آمریکا و کانادا برگزار می‌شود.
- هر سال یک فصل (Season) برگزار می‌کند.
- هر فصل از اکتبر شروع شده و تا ژوئن سال بعد ادامه دارد.

---

## 2. ساختار کلی NBA

```text
NBA
├── Eastern Conference
└── Western Conference
```

هر کنفرانس:
- ۱۵ تیم دارد.
- ۳ Division دارد.

---

## 3. Conference (کنفرانس)

دو کنفرانس اصلی:

| کنفرانس | تعداد تیم |
|---|---|
| Eastern Conference | ۱۵ |
| Western Conference | ۱۵ |

---

## 4. Division (دیویژن)

هر کنفرانس دارای سه Division است.

**Western Conference:** Pacific · Northwest · Southwest

**Eastern Conference:** Atlantic · Central · Southeast

```text
NBA
│
├── Eastern
│      ├── Atlantic
│      ├── Central
│      └── Southeast
│
└── Western
       ├── Pacific
       ├── Northwest
       └── Southwest
```

---

## 5. Team (تیم)

هر تیم شامل: نام تیم، شهر، کنفرانس، دیویژن، ورزشگاه، مربی، بازیکنان

نمونه: Los Angeles Lakers · Boston Celtics · Golden State Warriors

| فیلد | توضیح |
|---|---|
| team_id | شناسه تیم |
| team_name | نام تیم |
| city | شهر |
| abbreviation | مخفف |
| conference | کنفرانس |
| division | دیویژن |
| arena | ورزشگاه |

---

## 6. Arena (ورزشگاه)

هر تیم دارای یک ورزشگاه خانگی است.

اطلاعات: `arena_id` · `arena_name` · `city` · `state` · `capacity`

---

## 7. Season (فصل)

هر سال یک فصل جدید برگزار می‌شود. نمونه: `2023-24` · `2024-25` · `2025-26`

هر فصل شامل: Regular Season → Play-In → Playoffs → Finals

---

## 8. Player (بازیکن)

هر تیم حدود ۱۵ بازیکن دارد.

| فیلد | توضیح |
|---|---|
| player_id | شناسه |
| player_name | نام |
| birth_date | تاریخ تولد |
| height_cm | قد |
| weight_kg | وزن |
| nationality | ملیت |
| position | پست |

---

## 9. Position (پست بازیکنان)

۵ پست اصلی:

| مخفف | نام | توضیح |
|---|---|---|
| PG | Point Guard | بازی‌ساز، پاس‌دهنده اصلی |
| SG | Shooting Guard | امتیازآور، شوت‌زن |
| SF | Small Forward | ترکیبی از حمله و دفاع |
| PF | Power Forward | بازیکن قدرتی، ریباندگیر |
| C | Center | بلندقدترین بازیکن، دفاع و ریباند |

---

## 10. Coach (مربی)

هر تیم یک یا چند مربی در طول فصل دارد.

اطلاعات: `coach_id` · `coach_name` · `nationality` · `birth_date`

---

## 11. Game (بازی)

هر بازی شامل دو تیم، یک تاریخ، و یک نتیجه است.

| فیلد |
|---|
| game_id |
| season_id |
| game_date |
| home_team_id |
| away_team_id |
| arena_id |
| home_score |
| away_score |
| winner_team_id |

**Home Team:** تیمی که در ورزشگاه خودش بازی می‌کند.
**Away Team:** تیمی که مهمان است.

---

## 12. Regular Season

هر تیم `82 Games` بازی می‌کند. نتیجه هر بازی: Win (W) یا Loss (L)

### Win Percentage

```text
Win % = Wins / Total Games
```
مثال: `64 / 82 = 0.780`

---

## 13. Standings (جدول لیگ)

اطلاعات: Wins · Losses · Win Percentage · Conference Rank · Division Rank · Games Behind

---

## 14. Play-In Tournament

تیم‌های رتبه ۷ تا ۱۰ برای ورود به Playoffs رقابت می‌کنند.

## 15. Playoffs

مرحله حذفی لیگ.

## 16. NBA Finals

فینال NBA بین قهرمان دو کنفرانس برگزار می‌شود.

## 17. Champion

قهرمان نهایی فصل.

---

## 18. Player Statistics (آمار بازیکن)

بعد از هر بازی برای هر بازیکن ثبت می‌شود.

| مخفف | نام | توضیح |
|---|---|---|
| MIN | Minutes Played | مدت زمان بازی |
| PTS | Points | امتیاز |
| REB | Rebounds | توپ برگشتی |
| OREB | Offensive Rebound | ریباند حمله |
| DREB | Defensive Rebound | ریباند دفاع |
| AST | Assists | پاس گل |
| STL | Steals | توپ‌ربایی |
| BLK | Blocks | بلاک |
| TOV | Turnovers | از دست دادن توپ |
| PF | Personal Fouls | خطا |

---

## 19. Shooting Statistics

| مخفف | نام | فرمول |
|---|---|---|
| FGA | Field Goal Attempts | تعداد شوت زده شده |
| FGM | Field Goals Made | تعداد شوت موفق |
| FG% | Field Goal % | `FGM / FGA` |
| 3PA | Three Point Attempts | تعداد شوت سه امتیازی |
| 3PM | Three Point Made | تعداد سه امتیازی موفق |
| 3P% | Three Point % | `3PM / 3PA` |
| FTA | Free Throw Attempts | تعداد پرتاب آزاد |
| FTM | Free Throw Made | پرتاب آزاد موفق |
| FT% | Free Throw % | `FTM / FTA` |

---

## 20. Team Statistics (آمار تیم)

Points · Rebounds · Assists · Steals · Blocks · Turnovers · Fouls · Shooting Percentages

---

## 21. Advanced Statistics

| شاخص | توضیح |
|---|---|
| Pace | سرعت بازی — تعداد Possession در هر بازی |
| Offensive Rating (ORtg) | امتیاز تولیدشده در هر ۱۰۰ Possession |
| Defensive Rating (DRtg) | امتیاز دریافت‌شده در هر ۱۰۰ Possession |
| Net Rating | `ORtg - DRtg` |
| Usage Rate (USG%) | درصد حملاتی که توسط بازیکن استفاده می‌شود |
| True Shooting % (TS%) | شاخص واقعی بهره‌وری شوت‌زنی |
| Plus/Minus (+/-) | اختلاف امتیاز تیم هنگام حضور بازیکن در زمین |

---

## 22. اصطلاحات رایج NBA

| اصطلاح | توضیح |
|---|---|
| Double Double | حداقل ۱۰ واحد در دو شاخص آماری (مثلاً ۲۰ امتیاز + ۱۲ ریباند) |
| Triple Double | حداقل ۱۰ واحد در سه شاخص (مثلاً ۲۰ امتیاز + ۱۰ ریباند + ۱۱ پاس گل) |
| Quadruple Double | حداقل ۱۰ واحد در چهار شاخص |
| Sixth Man | بهترین بازیکن ذخیره |
| Clutch Time | دقایق حساس پایانی بازی |
| Back-to-Back (B2B) | دو بازی در دو روز متوالی |

---

## 23. سؤالات تحلیلی مناسب برای پروژه

- بهترین بازیکن هر فصل؟
- بهترین تیم هجومی؟ بهترین تیم دفاعی؟
- آیا بازی خانگی باعث افزایش شانس برد می‌شود؟
- آیا قد بازیکن با ریباند رابطه دارد؟
- آیا Turnover باعث باخت می‌شود؟
- آیا سن با عملکرد بازیکن رابطه دارد؟
- آیا Usage Rate با امتیاز رابطه دارد؟
- پیش‌بینی صعود به Playoffs
- پیش‌بینی برنده بازی

---

## 24. داده‌هایی که باید اسکرپ شوند

Teams · Players · Seasons · Games · Player Game Statistics · Team Game Statistics · Standings · Player Team History · Coaches · Arenas

---

## 25. نقشه راه پروژه

```text
Domain Knowledge
↓
Web Scraping
↓
Data Understanding
↓
Data Cleaning
↓
Database Design
↓
Normalization
↓
SQL Analysis
↓
EDA
↓
Missing Values
↓
Feature Engineering
↓
Statistical Tests
↓
Machine Learning
↓
Visualization & Presentation
```
