#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import time
import random
import re
import os
import string
import pandas as pd
from urllib.robotparser import RobotFileParser


# In[4]:


BASE = "https://www.basketball-reference.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": BASE + "/",
    "Connection": "keep-alive",
}

session = requests.Session()
session.headers.update(HEADERS)

rp = RobotFileParser()
rp.set_url(f"{BASE}/robots.txt")
rp.read()

def allowed(url):
    return rp.can_fetch(HEADERS["User-Agent"], url)


# In[5]:


MIN_DELAY = 3.0
JITTER = 2.0
MAX_RETRIES = 3

_last_request_time = [0.0]

def polite_get(url, max_retries=MAX_RETRIES):
    if not allowed(url):
        raise PermissionError(f"Disallowed by robots.txt: {url}")

    for attempt in range(max_retries):
        elapsed = time.time() - _last_request_time[0]
        wait = MIN_DELAY - elapsed + random.uniform(0, JITTER)
        if wait > 0:
            time.sleep(wait)

        resp = session.get(url, timeout=15)
        _last_request_time[0] = time.time()

        if resp.status_code == 200:
            return resp

        if resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", 60))
            time.sleep(retry_after)
            continue

        if resp.status_code in (500, 502, 503, 504):
            backoff = (2 ** attempt) * 5
            time.sleep(backoff)
            continue

        resp.raise_for_status()

    raise RuntimeError(f"Failed to fetch {url} after {max_retries} attempts")


# In[6]:


def get_players_for_letter(letter):
    url = f"{BASE}/players/{letter}/"
    try:
        resp = polite_get(url)
    except Exception as e:
        print(f"Could not fetch index for letter '{letter}': {e}")
        return []

    soup = BeautifulSoup(resp.content, "lxml")
    table = soup.find("table", id="players")
    if table is None or table.find("tbody") is None:
        return []

    players = []
    for row in table.find("tbody").find_all("tr"):
        th = row.find("th")
        if th is None:
            continue
        a = th.find("a")
        if a is None:
            continue
        players.append({
            "name": a.get_text(strip=True),
            "url": BASE + a["href"],
        })
    return players


def get_all_player_links(letters=None):
    if letters is None:
        letters = string.ascii_lowercase
    all_players = []
    for letter in letters:
        players = get_players_for_letter(letter)
        all_players.extend(players)
        print(f"{letter}: {len(players)} players (running total: {len(all_players)})")
    return all_players


# In[7]:


player_links = get_all_player_links()
len(player_links)


# In[8]:


player_links[-5:]


# In[11]:


from tqdm import tqdm


# In[12]:


HTML_DIR = "nba_player_html"
os.makedirs(HTML_DIR, exist_ok=True)

def player_id_from_url(url):
    return url.rstrip('/').split('/')[-1].replace('.html', '')

def download_all_players(player_links, out_dir=HTML_DIR, skip_existing=True):
    failed = []
    to_fetch = []

    for player in player_links:
        pid = player_id_from_url(player["url"])
        path = os.path.join(out_dir, f"{pid}.html")
        if skip_existing and os.path.exists(path):
            continue
        to_fetch.append(player)

    print(f"{len(player_links) - len(to_fetch)} already downloaded, {len(to_fetch)} left to fetch")

    # for i, player in enumerate(to_fetch):
    for i, player in enumerate(tqdm(to_fetch, desc="Downloading player pages", unit="pages")):
        url = player["url"]
        pid = player_id_from_url(url)
        path = os.path.join(out_dir, f"{pid}.html")
        try:
            resp = polite_get(url)
            with open(path, "wb") as f:
                f.write(resp.content)
        except PermissionError as e:
            print(f"Skipping (robots.txt disallows): {url}")
        except Exception as e:
            print(f"Failed {url}: {e}")
            failed.append({"url": url, "error": str(e)})

        if (i + 1) % 25 == 0:
            # print(f"Downloaded {i + 1}/{len(to_fetch)}")
            tqdm.write(f'Downloaded {i+1}/{len(to_fetch)}')

    if failed:
        pd.DataFrame(failed).to_csv("nba_download_failed.csv", index=False)
        print(f"{len(failed)} downloads failed - see nba_download_failed.csv")

    print("Download phase complete.")


# In[13]:


download_all_players(player_links)


# In[ ]:




