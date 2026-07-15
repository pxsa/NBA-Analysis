-- ==========================================================
-- Basketball Database Schema
-- Author: Your Name
-- Description:
-- Relational database schema for storing NBA player profiles,
-- season statistics, MVP voting, and championship rosters.
-- ==========================================================

CREATE DATABASE IF NOT EXISTS basketball_db;
USE basketball_db;

-- ==========================================================
-- Country
-- Stores all unique player nationalities.
-- ==========================================================

CREATE TABLE country (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_code VARCHAR(10) NOT NULL UNIQUE
);

-- ==========================================================
-- College
-- Stores all unique colleges.
-- ==========================================================

CREATE TABLE college (
    college_id INT AUTO_INCREMENT PRIMARY KEY,
    college_name VARCHAR(255) NOT NULL UNIQUE
);

-- ==========================================================
-- Position
-- Stores standardized basketball positions.
-- ==========================================================

CREATE TABLE position (
    position_id INT AUTO_INCREMENT PRIMARY KEY,
    position_code VARCHAR(5) NOT NULL UNIQUE
);

-- ==========================================================
-- Season
-- Stores NBA seasons.
-- ==========================================================

CREATE TABLE season (
    season_id INT AUTO_INCREMENT PRIMARY KEY,
    season_name VARCHAR(20) NOT NULL UNIQUE
);

-- ==========================================================
-- Team
-- Stores NBA teams.
-- team_name is nullable because the raw dataset only provides
-- team abbreviations.
-- ==========================================================

CREATE TABLE team (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_code VARCHAR(5) NOT NULL UNIQUE,
    team_name VARCHAR(100)
);

-- ==========================================================
-- Player
-- Stores player profile information.
-- ==========================================================

CREATE TABLE player (
    player_id VARCHAR(20) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    birth_place VARCHAR(255),
    height_cm INT,
    weight_kg FLOAT,

    shoots ENUM('Right','Left','Both'),

    player_url VARCHAR(255),

    country_id INT,

    CONSTRAINT fk_player_country
        FOREIGN KEY (country_id)
        REFERENCES country(country_id)
);

-- ==========================================================
-- Player <-> College (Many-to-Many)
-- ==========================================================

CREATE TABLE player_college (
    player_id VARCHAR(20),
    college_id INT,

    PRIMARY KEY (player_id, college_id),

    CONSTRAINT fk_pc_player
        FOREIGN KEY (player_id)
        REFERENCES player(player_id),

    CONSTRAINT fk_pc_college
        FOREIGN KEY (college_id)
        REFERENCES college(college_id)
);

-- ==========================================================
-- Player <-> Position (Many-to-Many)
-- ==========================================================

CREATE TABLE player_position (
    player_id VARCHAR(20),
    position_id INT,

    PRIMARY KEY (player_id, position_id),

    CONSTRAINT fk_pp_player
        FOREIGN KEY (player_id)
        REFERENCES player(player_id),

    CONSTRAINT fk_pp_position
        FOREIGN KEY (position_id)
        REFERENCES position(position_id)
);

-- ==========================================================
-- Player Season Statistics
-- One record per player per season.
-- Composite primary key:
-- (player_id, season_id)
-- ==========================================================

CREATE TABLE player_season_stats (

    player_id VARCHAR(20),
    season_id INT,

    team_code VARCHAR(5),

    age INT,
    position_code VARCHAR(5),

    games INT,
    games_started INT,
    minutes INT,

    win_shares FLOAT,
    ws_per_48 FLOAT,
    bpm FLOAT,
    vorp FLOAT,

    PRIMARY KEY (player_id, season_id),

    CONSTRAINT fk_ps_player
        FOREIGN KEY (player_id)
        REFERENCES player(player_id),

    CONSTRAINT fk_ps_season
        FOREIGN KEY (season_id)
        REFERENCES season(season_id),

    CONSTRAINT fk_ps_team
        FOREIGN KEY (team_code)
        REFERENCES team(team_code)
);

-- ==========================================================
-- MVP Awards
-- Stores MVP voting results.
-- MVP belongs to a player in a specific season,
-- therefore team information is intentionally omitted.
-- ==========================================================

CREATE TABLE mvp_award (

    player_id VARCHAR(20),
    season_id INT,

    mvp_rank INT,
    mvp_share DECIMAL(5,3),

    PRIMARY KEY (player_id, season_id),

    CONSTRAINT fk_mvp_player
        FOREIGN KEY (player_id)
        REFERENCES player(player_id),

    CONSTRAINT fk_mvp_season
        FOREIGN KEY (season_id)
        REFERENCES season(season_id)
);

-- ==========================================================
-- Championship Team Players
-- Stores players who were members of the NBA championship
-- roster in each season.
-- ==========================================================

CREATE TABLE champion_team_player (

    player_id VARCHAR(20),
    season_id INT,

    team_code VARCHAR(5),

    jersey_number INT,

    age INT,
    experience VARCHAR(10),

    games INT,
    minutes INT,
    win_shares FLOAT,

    PRIMARY KEY (player_id, season_id),

    CONSTRAINT fk_ctp_player
        FOREIGN KEY (player_id)
        REFERENCES player(player_id),

    CONSTRAINT fk_ctp_season
        FOREIGN KEY (season_id)
        REFERENCES season(season_id),

    CONSTRAINT fk_ctp_team
        FOREIGN KEY (team_code)
        REFERENCES team(team_code)
);