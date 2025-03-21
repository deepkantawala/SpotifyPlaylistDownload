from GetToken import GetToken
from GetSongs import GetSongs
import DownloadYoutube as DY

id = "XXX"
secret = "XXX"
playlist_url = input("Playlist Link: ")
gt = GetToken(id, secret)
print("Starting")
path = input(f"""Please enter path where to download songs (ex: "D:/test1/test2/") - """)
token = gt.start()
if token is None:
    print("Unauthorised, make sure you save the playlist to your library")
else:
    gs = GetSongs(token, playlist_url)
    all_songs = gs.start_get_songs()
    print(all_songs)
    gs = DY.GetYTSongs(path)
    gs.start(all_songs)
