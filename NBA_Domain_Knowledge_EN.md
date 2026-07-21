# NBA Domain Knowledge Documentation

Comprehensive domain knowledge documentation for the NBA data analysis project — the foundation for web scraping, database design, and data analysis.

---

## Table of Contents

1. [What is the NBA?](#1-what-is-the-nba)
2. [Overall Structure](#2-overall-structure)
3. [Conferences and Divisions](#3-conferences-and-divisions)
4. [Full List of 30 Teams](#4-full-list-of-30-teams)
5. [Team](#5-team)
6. [Arena](#6-arena)
7. [Season](#7-season)
8. [Player](#8-player)
9. [Position](#9-position)
10. [Coach](#10-coach)
11. [Game](#11-game)
12. [Regular Season](#12-regular-season)
13. [Standings](#13-standings)
14. [Play-In, Playoffs, Finals](#14-play-in-tournament)
15. [Player Statistics](#18-player-statistics)
16. [Shooting Statistics](#19-shooting-statistics)
17. [Team Statistics](#20-team-statistics)
18. [Advanced Statistics](#21-advanced-statistics)
19. [Famous NBA Trophies](#215-famous-nba-trophies)
20. [Four Factors](#216-four-factors)
21. [Season Awards](#22-season-awards)
22. [Draft](#23-draft)
23. [Contracts and Financial Rules](#24-contracts-and-financial-rules)
24. [Season Calendar](#25-season-calendar)
25. [Common NBA Terms](#26-common-nba-terms)
26. [Analytical Questions Suitable for the Project](#27-analytical-questions-suitable-for-the-project)
27. [Data to Be Scraped](#28-data-to-be-scraped)
28. [Project Roadmap](#29-project-roadmap)

---

## 1. What is the NBA?

The NBA (National Basketball Association) is the largest and most prestigious professional basketball league in the world.

- Founded: 1946 (originally as the BAA; merged with the NBL in 1949 to form the NBA)
- Consists of 30 teams (29 U.S. teams + 1 Canadian team: Toronto Raptors)
- Each team plays an **82-game** regular season
- The season runs from October through June of the following year (including the Finals)
- Current Commissioner: Adam Silver

---

## 2. Overall Structure

```text
NBA
├── Eastern Conference (15 teams)
│      ├── Atlantic Division
│      ├── Central Division
│      └── Southeast Division
└── Western Conference (15 teams)
       ├── Pacific Division
       ├── Northwest Division
       └── Southwest Division
```

Each division has 5 teams.

---

## 3. Conferences and Divisions

| Conference | Division | Number of Teams |
|---|---|---|
| Eastern | Atlantic | 5 |
| Eastern | Central | 5 |
| Eastern | Southeast | 5 |
| Western | Pacific | 5 |
| Western | Northwest | 5 |
| Western | Southwest | 5 |

---

## 4. Full List of 30 Teams

### Eastern Conference

**Atlantic:** Boston Celtics · Brooklyn Nets · New York Knicks · Philadelphia 76ers · Toronto Raptors

**Central:** Chicago Bulls · Cleveland Cavaliers · Detroit Pistons · Indiana Pacers · Milwaukee Bucks

**Southeast:** Atlanta Hawks · Charlotte Hornets · Miami Heat · Orlando Magic · Washington Wizards

### Western Conference

**Pacific:** Golden State Warriors · Los Angeles Clippers · Los Angeles Lakers · Phoenix Suns · Sacramento Kings

**Northwest:** Denver Nuggets · Minnesota Timberwolves · Oklahoma City Thunder · Portland Trail Blazers · Utah Jazz

**Southwest:** Dallas Mavericks · Houston Rockets · Memphis Grizzlies · New Orleans Pelicans · San Antonio Spurs

> Note: Team names and cities can change over time (relocation, rebranding). When scraping, verify this table against an official source (e.g., basketball-reference.com or nba.com).

---

## 5. Team

Each team includes: name, city, conference, division, arena, coaching staff, roster, general manager (GM).

| Field | Description |
|---|---|
| team_id | Team identifier |
| team_name | Team name |
| city | City |
| abbreviation | Abbreviation (e.g., LAL, BOS, GSW) |
| conference | Conference |
| division | Division |
| arena | Home arena |
| founded_year | Year founded |

---

## 6. Arena

Each team has one home arena.

Fields: `arena_id` · `arena_name` · `city` · `state` · `capacity`

---

## 7. Season

A new season is played every year. Example: `2023-24` · `2024-25` · `2025-26`

Each season consists of: Preseason → Regular Season → Play-In → Playoffs → Finals

---

## 8. Player

Each team carries up to 15 active roster players (plus two Two-Way Contract slots).

| Field | Description |
|---|---|
| player_id | Identifier |
| player_name | Name |
| birth_date | Date of birth |
| height_cm | Height |
| weight_kg | Weight |
| nationality | Nationality |
| position | Position |
| draft_year | Draft year |
| draft_pick | Draft pick number |
| jersey_number | Jersey number |

---

## 9. Position

5 main positions:

| Abbr. | Name | Description |
|---|---|---|
| PG | Point Guard | Primary ball-handler and playmaker |
| SG | Shooting Guard | Primary scorer, shooter |
| SF | Small Forward | Hybrid of offense and defense |
| PF | Power Forward | Physical player, rebounder |
| C | Center | Tallest player, defense and rebounding |

In modern NBA, the line between positions has blurred — a trend often called **positionless basketball**.

---

## 10. Coach

Each team has one Head Coach and several Assistant Coaches.

Fields: `coach_id` · `coach_name` · `nationality` · `birth_date` · `role` (Head/Assistant)

---

## 11. Game

Each game involves two teams, a date, and a result.

| Field |
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
| overtime (yes/no and number of OT periods) |

**Home Team:** the team playing at its own arena.
**Away Team:** the visiting team.

---

## 12. Regular Season

Each team plays `82 Games` (41 home + 41 away). Result of each game: Win (W) or Loss (L).

### Win Percentage

```text
Win % = Wins / Total Games
```
Example: `64 / 82 = 0.780`

---

## 13. Standings

Fields: Wins · Losses · Win Percentage · Conference Rank · Division Rank · Games Behind · Streak (recent win/loss trend)

---

## 14. Play-In Tournament

Introduced in the 2020-21 season. Teams seeded 7th through 10th in each conference compete for the final two playoff spots.

## 15. Playoffs

The league's elimination stage. The top 8 teams in each conference compete in a best-of-seven format (first to 4 wins). Four rounds: Round 1 → Conference Semifinals → Conference Finals → NBA Finals.

## 16. NBA Finals

The championship series between the Eastern and Western Conference champions, played best-of-seven.

## 17. Champion

The season's final champion. The winning team receives the **Larry O'Brien Championship Trophy**.

---

## 18. Player Statistics

Recorded for each player after every game.

| Abbr. | Name | Description |
|---|---|---|
| MIN | Minutes Played | Time played |
| PTS | Points | Points scored |
| REB | Rebounds | Total rebounds |
| OREB | Offensive Rebound | Rebounds on offense |
| DREB | Defensive Rebound | Rebounds on defense |
| AST | Assists | Passes leading to a score |
| STL | Steals | Ball steals |
| BLK | Blocks | Shot blocks |
| TOV | Turnovers | Loss of possession |
| PF | Personal Fouls | Fouls committed |
| +/- | Plus/Minus | Team's point differential while the player is on court |

---

## 19. Shooting Statistics

| Abbr. | Name | Formula |
|---|---|---|
| FGA | Field Goal Attempts | Total shots taken |
| FGM | Field Goals Made | Successful shots |
| FG% | Field Goal % | `FGM / FGA` |
| 3PA | Three Point Attempts | Total three-point shots taken |
| 3PM | Three Point Made | Successful three-pointers |
| 3P% | Three Point % | `3PM / 3PA` |
| FTA | Free Throw Attempts | Total free throws taken |
| FTM | Free Throw Made | Successful free throws |
| FT% | Free Throw % | `FTM / FTA` |
| eFG% | Effective FG% | `(FGM + 0.5 × 3PM) / FGA` — weights three-pointers more heavily |

---

## 20. Team Statistics

Points · Rebounds · Assists · Steals · Blocks · Turnovers · Fouls · Shooting Percentages · Pace · Point Differential

---

## 21. Advanced Statistics

| Metric | Description |
|---|---|
| Pace | Game speed — number of possessions per game |
| Offensive Rating (ORtg) | Points produced per 100 possessions |
| Defensive Rating (DRtg) | Points allowed per 100 possessions |
| Net Rating | `ORtg - DRtg` |
| Usage Rate (USG%) | Percentage of team plays used by a player while on court |
| True Shooting % (TS%) | Overall shooting efficiency, accounting for 2-pointers, 3-pointers, and free throws |
| PER (Player Efficiency Rating) | Overall per-minute production rating |
| Win Shares (WS) | Estimate of the number of wins a player contributed to their team |
| VORP (Value Over Replacement Player) | A player's value compared to a replacement-level player |
| BPM (Box Plus/Minus) | Estimated impact on team point differential per 100 possessions |

---

## 21.5. Famous NBA Trophies

| Trophy | Awarded To | Description |
|---|---|---|
| **Larry O'Brien Championship Trophy** | Championship team | The league's most famous trophy; a new one is made each year and belongs to the champion (not a traveling trophy) |
| **Bill Russell NBA Finals MVP Award** | Best player of the Finals | Named after Boston Celtics legend Bill Russell |
| **Michael Jordan Trophy** (formerly Maurice Podoloff Trophy until 2022) | Regular-season MVP | Renamed in 2022 in honor of Michael Jordan |
| **Hakeem Olajuwon Trophy** (unnamed before 2022) | Defensive Player of the Year (DPOY) | Named after Houston Rockets legend Hakeem Olajuwon |
| **Naismith Memorial Basketball Hall of Fame** | Basketball legends | The sport's hall of fame, named after James Naismith, the inventor of basketball |
| **Red Auerbach Trophy** | Coach of the Year | Named after legendary Boston Celtics coach Red Auerbach |
| **J. Walter Kennedy Citizenship Award** | Community service and philanthropy | Given to the player with the greatest positive social impact |

---

## 21.6. Four Factors

Introduced by **Dean Oliver**, the father of advanced basketball analytics. His research found that the outcome of a basketball game largely depends on these four factors — and they're calculated in nearly every serious NBA analysis, professional or academic:

| Factor | Formula | Approximate Weight | Description |
|---|---|---|---|
| **1. Shooting (eFG%)** | `(FGM + 0.5 × 3PM) / FGA` | 40% | The most important factor; shooting efficiency, weighted for the extra value of threes |
| **2. Turnovers (TOV%)** | `TOV / (FGA + 0.44×FTA + TOV)` | 25% | Percentage of possessions ending in a turnover; lower is better |
| **3. Rebounding (ORB%)** | `ORB / (ORB + Opponent DRB)` | 20% | Percentage of available offensive rebounds secured |
| **4. Free Throws (FT Rate)** | `FTA / FGA` | 15% | Ability to get to the free-throw line relative to shots taken |

**Practical use:** These four factors can be calculated both for a team (offensive four factors) and against its opponent (defensive four factors). A team that outperforms its opponent across these four factors usually wins the game — this is the foundation of many game-outcome prediction models in NBA analytics.

---

## 22. Season Awards

| Award | Description |
|---|---|
| MVP (Most Valuable Player) | Best player of the regular season |
| Finals MVP | Best player of the Finals (Bill Russell Award) |
| Defensive Player of the Year (DPOY) | Best defensive player |
| Rookie of the Year (ROY) | Best first-year player |
| Sixth Man of the Year | Best bench player |
| Most Improved Player (MIP) | Greatest improvement compared to the previous season |
| Coach of the Year | Best head coach |
| All-NBA Teams | Three top teams selected each season (First/Second/Third Team) |
| All-Defensive Teams | Two top defensive teams |
| All-Rookie Teams | Two top teams of first-year players |

---

## 23. Draft

- Held every year in June; teams select young players (mostly from college or international leagues)
- Two rounds, 30 picks per round
- **Draft Lottery:** determines the pick order for the 14 teams that missed the playoffs, via a weighted lottery (weaker teams have better odds at top picks)

---

## 24. Contracts and Financial Rules

| Concept | Description |
|---|---|
| Salary Cap | The suggested salary ceiling for each team per season |
| Luxury Tax | A tax paid by teams whose payroll exceeds a set threshold |
| Free Agency | The period when players without a contract can negotiate with any team |
| Trade Deadline | The final date for trading players during the season (usually early February) |
| Two-Way Contract | A special contract for players who split time between the NBA roster and the G League |

---

## 25. Season Calendar

```text
October        → Regular Season begins
October–November → NBA Cup (in-season tournament, introduced in 2023)
February       → All-Star Weekend + Trade Deadline
April          → Regular Season ends
April          → Play-In Tournament
April–May      → Playoffs
June           → NBA Finals + Draft
July           → Free Agency begins
```

---

## 26. Common NBA Terms

| Term | Description |
|---|---|
| Double Double | At least 10 in two statistical categories (e.g., 20 points + 12 rebounds) |
| Triple Double | At least 10 in three categories (e.g., 20 points + 10 rebounds + 11 assists) |
| Quadruple Double | At least 10 in four categories |
| Sixth Man | The best bench player |
| Clutch Time | Critical closing minutes of a game (typically the final 5 minutes with a close score) |
| Back-to-Back (B2B) | Two games played on two consecutive days |
| Buzzer Beater | A shot that goes in right as the game clock expires |
| Tanking | Intentionally losing games to secure a better draft pick |
| Load Management | Planned rest for players to prevent injury |

---

## 27. Analytical Questions Suitable for the Project

- Who is the best player each season?
- Which team has the best offense? The best defense?
- Does home-court advantage increase win probability?
- Is there a relationship between player height and rebounding?
- Do turnovers correlate with losses?
- Is there a relationship between age and player performance?
- Is there a relationship between Usage Rate and scoring?
- Do MVP winners tend to come from top-ranked teams?
- What's the relationship between Win Shares and playoff qualification?
- Predicting playoff qualification
- Predicting game winners

---

## 28. Data to Be Scraped

Teams · Players · Seasons · Games · Player Game Statistics · Team Game Statistics · Standings · Player Team History · Coaches · Arenas · Awards (MVP, DPOY, ROY, ...) · Draft History

---

## 29. Project Roadmap

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

## Suggested Resources for Going Deeper

- [Basketball-Reference.com](https://www.basketball-reference.com) — the most comprehensive historical NBA stats source
- [NBA.com/stats](https://www.nba.com/stats) — official league statistics
- [NBA.com](https://www.nba.com) — official news and team information
