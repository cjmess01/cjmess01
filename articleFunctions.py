import requests
from bs4 import BeautifulSoup as bs
import re

#In progress. Don't use.

def getTitle(url):
    req = requests.get(url)
    soup = bs(req.text, "html.parser")
    return soup.title


print(getTitle("https://insightcrime.org/news/latam-synthetic-drug-trade-booming-unodc-report/"))