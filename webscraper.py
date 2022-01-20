import requests
from bs4 import BeautifulSoup

URL = "https://spinitron.com/WPRB/pl/14609784/Flat-Circle-Radio-Hour"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# get the main container the content is in. I tried making the scraper get the spins-char here and skipping the next
# line but that broke the iterations
#results = soup.find_all("div", class_="main-container")

# get the table and its elements
song_elements = soup.find_all("td", class_="spin-text")

#print(song_elements)
# iterate through the table and get the artist name, song title, and album name
for element in song_elements:
    artistName = element.find("span", class_="artist")
    songName = element.find("span", class_="song")
    albumName = element.find("span", class_="release")
    print(artistName.text)
    print(songName.text)
    print(albumName.text)
    print()
