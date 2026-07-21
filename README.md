# NBA Domain Knowledge Documentation

مستندات جامع دانش حوزه (Domain Knowledge) برای پروژه تحلیل داده‌های NBA — پایه‌ای برای Web Scraping، طراحی دیتابیس، و تحلیل داده.

---

## فهرست مطالب

1. [NBA چیست؟](#1-nba-چیست)
2. [ساختار کلی NBA](#2-ساختار-کلی-nba)
3. [Conference و Division](#3-conference-و-division)
4. [لیست کامل ۳۰ تیم](#4-لیست-کامل-۳۰-تیم)
5. [Team](#5-team-تیم)
6. [Arena](#6-arena-ورزشگاه)
7. [Season](#7-season-فصل)
8. [Player](#8-player-بازیکن)
9. [Position](#9-position-پست-بازیکنان)
10. [Coach](#10-coach-مربی)
11. [Game](#11-game-بازی)
12. [Regular Season](#12-regular-season)
13. [Standings](#13-standings-جدول-لیگ)
14. [Play-In, Playoffs, Finals](#14-play-in-tournament)
15. [Player Statistics](#18-player-statistics-آمار-بازیکن)
16. [Shooting Statistics](#19-shooting-statistics)
17. [Team Statistics](#20-team-statistics-آمار-تیم)
18. [Advanced Statistics](#21-advanced-statistics)
19. [جوایز فصلی NBA](#22-جوایز-فصلی-nba)
20. [Draft (درفت)](#23-draft-درفت)
21. [قراردادها و مسائل مالی](#24-قراردادها-و-مسائل-مالی)
22. [تقویم فصل](#25-تقویم-فصل)
23. [اصطلاحات رایج NBA](#26-اصطلاحات-رایج-nba)
24. [سؤالات تحلیلی مناسب برای پروژه](#27-سؤالات-تحلیلی-مناسب-برای-پروژه)
25. [داده‌هایی که باید اسکرپ شوند](#28-داده‌هایی-که-باید-اسکرپ-شوند)
26. [نقشه راه پروژه](#29-نقشه-راه-پروژه)

---

## 1. NBA چیست؟

NBA (National Basketball Association) بزرگ‌ترین و معتبرترین لیگ بسکتبال حرفه‌ای جهان است.

- تأسیس: ۱۹۴۶ (با نام BAA؛ در سال ۱۹۴۹ با NBL ادغام شد و NBA نام گرفت)
- دارای ۳۰ تیم است (۲۹ تیم آمریکایی + ۱ تیم کانادایی: تورنتو رپترز)
- هر تیم فصل منظم را با **۸۲ بازی** آغاز می‌کند
- فصل از اکتبر شروع شده و تا ژوئن سال بعد (با فینال‌ها) ادامه دارد
- کمیسیونر فعلی لیگ: آدام سیلور (Adam Silver)

---

## 2. ساختار کلی NBA

```text
NBA
├── Eastern Conference (15 تیم)
│      ├── Atlantic Division
│      ├── Central Division
│      └── Southeast Division
└── Western Conference (15 تیم)
       ├── Pacific Division
       ├── Northwest Division
       └── Southwest Division
```

هر Division شامل ۵ تیم است.

---

## 3. Conference و Division

| کنفرانس | Division | تعداد تیم |
|---|---|---|
| Eastern | Atlantic | 5 |
| Eastern | Central | 5 |
| Eastern | Southeast | 5 |
| Western | Pacific | 5 |
| Western | Northwest | 5 |
| Western | Southwest | 5 |

---

## 4. لیست کامل ۳۰ تیم

### Eastern Conference

**Atlantic:** Boston Celtics · Brooklyn Nets · New York Knicks · Philadelphia 76ers · Toronto Raptors

**Central:** Chicago Bulls · Cleveland Cavaliers · Detroit Pistons · Indiana Pacers · Milwaukee Bucks

**Southeast:** Atlanta Hawks · Charlotte Hornets · Miami Heat · Orlando Magic · Washington Wizards

### Western Conference

**Pacific:** Golden State Warriors · Los Angeles Clippers · Los Angeles Lakers · Phoenix Suns · Sacramento Kings

**Northwest:** Denver Nuggets · Minnesota Timberwolves · Oklahoma City Thunder · Portland Trail Blazers · Utah Jazz

**Southwest:** Dallas Mavericks · Houston Rockets · Memphis Grizzlies · New Orleans Pelicans · San Antonio Spurs

> نکته: نام‌ها و شهرها ممکن است در طول زمان تغییر کنند (مثلاً جابه‌جایی تیم یا تغییر نام). برای پروژه، بهتر است این جدول را در زمان اسکرپ با منبع رسمی (مثل basketball-reference.com یا nba.com) تطبیق دهید.

---

## 5. Team (تیم)

هر تیم شامل: نام تیم، شهر، کنفرانس، دیویژن، ورزشگاه، مربی، بازیکنان، مدیر ارشد ورزشی (GM)

| فیلد | توضیح |
|---|---|
| team_id | شناسه تیم |
| team_name | نام تیم |
| city | شهر |
| abbreviation | مخفف (مثلاً LAL, BOS, GSW) |
| conference | کنفرانس |
| division | دیویژن |
| arena | ورزشگاه |
| founded_year | سال تأسیس |

---

## 6. Arena (ورزشگاه)

هر تیم دارای یک ورزشگاه خانگی است.

اطلاعات: `arena_id` · `arena_name` · `city` · `state` · `capacity`

---

## 7. Season (فصل)

هر سال یک فصل جدید برگزار می‌شود. نمونه: `2023-24` · `2024-25` · `2025-26`

هر فصل شامل: Preseason → Regular Season → Play-In → Playoffs → Finals

---

## 8. Player (بازیکن)

هر تیم حداکثر ۱۵ بازیکن در فهرست فعال (roster) دارد (به‌علاوه دو جایگاه Two-Way Contract).

| فیلد | توضیح |
|---|---|
| player_id | شناسه |
| player_name | نام |
| birth_date | تاریخ تولد |
| height_cm | قد |
| weight_kg | وزن |
| nationality | ملیت |
| position | پست |
| draft_year | سال درفت |
| draft_pick | شماره انتخاب در درفت |
| jersey_number | شماره پیراهن |

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

در دوران مدرن NBA، مرز بین پست‌ها کمرنگ‌تر شده و اصطلاح **Positionless Basketball** رایج شده است.

---

## 10. Coach (مربی)

هر تیم یک سرمربی (Head Coach) و چند مربی دستیار (Assistant Coach) دارد.

اطلاعات: `coach_id` · `coach_name` · `nationality` · `birth_date` · `role` (Head/Assistant)

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
| overtime (بله/خیر و تعداد OT) |

**Home Team:** تیمی که در ورزشگاه خودش بازی می‌کند.
**Away Team:** تیمی که مهمان است.

---

## 12. Regular Season

هر تیم `82 Games` بازی می‌کند (۴۱ خانگی + ۴۱ خارج از خانه). نتیجه هر بازی: Win (W) یا Loss (L)

### Win Percentage

```text
Win % = Wins / Total Games
```
مثال: `64 / 82 = 0.780`

---

## 13. Standings (جدول لیگ)

اطلاعات: Wins · Losses · Win Percentage · Conference Rank · Division Rank · Games Behind · Streak (روند اخیر بردوباخت)

---

## 14. Play-In Tournament

از فصل ۲۰۲۰-۲۱ اضافه شد. تیم‌های رتبه ۷ تا ۱۰ هر کنفرانس برای ورود به دو جایگاه آخر Playoffs رقابت می‌کنند.

## 15. Playoffs

مرحله حذفی لیگ. ۸ تیم برتر هر کنفرانس، به‌صورت Best-of-7 (هر دور تا ۴ برد) رقابت می‌کنند. چهار دور: Round 1 → Conference Semifinals → Conference Finals → NBA Finals

## 16. NBA Finals

فینال NBA بین قهرمان کنفرانس شرق و قهرمان کنفرانس غرب، به‌صورت Best-of-7 برگزار می‌شود.

## 17. Champion

قهرمان نهایی فصل. تیم قهرمان جام **Larry O'Brien Championship Trophy** را دریافت می‌کند.

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
| +/- | Plus/Minus | تفاضل امتیاز تیم هنگام حضور بازیکن در زمین |

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
| eFG% | Effective FG% | `(FGM + 0.5 × 3PM) / FGA` — وزن‌دهی بیشتر به شوت‌های سه امتیازی |

---

## 20. Team Statistics (آمار تیم)

Points · Rebounds · Assists · Steals · Blocks · Turnovers · Fouls · Shooting Percentages · Pace · Point Differential

---

## 21. Advanced Statistics

| شاخص | توضیح |
|---|---|
| Pace | سرعت بازی — تعداد Possession در هر بازی |
| Offensive Rating (ORtg) | امتیاز تولیدشده در هر ۱۰۰ Possession |
| Defensive Rating (DRtg) | امتیاز دریافت‌شده در هر ۱۰۰ Possession |
| Net Rating | `ORtg - DRtg` |
| Usage Rate (USG%) | درصد حملاتی که توسط بازیکن استفاده می‌شود |
| True Shooting % (TS%) | شاخص واقعی بهره‌وری شوت‌زنی (شامل شوت‌های ۲، ۳ امتیازی و پرتاب آزاد) |
| PER (Player Efficiency Rating) | شاخص کلی بهره‌وری بازیکن در هر دقیقه |
| Win Shares (WS) | تخمین تعداد بردهایی که یک بازیکن برای تیمش رقم زده |
| VORP (Value Over Replacement Player) | ارزش بازیکن نسبت به یک بازیکن سطح جایگزین |
| BPM (Box Plus/Minus) | تخمین تأثیر بازیکن بر تفاضل امتیاز تیم در هر ۱۰۰ پوزیشن |

---

## 22. جوایز فصلی NBA

| جایزه | توضیح |
|---|---|
| MVP (Most Valuable Player) | بهترین بازیکن فصل منظم |
| Finals MVP | بهترین بازیکن فینال (جایزه بیل راسل) |
| Defensive Player of the Year (DPOY) | بهترین بازیکن دفاعی |
| Rookie of the Year (ROY) | بهترین بازیکن سال اول |
| Sixth Man of the Year | بهترین بازیکن ذخیره |
| Most Improved Player (MIP) | بیشترین پیشرفت نسبت به فصل قبل |
| Coach of the Year | بهترین سرمربی |
| All-NBA Teams | سه تیم منتخب برتر فصل (First/Second/Third Team) |
| All-Defensive Teams | دو تیم منتخب دفاعی برتر |
| All-Rookie Teams | دو تیم منتخب بهترین بازیکنان سال اول |

---

## 22.5. تروفی‌های معروف NBA

| تروفی | برای چه کسی | توضیح |
|---|---|---|
| **Larry O'Brien Championship Trophy** | تیم قهرمان فصل | معروف‌ترین تروفی NBA؛ هر ساله یک نسخه‌ی جدید ساخته می‌شود (به تیم قهرمان تعلق می‌گیرد، نه امانی) |
| **Bill Russell NBA Finals MVP Award** | بهترین بازیکن فینال | به نام بیل راسل، افسانه‌ی بوستون سلتیکس، نام‌گذاری شده |
| **Michael Jordan Trophy** (تا ۲۰۲۲: Maurice Podoloff Trophy) | MVP فصل منظم | در سال ۲۰۲۲ به افتخار مایکل جردن تغییر نام داد |
| **Hakeem Olajuwon Trophy** (تا ۲۰۲۲: بدون نام خاص) | بهترین بازیکن دفاعی سال (DPOY) | به نام حکیم اولاجوان، مرکز افسانه‌ای هیوستون راکتس |
| **Naismith Memorial Basketball Hall of Fame** | بزرگان تاریخ بسکتبال | تالار مشاهیر بسکتبال؛ به نام جیمز نایسمیت، مخترع بسکتبال |
| **Red Auerbach Trophy** | بهترین سرمربی سال | به نام رد آئرباخ، مربی افسانه‌ای بوستون سلتیکس |
| **J. Walter Kennedy Citizenship Award** | خدمات اجتماعی و انسان‌دوستانه | برای بازیکنی که بیشترین تأثیر مثبت اجتماعی را داشته |

> اگه اسم تروفی مدنظرت یکی از این‌ها نبود، احتمالاً بگو چه ویژگی‌ای ازش یادته (مثلاً «مال بهترین دفاعی بود» یا «هرسال یه دونه جدید می‌سازن») تا دقیق‌تر پیداش کنیم.

---

## 22.6. Four Factors — چهار فاکتور طلایی تحلیل بسکتبال

این مفهوم را **دین الیور (Dean Oliver)**، پدر آمار پیشرفته بسکتبال، معرفی کرد. طبق تحقیق او، نتیجه‌ی هر بازی بسکتبال عمدتاً به این چهار فاکتور بستگی دارد — و تقریباً در هر تحلیل NBA (چه حرفه‌ای چه پروژه‌های دانشجویی) این چهار مورد محاسبه می‌شوند:

| فاکتور | فرمول | اهمیت (وزن تقریبی) | توضیح |
|---|---|---|---|
| **1. Shooting (eFG%)** | `(FGM + 0.5 × 3PM) / FGA` | ۴۰٪ | مهم‌ترین فاکتور؛ کارایی شوت‌زنی با احتساب ارزش بیشتر شوت سه‌امتیازی |
| **2. Turnovers (TOV%)** | `TOV / (FGA + 0.44×FTA + TOV)` | ۲۵٪ | درصد پوزیشن‌هایی که به از دست دادن توپ ختم می‌شوند؛ هرچه کمتر بهتر |
| **3. Rebounding (ORB%)** | `ORB / (ORB + Opponent DRB)` | ۲۰٪ | درصد ریباندهای حمله گرفته‌شده از کل ریباندهای در دسترس |
| **4. Free Throws (FT Rate)** | `FTA / FGA` | ۱۵٪ | توانایی رفتن به خط پرتاب آزاد نسبت به تعداد شوت‌ها |

**کاربرد عملی:** این چهار فاکتور را می‌توان هم برای **تیم** (offensive four factors) و هم برای **حریف** (defensive four factors) محاسبه کرد. تیمی که در این چهار فاکتور نسبت به حریف برتری داشته باشد، معمولاً برنده‌ی بازی است — این مبنای بسیاری از مدل‌های پیش‌بینی نتیجه در تحلیل داده NBA است.

---

## 23. Draft (درفت)

- هر ساله در ژوئن برگزار می‌شود؛ تیم‌ها بازیکنان جوان (عمدتاً از دانشگاه یا لیگ‌های بین‌المللی) را انتخاب می‌کنند
- دو دور دارد، هر دور ۳۰ انتخاب (Pick)
- **Draft Lottery:** ترتیب انتخاب ۱۴ تیمی که به Playoffs نرسیدند، با قرعه‌کشی وزن‌دار مشخص می‌شود (تیم‌های ضعیف‌تر شانس بیشتری برای پیک‌های اول دارند)

---

## 24. قراردادها و مسائل مالی

| مفهوم | توضیح |
|---|---|
| Salary Cap | سقف حقوقی پیشنهادی برای هر تیم در هر فصل |
| Luxury Tax | مالیاتی که تیم‌های با حقوق بالاتر از سقف مشخص باید بپردازند |
| Free Agency | دوره‌ای که بازیکنان بدون قرارداد می‌توانند با هر تیمی مذاکره کنند |
| Trade Deadline | آخرین مهلت مبادله بازیکن بین تیم‌ها در طول فصل (معمولاً اوایل فوریه) |
| Two-Way Contract | قرارداد ویژه بازیکنانی که بین تیم اصلی و لیگ توسعه (G League) در رفت‌وآمدند |

---

## 25. تقویم فصل

```text
اکتبر    → آغاز فصل منظم (Regular Season)
اکتبر–نوامبر → NBA Cup (تورنومنت داخل‌فصلی، از ۲۰۲۳ اضافه شد)
فوریه    → All-Star Weekend + Trade Deadline
آوریل    → پایان فصل منظم
آوریل    → Play-In Tournament
آوریل–می  → Playoffs
ژوئن     → NBA Finals + Draft
جولای    → آغاز Free Agency
```

---

## 26. اصطلاحات رایج NBA

| اصطلاح | توضیح |
|---|---|
| Double Double | حداقل ۱۰ واحد در دو شاخص آماری (مثلاً ۲۰ امتیاز + ۱۲ ریباند) |
| Triple Double | حداقل ۱۰ واحد در سه شاخص (مثلاً ۲۰ امتیاز + ۱۰ ریباند + ۱۱ پاس گل) |
| Quadruple Double | حداقل ۱۰ واحد در چهار شاخص |
| Sixth Man | بهترین بازیکن ذخیره |
| Clutch Time | دقایق حساس پایانی بازی (معمولاً ۵ دقیقه آخر با اختلاف امتیاز کم) |
| Back-to-Back (B2B) | دو بازی در دو روز متوالی |
| Buzzer Beater | شوتی که همزمان با پایان زمان بازی وارد سبد می‌شود |
| Tanking | استراتژی باختن عمدی بازی‌ها برای گرفتن پیک بهتر در درفت |
| Load Management | استراحت‌دادن برنامه‌ریزی‌شده به بازیکنان برای جلوگیری از آسیب‌دیدگی |

---

## 27. سؤالات تحلیلی مناسب برای پروژه

- بهترین بازیکن هر فصل؟
- بهترین تیم هجومی؟ بهترین تیم دفاعی؟
- آیا بازی خانگی باعث افزایش شانس برد می‌شود؟
- آیا قد بازیکن با ریباند رابطه دارد؟
- آیا Turnover باعث باخت می‌شود؟
- آیا سن با عملکرد بازیکن رابطه دارد؟
- آیا Usage Rate با امتیاز رابطه دارد؟
- آیا برندگان MVP بیشتر از تیم‌های برتر جدول می‌آیند؟
- رابطه بین Win Shares و شانس رسیدن به Playoffs چیست؟
- پیش‌بینی صعود به Playoffs
- پیش‌بینی برنده بازی

---

## 28. داده‌هایی که باید اسکرپ شوند

Teams · Players · Seasons · Games · Player Game Statistics · Team Game Statistics · Standings · Player Team History · Coaches · Arenas · Awards (MVP, DPOY, ROY, ...) · Draft History

---

## 29. نقشه راه پروژه

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

---

## منابع پیشنهادی برای عمیق‌تر شدن

- [Basketball-Reference.com](https://www.basketball-reference.com) — کامل‌ترین منبع آماری تاریخی NBA
- [NBA.com/stats](https://www.nba.com/stats) — آمار رسمی لیگ
- [NBA.com](https://www.nba.com) — اخبار و اطلاعات رسمی تیم‌ها
