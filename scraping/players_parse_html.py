#!/usr/bin/env python
# coding: utf-8

# In[65]:


from bs4 import BeautifulSoup
import re
import os
import pandas as pd


# ## Getting Players Information

# In[69]:


def find_general_info(soup, url):
    info = {
        'player_id': None, 'full_name': None, 'birth_date': None, 'born': None,
        'height': None, 'weight': None, 'nationality': None,
        'position': None, 'shoots': None, 'college': None,
        'high_school': None, 'career_length': None, 'link': url,
    }

    meta = soup.find('div', id='meta')
    if meta is None:
        return info

    h1 = meta.find('h1')
    if h1:
        info['full_name'] = h1.text.strip()

    nat_span = meta.find('span', class_='f-i')
    if nat_span:
        info['nationality'] = nat_span.get_text(strip=True)

    for p in meta.find_all('p'):
        # text = p.get_text(strip=True)
        text = re.sub(r'\s+', ' ', p.get_text(separator=' ', strip=True)).strip()
        try:
            if 'Career Length' in text:
                info['career_length'] = text.replace('Career Length:', '').strip()

            elif 'Position' in text:
                m = re.search(r'Position:\s*(.+)', text)
                if m:
                    pos = m.group(1)
                    # strip off a trailing 'Shoots:' fragment if present on the same line
                    pos = re.split(r'Shoots:', pos)[0].strip(' \u25aa')
                    info['position'] = pos.strip()
                m2 = re.search(r'Shoots:\s*(\w+)', text)
                if m2:
                    info['shoots'] = m2.group(1).strip()

            elif 'College' in text:
                info['college'] = text.replace('College:', '').strip()

            elif 'High School' in text:
                info['high_school'] = text.replace('High School:', '').strip()



            elif 'Born' in text:
                # Grab everything after "Born:" up to " in " (if present) or end of string
                m = re.search(r'Born:\s*(.*?)(?:\s+in\s+.*)?$', text)
                if m:
                    info['birth_date'] = m.group(1).strip()
                m2 = re.search(r'\bin\s+(.*)', text)
                if m2:
                    info['born'] = m2.group(1).strip()


            # e.g. 6-5,205lb(196cm, 92kg)
            elif 'lb' in text or 'kg' in text or 'cm' in text:
                m = re.search(r'\((\d{3})cm', text)
                if m:
                    info['height'] = m.group(1).strip()
                m2 = re.search(r'(\d{2,3})kg', text)
                if m2:
                    info['weight'] = m2.group(1).strip()
        except Exception:
            # don't let one malformed field kill the whole player
            continue

    return info


def find_stats(soup):
    stats = {}
    for div in soup.select(".stats_pullout .p1 > div, .stats_pullout .p2 > div, .stats_pullout .p3 > div"):
        try:
            strong = div.find("strong")
            if strong is None:
                continue
            key = strong.get_text(strip=True)
            ps = div.find_all("p")
            if not ps:
                continue
            value = ps[-1].get_text(strip=True)
            stats[key] = float(value)
        except (ValueError, AttributeError):
            continue
    return stats


# In[70]:


# Step 1: List the files and open one

PATH = '../nba_player_html'
data_dir = os.listdir(PATH)
print(f'{len(data_dir)} html have been scraped successfully.')


# In[71]:


for h in data_dir[:5]:
    print(h)


# In[72]:


results = []
BASE = "https://www.basketball-reference.com"
for html in data_dir:
    p = os.path.join(PATH, html)
    with open(p, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'lxml')
    url = BASE + f'/players/{html[0]}/{html}'
    info = find_general_info(soup, url)
    stats = find_stats(soup)
    info.update(stats)
    results.append(info)


# In[83]:


df = pd.DataFrame(results)
df.head()


# In[56]:


df.info()


# In[84]:


df.isnull().sum()


# ### Add `player_id` column

# In[86]:


def add_player_id_col(df):
    df.drop(columns='player_id', inplace=True)
    players_id = df['link'].map(lambda x: x.split('/')[-1].replace('.html', ''))
    df.insert(0, 'player_id', players_id)
    return df

def save_new_df_to_csv(df, path):
    df.to_csv(path) 


# In[87]:


# insert player_id column to raw data
path = os.path.join('../Data/raw_data', 'players.csv')
df = add_player_id_col(df)
save_new_df_to_csv(df, path)
df.head()


# In[88]:


df.info()


# # Missing Values

# In[89]:


df.isna().sum()


# ## birth_date

# In[90]:


df.loc[df['birth_date'].isna()][['player_id', 'link']]

