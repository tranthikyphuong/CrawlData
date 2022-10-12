from re import S
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
        test = False
        URLsearch = url('https://link.springer.com/search?query='+str(x)+'&facet-content-type=%22Journal%22')
        for _cate in URLsearch.find('div', { 'id': 'discipline-facet' }).find_all('span', { 'class': 'facet-title' }):
            test = True
            categories.append(_cate.get_text())
            break
        if test == False:
            categories.append('Erro')
        print("crawled name:  " + str(x))
    return categories
def sub_discipline_facet():
    sub = []
    string = []
    for x in name.journal:
        test = False
        URLsearch = url('https://link.springer.com/search?query='+str(x)+'&facet-content-type=%22Journal%22')
        for _sub in URLsearch.find('div', { 'id': 'sub-discipline-facet' }).find_all('span', { 'class': 'facet-title' }):
            test = True
            sub.append(_sub.get_text())
        if test == False:
            sub.append('Erro')
    for s in sub:
        string += ', ' + s
    return  string[1:] 
def startCrawl():
    displayCates = crawlCategories()
    sub_discipline = sub_discipline_facet()
    df = pd.DataFrame({'Name': name.journal,'Discipline': displayCates,'Sub-Discipline': sub_discipline}) 
    df.to_csv('C:/Users/ttkph/Desktop/categories-Springer-v1-train.csv', index=False, encoding='utf-8')
startCrawl()