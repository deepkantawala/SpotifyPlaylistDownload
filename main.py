from GetToken import GetToken
from GetSongs import GetSongs
import DownloadYoutube as DY

id = "xxxxxxxxxxxxxxxxxx"
secret = "xxxxxxxxxxxxxxxxxx"
# playlist_url = input("Playlist Link: ")
playlist_url = "https://open.spotify.com/playlist/4a40bfbdBAbJDtQDGoNuhR?si=f26aa89c79314d95"
gt = GetToken(id, secret)
print("Starting")
token = gt.start()
if token is None:
    print("Unauthorised, make sure you save the playlist to your library")
else:
    print("Token is:", token)
    gs = GetSongs(token, playlist_url)
    all_songs = gs.start_get_songs()
    print(all_songs)
    gs = DY.GetYTSongs()
    gs.start(all_songs)
