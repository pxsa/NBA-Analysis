-- 1: TOTAL PLAYERS
SELECT
  COUNT(*) AS total_players
FROM
  player


--  2: TOTAL TEAMS
SELECT
	COUNT(*) AS total_teams
FROM team;


-- 3: TOTAL SEASONS
SELECT
  COUNT(*) AS total_season
FROM
  season;


-- 4: Top 10 countries with most players
SELECT
  country_code,
  COUNT(*) AS total_players
FROM
  country c
  JOIN player p ON p.country_id = c.country_id
GROUP BY
  country_code
ORDER BY
  total_players DESC
LIMIT
  10;


-- 5: PLAYER BY POSITION
SELECT
  position_code,
  count(p.player_id) AS total_player
FROM
  player p
  JOIN playerposition pp ON pp.player_id = p.player_id
  JOIN positioni po ON po.position_id = pp.position_id
GROUP BY
  position_code
ORDER BY
  total_player DESC;


-- 6: Top 10 Players by Career Win Shares
SELECT
  p.full_name,
  round(sum(s.win_shares), 2) AS career_win_shares
FROM
  player p
  JOIN playerseasonstats s ON p.player_id = s.player_id
GROUP BY
  p.full_name
HAVING
  career_win_shares IS NOT NULL
ORDER BY
  career_win_shares DESC
LIMIT
  10;


-- 7: Number of players with different positions
WITH player_positions AS (
  SELECT
    player_id,
    COUNT(*) AS total_position
  FROM playerposition
  GROUP BY player_id
  HAVING COUNT(*) > 1
)
SELECT
  total_position,
  COUNT(*) AS player_count
FROM player_positions
GROUP BY total_position
ORDER BY total_position DESC;


-- 8: Players with same name
SELECT
  full_name,
  count(*) AS player_with_same_name
FROM
  player
GROUP BY
  full_name
HAVING
  player_with_same_name > 1


  -- 9: Top 10 Players by Career VORP
SELECT
  full_name,
  round(sum(vorp), 2) AS sum_vorp
FROM
  player p
  JOIN playerseasonstats s ON p.player_id = s.player_id
GROUP BY
  full_name
ORDER BY
  sum_vorp DESC
LIMIT
  10;


-- 10: Top 10 Players by Career BPM

SELECT
  p.full_name,
  ROUND(AVG(s.bpm), 2) AS avg_bpm
FROM
  playerseasonstats s
  JOIN player p ON p.player_id = s.player_id
GROUP BY
  p.full_name
ORDER BY
  avg_bpm DESC
LIMIT
  10


-- 11: Which colleges have produced the most NBA players?
SELECT
  c.college_name,
  COUNT(DISTINCT pc.player_id) AS total_players
FROM
  playercollege pc
  JOIN college c ON c.college_id = pc.college_id
GROUP BY
  c.college_name
ORDER BY
  total_players DESC
LIMIT
  10;


-- 12: Average age of players over time
SELECT
    s.season_name,
    ROUND(AVG(ps.age),2) AS average_age
FROM playerseasonstats ps
JOIN season s
ON ps.season_id = s.season_id
GROUP BY s.season_name
ORDER BY s.season_name;


-- 13: Which teams rely on younger players?
SELECT
    t.team_code,
    ROUND(AVG(ps.age),1) AS average_age
FROM playerseasonstats ps
JOIN team t
ON ps.team_code=t.team_code
GROUP BY t.team_code
ORDER BY average_age;


-- 14: Which countries produce the most MVP winners?
SELECT
  c.country_code,
  COUNT(DISTINCT m.player_id) AS mvp_players
FROM
  mvp_award m
  JOIN player p ON m.player_id = p.player_id
  JOIN country c ON p.country_id = c.country_id

GROUP BY
  c.country_code
ORDER BY
  mvp_players DESC;


-- 15: Which colleges produce championship players?
SELECT
    c.college_name,
    COUNT(DISTINCT cp.player_id) AS champions
FROM championteamplayer cp
JOIN playercollege pc ON cp.player_id = pc.player_id
JOIN college c ON pc.college_id = c.college_id
GROUP BY c.college_name
ORDER BY champions DESC;


-- 16: Number of players by cluster
SELECT
  CASE cluster
    WHEN 0 THEN 'Professional'
    WHEN 1 THEN 'Casual'
    WHEN 2 THEN 'Veteran'
    WHEN 3 THEN 'Hardcore'
    ELSE 'Unknown'
  END AS cluster_name,
  COUNT(*) AS number_of_players,
  ROUND(COUNT(*) * 100 / (SELECT COUNT(*) FROM playerseasonstats), 2) AS percentage
FROM
  playerseasonstats
GROUP BY
  cluster
ORDER BY
  number_of_players DESC


-- 17: Average Win Shares by cluster
SELECT
  CASE cluster
    WHEN 0 THEN 'Professional'
    WHEN 1 THEN 'Casual'
    WHEN 2 THEN 'Veteran'
    WHEN 3 THEN 'Hardcore'
  END AS cluster_name,
  round(avg(s.win_shares), 2) AS avg_win_shares
FROM
  playerseasonstats s
GROUP BY
  cluster_name


-- 18: Average age by cluster
SELECT
  CASE cluster
    WHEN 0 THEN 'Professional'
    WHEN 1 THEN 'Casual'
    WHEN 2 THEN 'Veteran'
    WHEN 3 THEN 'Hardcore'
  END AS cluster_name,
  round(avg(age), 2) AS avg_age
FROM
  playerseasonstats
GROUP BY
  cluster_name


-- 19: Average minutes by cluster
SELECT
  CASE cluster
    WHEN 0 THEN 'Professional'
    WHEN 1 THEN 'Casual'
    WHEN 2 THEN 'Veteran'
    WHEN 3 THEN 'Hardcore'
  END AS cluster_name,
  round(avg(minutes)) AS avg_age
FROM
  playerseasonstats
GROUP BY
  cluster_name


-- 20: Average statistics by cluster
SELECT
    CASE cluster
	WHEN 0 THEN 'Professional'
	WHEN 1 THEN 'Casual'
	WHEN 2 THEN 'Veteran'
	WHEN 3 THEN 'Hardcore'
	END as cluster,
    ROUND(AVG(minutes),0) AS avg_minutes,
    ROUND(AVG(win_shares),2) AS avg_ws,
    ROUND(AVG(ws_per_48),3) AS avg_ws48,
    ROUND(AVG(vorp),2) AS avg_vorp,
    ROUND(AVG(age),1) AS avg_age,
    ROUND(AVG(bpm),1) AS avg_experience,
    ROUND(AVG(games),1) AS avg_games
FROM playerseasonstats
GROUP BY cluster;