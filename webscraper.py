import requests
from bs4 import BeautifulSoup

URL = "https://spinitron.com/WPRB/pl/14609784/Flat-Circle-Radio-Hour"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# get the main container the content is in. I tried making the scraper get the spins-char here and skipping the next
# line but that broke the iterations
results = soup.find("div", class_="main-container")

song_elements = results.find("table", class_="table table-striped table-bordered")

for element in song_elements.contents[0].children:
    artistName = element.find("span", class_="song")
    songName = element.find("span", class_="song")
    albumName = element.find("span", class_="release")
    print(artistName.text)
    print(songName.text)
    print(albumName.text)
    print()
