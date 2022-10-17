# I often have to travel through bus to get to my college, and my part-time job which is quite far and i like to listen to music when I travel.
# There are quite a few places on the way where I get network issue, I also have to save my internet data as it is limited so I came up with a idea and 
# Created a project named SpotifyPlaylistDownload with my friend Shravan Patel, which will download songs from spotify playlist after which i can listen to songs without using internet data  

## This project contains the following files:

### - DownloadYoutube.py : This file is used to download songs from youtube.
### - GetPlaylists.py : This file is used to get spotify playlist of a user. (under Development)
### - GetSongs.py : This file is used to get playlisy through spotify API
### - GetToken.py : This file is used to get Bearer token which is required to get playlist from spotify's API.
### - main.py : This is a main file which we execute and it will call methods from other files in order to download the songs

## Known issues:

### - [1] pytube's search object sometimes throws execption for few songs.
### - [2] Some songs which are more popular than the original one are downloaded instead.

## Future plan:

### - [1] Bypass age restriction for some explicit songs.
### - [2] Better logging.
### - [3] Check previously downloaded songs and ignore them while downloading.