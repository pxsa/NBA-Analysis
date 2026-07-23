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