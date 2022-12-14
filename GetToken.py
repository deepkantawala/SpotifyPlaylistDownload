import requests
import base64


class GetToken:
    def __init__(self, id, secret):
        self.id = id
        self.secret = secret
        self.token_url = "https://accounts.spotify.com/api/token"

    def create_token_header(self, id, secret):
        client_cr = f"{id}:{secret}"
        client_cr_64 = base64.b64encode(client_cr.encode())
        header = {
            "Authorization": f"Basic {client_cr_64.decode()}"
        }
        return header

    def request_token(self, token_url, data, header):
        try:
            res = requests.post(token_url, data=data, headers=header)
            res_json = res.json()
            return res_json["access_token"]
        except Exception as e:
            return None

    def start(self):
        ct = self.create_token_header(id=self.id, secret=self.secret)
        rt = self.request_token(token_url=self.token_url, data={"grant_type": "client_credentials"}, header=ct)
        if rt is None:
            return None
        return rt
