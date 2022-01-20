import requests
from bs4 import BeautifulSoup

# URL of the page that is to be scraped
URL = "https://spinitron.com/WPRB/pl/14609784/Flat-Circle-Radio-Hour"
page = requests.get(URL)

# parse the contents of the page into a BeautifulSoup obj from bs4 (BeautifulSoup4)
soup = BeautifulSoup(page.content, "html.parser")

# get the table and its elements
song_elements = soup.find_all("td", class_="spin-text")

# print(song_elements)

# iterate through the table and print each artist name, song title, and album name
for element in song_elements:
    artistName = element.find("span", class_="artist")
    songName = element.find("span", class_="song")
    albumName = element.find("span", class_="release")
    print(artistName.text)
    print(songName.text)
    print(albumName.text)
    print()
