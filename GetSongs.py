import requests


class GetSongs:
    def __init__(self, token, url):
        self.url = url
        self.token = token

    def fetch_songs_from_playlist(self, playlist_url):
        playlist_id = playlist_url.split('?')[0].split('/')[-1]
        custom_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?offset=0&limit=100'
        songs = []
        while True:
            a = requests.get(url=custom_url,
                             headers={"Authorization": f'Bearer {self.token}'})
            tracks_response = a.json()
            for i in tracks_response["items"]:
                tmp = {}
                tmp["song"] = i["track"]["name"]
                tmp["artist"] = i["track"]["artists"][0]["name"]
                songs.append(tmp)
            if tracks_response["next"] is not None:
                custom_url = tracks_response["next"]
            else:
                break
        return songs

    def start_get_songs(self):
        return self.fetch_songs_from_playlist(self.url)
