import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import socket


# LOAD ENV VARIABLES FROM ACTUAL MYSQL
load_dotenv('../.env')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('PASSWORD')
HOST = 'localhost'
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')

print("Source MySQL (from ../.env):")
print(f"Username: {USERNAME}")
print(f"Password: {'*' * len(PASSWORD) if PASSWORD else 'None'}")
print(f"Host: {HOST}")
print(f"Port: {PORT}")
print(f"Database: {DATABASE}\n")


# LOAD ENV VARIABLES FROM DOCKER MYSQL
load_dotenv('.env-docker', override=True)
DOCKER_USERNAME = os.getenv('DB_USERNAME')
DOCKER_PASSWORD = os.getenv('PASSWORD')
DOCKER_HOST = os.getenv('HOST')
DOCKER_PORT = os.getenv('PORT')
DOCKER_DATABASE = os.getenv('DATABASE')

print("Destination Docker MySQL (from .env-docker):")
print(f"Username: {DOCKER_USERNAME}")
print(f"Password: {'*' * len(DOCKER_PASSWORD) if DOCKER_PASSWORD else 'None'}")
print(f"Host: {DOCKER_HOST}")
print(f"Port: {DOCKER_PORT}")
print(f"Database: {DOCKER_DATABASE}\n")

# CREATE DATABASE ENGINE
try:
    # Engine for source MySQL
    engine = create_engine(
        f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    )
    # Test source connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Source MySQL connection successful!")
except Exception as e:
    print(f"Failed to connect to source MySQL: {e}")
    exit(1)


try:
    # Engine for Docker MySQL
    docker_engine = create_engine(
        f"mysql+pymysql://{DOCKER_USERNAME}:{DOCKER_PASSWORD}@{DOCKER_HOST}:{DOCKER_PORT}/{DOCKER_DATABASE}",
        pool_pre_ping=True
    )
    # Test Docker connection
    with docker_engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Docker MySQL connection successful!\n")
except Exception as e:
    print(f"Failed to connect to Docker MySQL: {e}")
    print("3. Try connecting directly: mysql -h {DOCKER_HOST} -P {DOCKER_PORT} -u {DOCKER_USERNAME} -p")
    exit(1)

# READ DATA FROM ACTUAL MYSQL AND THEN CRAETE DATAFRAME
champion_team_player_df = pd.read_sql('SELECT * FROM championteamplayer', engine)
college_df              = pd.read_sql('SELECT * FROM college', engine)
country_df              = pd.read_sql('SELECT * FROM country', engine)
mvp_award_df            = pd.read_sql('SELECT * FROM mvp_award', engine)
player_df               = pd.read_sql('SELECT * FROM player', engine)
player_college_df       = pd.read_sql('SELECT * FROM playercollege', engine)
player_position_df      = pd.read_sql('SELECT * FROM playerposition', engine)
player_season_stats_df  = pd.read_sql('SELECT * FROM playerseasonstats', engine)
position_df             = pd.read_sql('SELECT * FROM position', engine)
season_df               = pd.read_sql('SELECT * FROM season', engine)
team_df                 = pd.read_sql('SELECT * FROM team', engine)

# LOAD DATA TO DOCKER MYSQL
country_df.to_sql(name="country", con=docker_engine, if_exists="append", index=False)
college_df.to_sql(name="college", con=docker_engine, if_exists="append", index=False)
position_df.to_sql(name="position", con=docker_engine, if_exists="append", index=False)
season_df.to_sql(name="season", con=docker_engine, if_exists="append", index=False)
team_df.to_sql(name="team", con=docker_engine, if_exists="append", index=False)
player_df.to_sql(name="player", con=docker_engine, if_exists="append", index=False)
player_college_df.to_sql(name="playercollege", con=docker_engine, if_exists="append", index=False)
player_position_df.to_sql(name="playerposition", con=docker_engine, if_exists="append", index=False)
player_season_stats_df.to_sql(name="playerseasonstats", con=docker_engine, if_exists="append", index=False)
mvp_award_df.to_sql(name="mvp_award", con=docker_engine, if_exists="append", index=False)
champion_team_player_df.to_sql(name="championteamplayer", con=docker_engine, if_exists="append", index=False)