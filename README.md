# WPRBtoSpotifyPlaylist
The goal is to make a tool to turn a published playlist from the radio station 103.3 WPRB (New Jersey's only radio station) into a Spotify playlist

Right now I am planning to use the following solutions to get this done,
    BeautifulSoup - Python backend webscraper
    Flask - Host Python API
    React - Call Spotify API and my Python API
    Spotify API - Auth user, search songs returned from my API, and add those songs to a new playlist in the users library
    
Looking to dip into Docker in the future to host but that will be outside the scope of my MVP.

MVP will be that a user submits a link from a WPRB playlist, auths into Spotify, then the user will get a preview of the playlist that was built from the link provided, then the user has the option to add the genrated playlist to their Spotify library. Also hoping to have it note anything that couldnt be found on Spotify/not availabe to stream in the users country. 
