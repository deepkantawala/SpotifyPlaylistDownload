import glob
import os
import json
import requests

# token_api = requests.post(url='https://accounts.spotify.com/api/token',
#                           data={
#                               'code': 'AQDkg81SuMEdKU6GVfehCPEi1MPct2iBBTr9yxcQEC4jpzVBC1DhMllkNSx09LM_BSRwek4ea-8Ry2l9IpfM-tEApirzxf1LxMJc_GhRCiK-5uhTNdRj9akDauDttPfy2LL3TM4AoaGSRwnswghUCTuHR35OoELgZZ6pLWd64OiP1k0',
#                               'redirect_uri': 'http://localhost:12345/callback', 'grant_type': 'authorization_code'},
#                           headers={'Authorization': 'Basic ' + base64.b64encode(
#                               b'xxxxxxxxxxxxxxxx:xxxxxxxxxxxxxxxxxx').decode('ascii')})
# token = json.loads(bytes.decode(token_api.content, 'utf-8'))
# access_token = token["access_token"]
# refresh_token = token["refresh_token"]
# refresh_token_api = requests.post(url='https://accounts.spotify.com/api/token',
#                                   data={'refresh_token': refresh_token, 'grant_type': 'refresh_token'},
#                                   headers={'Authorization': 'Basic ' + base64.b64encode(
#                                       b'xxxxxxxxxxxxxxxxx:xxxxxxxxxxxxxxxxx').decode(
#                                       'ascii')})
# token = json.loads(bytes.decode(refresh_token_api.content, 'utf-8'))
# print(token)
# user = requests.get(url='https://api.spotify.com/v1/me',
#                     headers={
#                         'Authorization': 'Bearer BQBGFJg2LaSWBevlMPHS-ksvEfhGuNT2naz8GaRZU5y7yMqr06SmlB7tDDsl9JHrzpNd8PooctCuS_DuK9ZaURet8ZsXAQS3GIoX1grF5Ijx3L1wzRIaJRTPcNgRJARAR9dpsuJyHl8GF9tpRkcDaYPCKUrgBFyIJzKkBNao-1lCuW5cATmByMklYKnJ--ySAg'})
# response = json.loads(bytes.decode(user.content, 'utf-8'))
# user_id = response["id"]
# print(user_id)
playlist = requests.get(url=' https://api.spotify.com/v1/me/playlists',
                        headers={
                            'Authorization': 'Bearer BQCyNPrrH8oLHwCPolnmzC4NZDtt3XLV64FwtH0wjM5dleNUynFWVhAeNq1taoGAYb_ieVkz8vQfYiy8xdcPpHwT5d3nIBw8ojrjMr3irEiRzr8QEHT5qC2hO-hVeLkS2_M_AQGgNlzswysbnTW4-CKw2rIxxUYbir6rK3mEK41LDZsOlH4uZDs6E192MUQbQRpiZDSmzIOQMfHokgc4urjxWe2y_n4kTY9CPMW-yOarneTgKVgEqdDOxNF_jDUB43piJrEo126Fl0VkjZ7TYwEqaq5_FHZSkuHndLi6Lpqz3wA'})
response = json.loads(bytes.decode(playlist.content, 'utf-8'))
playlists_list = []
for i in response["items"]:
    playlists_list.append(i["tracks"]["href"])
print(playlists_list)
songs = []
for pl in playlists_list:
    pl_link = pl + '?offset=0&limit=100&locale=en-US,en;q=0.5'
    while True:
        tracks = requests.get(
            url=pl_link,
            headers={
                'Authorization': 'Bearer BQCyNPrrH8oLHwCPolnmzC4NZDtt3XLV64FwtH0wjM5dleNUynFWVhAeNq1taoGAYb_ieVkz8vQfYiy8xdcPpHwT5d3nIBw8ojrjMr3irEiRzr8QEHT5qC2hO-hVeLkS2_M_AQGgNlzswysbnTW4-CKw2rIxxUYbir6rK3mEK41LDZsOlH4uZDs6E192MUQbQRpiZDSmzIOQMfHokgc4urjxWe2y_n4kTY9CPMW-yOarneTgKVgEqdDOxNF_jDUB43piJrEo126Fl0VkjZ7TYwEqaq5_FHZSkuHndLi6Lpqz3wA'})
        tracks_response = json.loads(bytes.decode(tracks.content, 'utf-8'))
        for i in tracks_response["items"]:
            tmp = {}
            tmp["song"] = i["track"]["name"]
            tmp["artist"] = i["track"]["artists"][0]["name"]
            songs.append(tmp)
        if tracks_response["next"] != None:
            pl_link = tracks_response["next"]
        else:
            break
print(len(songs), songs)

