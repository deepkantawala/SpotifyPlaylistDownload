from GetToken import GetToken
from GetSongs import GetSongs


id = "xxx"
secret = "xxx"
playlist_url = input("Playlist Link: ")
gt = GetToken(id, secret)
token = gt.start()
if token is None:
    print("Unauthorised, make sure you save the playlist to your library")
else:
    print(token)
    gs = GetSongs(token, playlist_url)
    all_songs = gs.start_get_songs()
    print(all_songs)
