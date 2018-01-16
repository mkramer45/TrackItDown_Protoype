import bs4
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import sqlite3

my_url = ['https://www.beatport.com/genre/deep-house/12/top-100', 
'https://www.beatport.com/genre/tech-house/11/top-100',
'https://www.beatport.com/genre/house/5/top-100', 
'https://www.beatport.com/genre/progressive-house/15/top-100',
'https://www.beatport.com/genre/funk-soul-disco/40/top-100',
'https://www.beatport.com/genre/indie-dance-nu-disco/37/top-100',
'https://www.beatport.com/genre/funky-groove-jackin-house/81/top-100',
'https://www.beatport.com/genre/leftfield-house-and-techno/80/top-100',
'https://www.beatport.com/genre/dj-tools/16/top-100',
'https://www.beatport.com/genre/minimal-deep-tech/14/top-100',
 'https://www.beatport.com/genre/techno/6/top-100']
# opening up connecting, grabbing the page

for url in my_url:

	uClient = uReq(url)
# this will offload our content in'to a variable
	page_html = uClient.read()
# closes our client
	uClient.close()

# html parsing
	page_soup = soup(page_html, "html.parser")

	containers = page_soup.findAll("li",{"class":"bucket-item ec-item track"})

	print(url)

	conn = sqlite3.connect('Beatscrape.db')
	cursor = conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS Tracks(Artist TEXT, Song TEXT, Label TEXT, Price DECIMAL, ChartPosition TEXT, Genre TEXT, Websource TEXT)')



# MSK, artist name
	for container in containers:

		artistName = container["data-ec-d1"] 

		song_Name = container["data-ec-name"]

		label_Name = container["data-ec-brand"] 

		price_Amount = container["data-ec-price"]

		chart_position = container["data-ec-position"]

		song_Genre = container["data-ec-d3"]

		web_source = 'Beatport'

		conn = sqlite3.connect('Beatscrape.db')
		cursor = conn.cursor()
		cursor.execute("INSERT INTO Tracks VALUES (?, ?, ?, ?, ?, ?, ?)", (artistName, song_Name, label_Name, price_Amount, chart_position, song_Genre, web_source))

		conn.commit()
		cursor.close()
		conn.close()
#cursor.execute('CREATE TABLE IF NOT EXISTS ArtistMonitor(id INTEGER PRIMARY KEY AUTOINCREMENT, DJname TEXT)')




