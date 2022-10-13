from GetToken import GetToken
from GetSongs import GetSongs
import DownloadYoutube as DY

id = "XXX"
secret = "XXX"
# playlist_url = input("Playlist Link: ")
playlist_url = "0cux1Vcmv7TR4mUcEMmbve?si=3dcae81f794d4202"
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

# https://open.spotify.com/playlist/0cux1Vcmv7TR4mUcEMmbve?si=f2131935322f483b