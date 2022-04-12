from secrets import refresh_token, base_64
import requests, json

class Refresh:
    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64 = base_64

    def refresh(self):
        # Example curl command
        # curl -H "Authorization: Basic ZjM4Zj...Y0MzE=" -d grant_type=refresh_token -d refresh_token=NgAagA...NUm_SHo https://accounts.spotify.com/api/token
        
        query = 'https://accounts.spotify.com/api/token'
        response = requests.post(query,
                                data = {'grant_type':'refresh_token', 'refresh_token':self.refresh_token}, # body parameters
                                headers = {'Authorization': 'Basic ' + self.base_64}) # header parameter

        response_json = response.json()
        return response_json['access_token']