#import Libraries
import requests
import urllib.request
import pandas as pd
import lxml
import html5lib

from bs4 import BeautifulSoup #third party library to extract data from html and xml files

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"# url of the web page contents to download
source_code= requests.get(url)#GET requests web server to download the html contents of a web page
plain_text=source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

table = soup.find('table',attrs={'class': 'wikitable sortable plainrowheaders'}) #find table with class name 'wikitable sortable plainrowheaders'
rows = table.find_all('tr') #store tr tags in variable row
for row in rows:    # loop through each tr tag
    cols_th = row.find_all('th')    #find all th tags
    print("Printing th contents:")
    cols_th = [y.text.strip() for y in cols_th] #remove excess content and store contents of each th tag
    print(cols_th)
    cols = row.find_all('td')   #find all td tags
    print("Printing td contents:")
    cols = [x.text.strip() for x in cols] #remove excess content and store contents of each td tag
    print (cols)

table_all = soup.find_all('table')  #find all tables in the given url
for tables in soup.find_all('table'):
    rows = table.find_all('tr')
    for row in rows:    # loop through each tr tag
        cols_th = row.find_all('th')     #find all th tags
        print("Printing th contents:")
        cols_th = [y.text.strip() for y in cols_th] #remove excess content and store contents of each th tag
        print(cols_th)
        cols = row.find_all('td')   #find all td tags
        print("Printing td contents:")
        cols = [x.text.strip() for x in cols]   #remove excess content and store contents of each td tag
        print(cols)
#Print all tables in the dataframe using pandas
print(pd.read_html(url))
print(pd.read_html(url, match="wikitable sortable plainrowheaders"))