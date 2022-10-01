# crawl

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

# crawl all categoriess
def crawlCategories():
    print("Start crawl categories")
    categories = []
    soupCate = url("https://link.springer.com/search/facetexpanded/discipline?facet-content-type=%22Journal%22")
    for _cate in soupCate.find_all('span',{'class' : 'facet-title'}):
        categories.append(_cate.get_text())
    return categories

# crawl all titles
def crawlTitles(whiteList = []):
    _cates = crawlCategories()
    mappedByCate = {}
    for _cate in _cates:
        print("Start crawl title (only first page) in cate=" + _cate)
        titles = []
        soupTitle = url(baseURL + "&facet-discipline=" + _cate)
        for _title in soupTitle.find_all('a',{'class' : 'title'}):
             titles.append(_title.get_text())
        mappedByCate[_cate] = titles
    return mappedByCate

# main
def startCrawl():
    titles = crawlTitles()
    displayTitles = []
    displayCates = []
    for _cate in titles.keys():
        for _title in titles[_cate]:
            displayTitles.append(_title)
            displayCates.append(_cate)
    df = pd.DataFrame({'Name': displayTitles,'Discipline': displayCates}) 
    df.to_csv('C:/Users/ttkph/Desktop/titles_by_discipline.csv', index=False, encoding='utf-8')

startCrawl()

# if __name__=="__main__":
#     URLMathematics = "https://link.springer.com/search?facet-content-type=%22Journal%22&facet-discipline=%22Mathematics%22"
#     # URLPhysics = "//link.springer.com/search?facet-content-type=%22Journal%22&facet-discipline=%22Physics%22&just-selected-from-overlay=facet-discipline&just-selected-from-overlay-value=%22Physics%22"
#     # URLChemistry = "https://link.springer.com/search?facet-content-type=%22Journal%22&facet-discipline=%22Chemistry%22&just-selected-from-overlay=facet-discipline&just-selected-from-overlay-value=%22Chemistry%22"
#     # URLMedicine_Public_Health = "https://link.springer.com/search?facet-content-type=%22Journal%22&facet-discipline=%22Medicine+%26+Public+Health%22"
#     # URLComputer_Science = "https://link.springer.com/search?facet-content-type=%22Journal%22&facet-discipline=%22Computer+Science%22&just-selected-from-overlay=facet-discipline&just-selected-from-overlay-value=%22Computer+Science%22"
#     # URLEconomics = "https://link.springer.com/search?facet-content-type=%22Journal%22&facet-discipline=%22Economics%22&just-selected-from-overlay=facet-discipline&just-selected-from-overlay-value=%22Economics%22"
#     soupmath = url(URLMathematics)
#     # soupPhysics = url(URLPhysics)
#     # soupChemistry = url(URLChemistry)
#     # soupMedicine_Public_Health = url(URLMedicine_Public_Health)
#     # soupComputer_Science = url(URLComputer_Science)
#     # soupEconomics = url(URLEconomics)
#     # Lay cac the loai du lieu
#     Discipline = []
#     name = []
#     #math
#     for x in range(1,12):
#          URLMathematics1 = "https://link.springer.com/search/page/" + str(x) + "?facet-content-type=%22Journal%22&facet-discipline=%22Mathematics%22"
#          soup = url(URLMathematics1)
#          for y in soup.find_all('a',{'class' : 'title'}):
#              name.append(y.get_text())
#          for z in soup.find_all('span',{'class' : 'facet-title'}):
#              Discipline.append(z.get_text())
#          print("crawled " + str(x) + "/ 12 pages")

#     # input csv
#     df = pd.DataFrame({'Name': name,'Discipline': Discipline}) 
#     df.to_csv('C:/Users/ttkph/Desktop/Discipline_link.csv', index=False, encoding='utf-8')