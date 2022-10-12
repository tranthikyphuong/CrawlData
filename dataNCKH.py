from unicodedata import category
from cleandata import name
from faulthandler import disable
import requests
import pandas as pd
import io
import scrapy
from pathlib import Path
from bs4 import BeautifulSoup
baseURL = 'https://link.springer.com/search?facet-content-type=%22Journal%22'
# get html from url
def url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
def crawlCategories():
    categories = []
    for x in name.journal:
        URLsearch = url('https://link.springer.com/search?query='+str(x)+'&facet-content-type=%22Journal%22')
        for _cate in URLsearch.find_all('span',{'class' : 'facet-title'}):
            categories.append(_cate.get_text())
    print("crawled name:  " + str(x))
    return categories
print(crawlCategories())
def startCrawl():
    displayCates = crawlCategories()
    print(displayCates)
    # df = pd.DataFrame({'Name': name.journal,'Discipline': displayCates}) 
    # df.to_csv('C:/Users/ttkph/Desktop/categories-Springer-v1-train.csv', index=False, encoding='utf-8')
# startCrawl()