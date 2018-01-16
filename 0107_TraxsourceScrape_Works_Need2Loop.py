import bs4
import requests
from bs4 import BeautifulSoup as soup
import sqlite3
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

my_url = [
'https://www.traxsource.com/genre/20/techno/top',
 'https://www.traxsource.com/genre/18/tech-house/top',
 'https://www.traxsource.com/genre/4/house/top',
 'https://www.traxsource.com/genre/24/soulful-house/top',
 'https://www.traxsource.com/genre/17/nu-disco-indie-dance/top',
 # 'https://www.traxsource.com/genre/15/jackin-house',
 # 'https://www.traxsource.com/genre/16/minimal',
 # 'https://www.traxsource.com/genre/19/progressive-house',
 # 'https://www.traxsource.com/genre/27/afro-house',
 # 'https://www.traxsource.com/genre/23/afro-latin-brazilian',
 # 'https://www.traxsource.com/genre/7/accapella',
 # 'https://www.traxsource.com/genre/21/sounds-samples-and-loops'
 ]


for url in my_url:

    uClient = uReq(url)

    page_html = uClient.read()

    uClient.close()

    page_soup = soup(page_html, "html.parser")

    tracks = page_soup.findAll('div', class_=re.compile("trk-row play-trk"))

    print(url)

    conn = sqlite3.connect('Beatscrape.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Tracks(Artist TEXT, Song TEXT, Label TEXT, Price DECIMAL, ChartPosition TEXT, Genre TEXT, Websource TEXT)')

    for track in tracks:

    # get the name of the song
        song = track.find('div', class_='trk-cell title')
        songx = song.text.strip()

    # get the name(s) of the artist
        artist = track.find('div', class_='trk-cell artists')
        artistx = artist.text.strip()

        genre = track.find('div', class_='trk-cell genre')
        genrex = genre.text.strip()

        label = track.find('div', class_='trk-cell label')
        labelx = label.text.strip()

        released = track.find('div', class_='trk-cell r-date')
        releasedx = released.text.strip()

        price = track.find('div', class_='buy-cont')
        pricex = price.text.strip()

        position = track.find('div', class_='trk-cell tnum-pos')
        positionx = position.text.strip()

        web_source = 'Traxsource'


        conn = sqlite3.connect('Beatscrape.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Tracks VALUES (?, ?, ?, ?, ?, ?, ?)", (artistx, songx, labelx, pricex, positionx, genrex, web_source))
        conn.commit()
        cursor.close()
        conn.close()