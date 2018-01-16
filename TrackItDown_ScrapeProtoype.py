from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import sqlite3
import re

url = 'https://www.trackitdown.net/genre/techno/top10.html'
# opening up connecting, grabbing the page

uClient = uReq(url)
# this will offload our content in'to a variable
page_html = uClient.read()
# closes our client
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll('div', class_=re.compile("featuredTracks track"))




