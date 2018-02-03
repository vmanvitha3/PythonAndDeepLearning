#program that parse a wikipage then extract the headers of the page.

#import all libraries
import requests
import urllib.request

from bs4 import BeautifulSoup #third party library to extract data from html and xml files

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"# url of the web page contents to download
source_code= requests.get(url)#GET requests web server to download the html contents of a web page
plain_text=source_code.text
bsObj = BeautifulSoup(plain_text, "html.parser")
title = bsObj.title #Save title in a variable
print("Title is ",title)#print title


for link in bsObj.find_all('a'):#find all instances of a tag on the page and save them to result variable
    print(link.get('href')) #print links from a tags
)