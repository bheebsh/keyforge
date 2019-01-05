import requests
import json
from time import sleep
import random
import os.path

# Url format is:
# https://www.keyforgegame.com/api/decks/?page={0}&page_size={1}

data_dir = os.path.relpath("data/decks/")

# I want to get the data on decks & cards
# To do so, use requests to query the page using above template to get decks
# Then parse each deck int oa separate .json file which will be stored in
# ../data/decks

base_url = "https://www.keyforgegame.com/api/decks/?"
query_url = "page=%d&page_size%d"

# First, i need to update the number of decks
# Number of decks at time of writing is 443k, but it's constantly changing
url = base_url + (query_url % (1, 1))
r = requests.get(url)
total_decks = r.json()["count"]

decks_per_page = 30 # API has limit of 30
num_pages = 1

for i in range(1, num_pages + 1):
    url = base_url + (query_url % (i, decks_per_page))
    r = requests.get(url)

    start_num = (i - 1) * decks_per_page + 1
    end_num = i * decks_per_page
    outname = os.path.join(data_dir, "decks-%d-%d.json" % (start_num, end_num))

    with open(outname, "w") as outfile:
        json.dump(r.json()["data"], outfile)



    sleep(5)
