#!/usr/bin/env python
# coding: utf-8

# # Read data from database
# 

# In[1]:


import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# In[2]:


load_dotenv('../.env')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')


# In[3]:


engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

champion_team_player_df = pd.read_sql('SELECT * FROM championteamplayer', engine)
college_df              = pd.read_sql('SELECT * FROM college', engine)
country_df              = pd.read_sql('SELECT * FROM country', engine)
mvp_award_df            = pd.read_sql('SELECT * FROM mvp_award', engine)
player_df               = pd.read_sql('SELECT * FROM player', engine)
player_college_df       = pd.read_sql('SELECT * FROM playercollege', engine)
player_position_df      = pd.read_sql('SELECT * FROM playerposition', engine)
player_season_stats_df  = pd.read_sql('SELECT * FROM playerseasonstats', engine)
positions_df            = pd.read_sql('SELECT * FROM position', engine)
season_df               = pd.read_sql('SELECT * FROM season', engine)
team_df                 = pd.read_sql('SELECT * FROM team', engine)


# # Preprocessing

# In[4]:


def check_fk(child_df, child_col, parent_df, parent_col, child_name, parent_name):
    child_keys = set(child_df[child_col].dropna().unique())
    parent_keys = set(parent_df[parent_col].dropna().unique())
    missing = child_keys - parent_keys
    print(f"{child_name}.{child_col} -> {parent_name}.{parent_col}: "
          f"{len(missing)} unmatched value(s)")
    if missing:
        print("  examples:", list(missing)[:10])
        # show the actual offending rows
        bad_rows = child_df[child_df[child_col].isin(missing)]
        print(bad_rows)
    return missing


# ### champion_team_player_df

# In[5]:


champion_team_player_df.head()


# In[6]:


print(champion_team_player_df.isnull().sum())
print('---')
print(f'Duplicated: {champion_team_player_df.duplicated().sum()}')
print('---')
# ChampionTeamPlayer checks
check_fk(champion_team_player_df, 'player_id', player_df, 'player_id', 'ChampionTeamPlayer', 'Player')
check_fk(champion_team_player_df, 'season_id', season_df, 'season_id', 'ChampionTeamPlayer', 'Season')
check_fk(champion_team_player_df, 'team_code', team_df,   'team_code', 'ChampionTeamPlayer', 'Team')


# ### college_df

# In[7]:


college_df.head()


# In[8]:


print('shape:', college_df.shape)
print('---')
print(college_df.isna().sum())
print('---')
print('duplicate:', college_df.duplicated().sum())


# ### country

# In[9]:


country_df.head()


# In[10]:


print('shape:', country_df.shape)
print('---')
print(country_df.isna().sum())
print('---')
print('duplicate:', country_df.duplicated().sum())


# ### mvp_award_df

# In[11]:


mvp_award_df.head()


# In[12]:


print(f'shape:', mvp_award_df.shape)
print('---')
print(mvp_award_df.isnull().sum())
print('---')
print(f'Duplicated: {mvp_award_df.duplicated().sum()}')
print('---')
# ChampionTeamPlayer checks
check_fk(mvp_award_df, 'player_id', player_df, 'player_id', 'ChampionTeamPlayer', 'Player')
check_fk(mvp_award_df, 'season_id', season_df, 'season_id', 'ChampionTeamPlayer', 'Season')


# In[13]:


print(mvp_award_df.value_counts('mvp_rank'))
mvp_award_df[mvp_award_df['mvp_rank'].isna()]


# In[14]:


print(mvp_award_df['mvp_rank'].isna().sum(), 'out of', len(mvp_award_df))
print(mvp_award_df[mvp_award_df['mvp_rank'].isnull()].groupby('season_id').size())


# ### player_df

# In[15]:


player_df.head()


# In[16]:


print('shape:', player_df.shape)
print('---')
print(player_df.isna().sum())
print('---')
print('Duplicated:', player_df.duplicated().sum())


# In[17]:


# Extracting players who their 'weight_kg' is missing
missing_weight_kg = player_df[player_df['weight_kg'].isna()]
print(missing_weight_kg[['player_id', 'player_url']])

# I check the actual url for these 5 players. there is nothing wrong with scraping. 
# four of them are dead ;(

player_df = player_df[player_df['weight_kg'].notna()]
print(player_df.shape)


# In[18]:


# Extracting players who dosn't have 'birth_place' 
missing_birth_place = player_df[player_df['birth_place'].isna()]
missing_birth_place
# I Check the site, there is a bug in scraping players data 


# ### player_college_df

# In[19]:


player_college_df.head()


# In[20]:


print('shape:', player_college_df.shape)
print('---')
print(player_college_df.isna().sum())
print('---')
print('Duplicated:', player_college_df.duplicated().sum())


# ### player_position_df

# In[21]:


player_position_df.head()


# In[22]:


print('shape:', player_position_df.shape)
print('---')
print(player_position_df.isna().sum())
print('---')
print('Duplicated:', player_position_df.duplicated().sum())


# ### player_season_stats_df

# In[23]:


player_season_stats_df.head()


# In[24]:


print('shape:', player_season_stats_df.shape)
print('---')
print(player_season_stats_df.isna().sum())
print('---')
print('Duplicated:', player_season_stats_df.duplicated().sum())


# ### positions_df

# In[25]:


positions_df


# In[26]:


print('shape:', positions_df.shape)
print('---')
print(positions_df.isna().sum())
print('---')
print('Duplicated:', positions_df.duplicated().sum())


# ### season_df

# In[27]:


season_df.head()


# In[28]:


print('shape:', season_df.shape)
print('---')
print(season_df.isna().sum())
print('---')
print('Duplicated:', season_df.duplicated().sum())


# ### team_df

# In[29]:


team_df.head()


# In[30]:


print('shape:', team_df.shape)
print('---')
print(team_df.isna().sum())
print('---')
print('Duplicated:', team_df.duplicated().sum())


# In[31]:


# Tables with missing values

# champion_team_player_df -> a lot
# player_df -> birth_date, birth_place, weight_kg
# mvp_award_df -> mvp_rank
# player_season_stats -> position_code


# # Inspecting Tables
# 

# In[34]:


def numerical_data_summary(df: pd.DataFrame) -> pd.DataFrame:
    numerical_cols = df.select_dtypes(exclude=['str', 'object', 'bool', 'datetime64'])

    summary_df = pd.DataFrame()

    for col in numerical_cols:
        summary_df[col] = {
            'Count': len(df[col]),
            'Unique': df[col].nunique(),
            'Min': df[col].min(),
            'Max': df[col].max(),
            'Mean': df[col].mean(),
            'Mode': df[col].mode()[0],
            'Q1': np.quantile(df[col].dropna(), 0.25),
            'Median': np.quantile(df[col].dropna(), 0.5),
            'Q3': np.quantile(df[col].dropna(), 0.75),
            'Variance': df[col].var(),
            'Std': df[col].std(),
            'range': df[col].max() - df[col].min(),
            'IQR': np.quantile(df[col].dropna(), 0.75) - np.quantile(df[col].dropna(), 0.25),
            'Skewness': df[col].skew(),
            'Kurtosis': df[col].kurtosis(),
        }

    return summary_df


# In[35]:


print(numerical_data_summary(player_df))
print('---')
print(numerical_data_summary(player_season_stats_df))


# # Outlier Handling

# In[42]:


LOW_SAMPLE_GAMES = 10
LOW_SAMPLE_MINUTES = 250

player_season_stats_df['low_sample'] = (
    (player_season_stats_df['games'] < LOW_SAMPLE_GAMES) |
    (player_season_stats_df['minutes'] < LOW_SAMPLE_MINUTES)
)
print(player_season_stats_df['low_sample'].value_counts())


# In[43]:


# IQR-based flag as a supplementary check (for documentation, not automatic removal)
def iqr_outlier_flags(df, col):
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5*iqr, q3 + 1.5*iqr
    return (df[col] < lower) | (df[col] > upper)

for col in ['win_shares', 'bpm', 'vorp']:
    flag = iqr_outlier_flags(player_season_stats_df, col)
    print(f'{col}: {flag.sum()} IQR-flagged rows (kept, not removed -- likely genuine elite/poor seasons)')


# # Feature Engineering

# In[44]:


stats_sorted = player_season_stats_df.sort_values(['player_id', 'season_id']).copy()
stats_sorted['played'] = stats_sorted['games'] > 0

# cumulative count of seasons actually played, inclusive of current season
stats_sorted['experience'] = stats_sorted.groupby('player_id')['played'].cumsum()

player_season_stats_df = stats_sorted.drop(columns=['played'])
player_season_stats_df[['player_id', 'season_id', 'games', 'experience']].head(10)


# In[45]:


player_df['height_m'] = player_df['height_cm'] / 100
player_df['bmi'] = player_df['weight_kg'] / (player_df['height_m'] ** 2)
player_df['agility'] = player_df['height_cm'] / player_df['weight_kg']

player_df[['player_id', 'full_name', 'height_cm', 'weight_kg', 'bmi', 'agility']].head()


# In[46]:


player_season_stats_df['innate_ability'] = (
    player_season_stats_df['experience'] / player_season_stats_df['age']
)
player_season_stats_df[['player_id', 'season_id', 'age', 'experience', 'innate_ability']].head()


# In[47]:


mvp_award_df['is_mvp_candidate'] = True  # presence in this table already means they got votes
champion_team_player_df['is_champion'] = True


# # Binning

# In[48]:


height_bins = [0, 190, 201, 213, 300]
height_labels = ['Guard-height (<190cm)', 'Wing-height (190-201cm)', 'Big-height (201-213cm)', 'Very tall (>213cm)']

player_df['height_bin'] = pd.cut(player_df['height_cm'], bins=height_bins, labels=height_labels)
print(player_df['height_bin'].value_counts())


# In[49]:


player_season_stats_df['experience_qbin'] = pd.qcut(
    player_season_stats_df['experience'], q=4, labels=['Rookie-tier', 'Developing', 'Prime', 'Veteran'], duplicates='drop'
)
print(player_season_stats_df['experience_qbin'].value_counts())


# # Master Table

# In[50]:


master_df = (
    player_season_stats_df
    .merge(player_df.drop(columns=['height_m']), on='player_id', how='left')
    .merge(player_position_df, on='player_id', how='left')
    .merge(positions_df, on='position_id', how='left')
    .merge(
        mvp_award_df[['player_id', 'season_id', 'mvp_rank', 'mvp_share', 'is_mvp_candidate']],
        on=['player_id', 'season_id'], how='left'
    )
    .merge(
        champion_team_player_df[['player_id', 'season_id', 'team_code', 'is_champion']],
        on=['player_id', 'season_id', 'team_code'], how='left'
    )
    .merge(season_df, on='season_id', how='left')
)

# fill the join-created NaNs for the boolean flags with False (they mean "not a candidate / not a champion that season")
master_df['is_mvp_candidate'] = master_df['is_mvp_candidate'].fillna(False)
master_df['is_champion'] = master_df['is_champion'].fillna(False)

print(master_df.shape)
master_df.head()


# In[51]:


# Row count should not blow up vs the base table (player_season_stats_df), aside from
# legitimate one-to-many cases (a player with 2 positions -> 2 rows). Check and understand any growth.
print('player_season_stats_df rows:', len(player_season_stats_df))
print('master_df rows:', len(master_df))

# Spot-check: no player-season should be missing height/weight (player_df had no nulls there)
print('missing height in master:', master_df['height_cm'].isna().sum())
print('missing weight in master:', master_df['weight_kg'].isna().sum())

# Spot-check: mvp candidates and champions counts look sane
print('mvp candidate rows:', master_df['is_mvp_candidate'].sum())
print('champion rows:', master_df['is_champion'].sum())


# In[52]:


# master_df.to_parquet('../Data/master_player_season.parquet', index=False)
master_df.to_csv('../Data/clean_data/master_player_season.csv', index=False)
print('Saved master_player_season.parquet and .csv')

