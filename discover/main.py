import json 
import requests
from secrets import spotify_user_id, discover_weekly_id
from datetime import date
from refresh import Refresh

class DiscoverWeekly:
    def __init__(self):
        self.user_id = spotify_user_id
        self.access_token = '' # refreshes spotify token automatically
        self.discover_weekly_id = discover_weekly_id
        self.tracks = '' # string of comma separated separated values
        self.new_playlist_id = ''
        self.cover_url = ''

    # loop through playlist tracks and add them to string (list)
    def find_songs(self):
        print('Finding songs in Discover Weekly...')
        # GET request for list of playlist's items
        query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(self.discover_weekly_id)
        response = requests.get(query,
                                headers={'Content-Type': 'application/json',
                                         'Authorization': 'Bearer {}'.format(self.access_token)})
        response_json = response.json()

        for i in response_json['items']:
            self.tracks += (i['track']['uri'] + ',')
        self.tracks = self.tracks[:-1]

        self.add_to_playlist()

    def create_playlist(self):
        print('Creating Discover Weekly playlist...')
        today = date.today()
        todayFormatted = today.strftime('%m/%d/%Y')

        # POST request to create a playlist
        query = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.user_id)
        request_body = json.dumps({
            'name': todayFormatted + ' Discover Weekly',
            'public': False,
            'description': 'Discover weekly playlist automated every week by python script'
        })

        response = requests.post(query, data=request_body, headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.access_token)
        })

        response_json = response.json()

        return response_json['id']

    def add_to_playlist(self):
        print('Adding songs...')

        self.new_playlist_id = self.create_playlist() # creates playlist and saves its id
        
        query = 'https://api.spotify.com/v1/playlists/{}/tracks?uris={}'.format(self.new_playlist_id, self.tracks)

        response = requests.post(query, headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.access_token)
        })

    # start the program by first refreshing our access token
    def start(self):
        print('Refreshing token')
        refresh_caller = Refresh()
        self.access_token = refresh_caller.refresh() # returns access token
        self.find_songs()

    def upload_playlist_cover(self):
        print('Uploading playlist cover...')

        query = 'https://api.spotify.com/v1/playlists/{}/images'.format(self.new_playlist_id)

        response = requests.get(query, headers = {
            'Content-Type': 'image/jpeg',
            'Authorization': 'Bearer {}'.format(self.access_token)
        })

        response_json = response.json()
        print(response_json)

a = DiscoverWeekly()
a.start()