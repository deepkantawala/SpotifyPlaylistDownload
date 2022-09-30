from GetToken import GetToken
from GetSongs import GetSongs


id = "xxx"
secret = "xxx"
token_url = "https://accounts.spotify.com/api/token"
playlist_url = input("Playlist Link: ")
gt = GetToken(id, secret, token_url)
token = gt.start()
print(token)
gs = GetSongs(token, playlist_url)
all_songs = gs.start_get_songs()
print(all_songs)
