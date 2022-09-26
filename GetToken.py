import requests
import time
import base64


class GetToken:

    def __init__(self, id, secret, token_url):
        self.id = id
        self.secret = secret
        self.token_url = token_url

    def create_token_header(self, id, secret):
        print("Initiating create_token_header method")
        client_cr = f"{id}:{secret}"
        client_cr_64 = base64.b64encode(client_cr.encode())
        print("Base64 of id:secret: ", client_cr_64)
        header = {
            "Authorization": f"Basic {client_cr_64.decode()}"
        }
        print("Header: ", header)
        return header

    def request_token(self,token_url ,data, header):
        res = requests.post(token_url, data=data, headers=header)
        print(res.json())
        res_json = res.json()
        return res_json["access_token"]


    def start(self):
        ct = self.create_token_header(id = self.id, secret = self.secret)
        rt = self.request_token(token_url=self.token_url, data = {"grant_type": "client_credentials"}, header=ct)
        return rt





id = "b0b98946ddda49f793801e7a158c88a0"
secrete = "628d3aab1e6749b8aec3b4d5f960bb93"
uri = "https://api.spotify.com/v1/DeepKantawala/tracks"

token_url = "https://accounts.spotify.com/api/token"


gt = GetToken(id, secrete, token_url)
token = gt.start()
print(token)

