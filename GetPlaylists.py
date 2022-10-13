import requests
import json
# Under development


class GetPlaylists:
    def __init__(self, token):
        self.token = token

    def get_user_id(self):
        user = requests.get(url='https://api.spotify.com/v1/me',
                            headers={
                                'Authorization': 'Bearer ' + self.token})
        response = json.loads(bytes.decode(user.content, 'utf-8'))
        print(response)
        user_id = response["id"]
        print(user_id)
        return user_id

    def get_all_uesrs_playlists(self):
        uid = self.get_user_id()
        playlist = requests.get(url=f'https://api.spotify.com/v1/users/{uid}/playlists',
                                headers={
                                    'Authorization': f'Bearer {self.token}'})
        response = json.loads(bytes.decode(playlist.content, 'utf-8'))
        playlists_list = []
        # for i in response["items"]:
        #     playlists_list.append({"name": i["name"], "link": i["tracks"]["href"]})
        print(response)
        return response

    def start_fetch_playlist(self):
        return self.get_all_uesrs_playlists()
