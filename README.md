# WPRBtoSpotifyPlaylist
The goal is to make a tool to turn a published playlist from the radio station 103.3 WPRB (New Jersey's only radio station) into a Spotify playlist

Right now I am planning to use the following solutions to get this done,

	-BeautifulSoup: Python backend web scraper
	-Flask: Create Python API
	-React: Call Spotify API and my Python API
	-Spotify API: Auth user, search songs returned from my API, and add those songs to a new playlist in the users library
    
Looking to dip into Docker in the future to host but that will be outside the scope of my MVP.

MVP will be that a user submits a link from a WPRB playlist, auths into Spotify, then the user will get a preview of the playlist that was built from the link provided, then the user has the option to add the generated playlist to their Spotify library. Also hoping to have it note anything that couldn’t be found on Spotify/not available to stream in the users country.

Hoping in the future to add the ability to enter a show name and get a playlist of all the music from every airing of that show.
