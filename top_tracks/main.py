import json, requests 
from secrets import user_id
from refresh import Refresh 
import datetime

# make a new playlist and fill it with the top tracks for (every) year/ month/ week/ day
class TopTracks:
    def __init__(self):
        self.user_id = user_id
        self.new_playlist_id = ''
        self.tracks = ''
        self.access_token = ''
        self.time_range = ''

    # num_songs: 1-50
    # time_range: short_term (4 weeks), medium_term(6 months), long_term(1 year)
    def find_songs(self, time_range, num_songs):
        print('Getting your top tracks...')
        query = 'https://api.spotify.com/v1/me/top/{}'.format('tracks')
        
        response = requests.get(query, 
                                headers={'Content-Type':'application/json', 
                                        'Authorization':'Bearer {}'.format(self.access_token)},
                                params={'time_range':time_range,
                                        'limit':num_songs}) 
        
        response_json = response.json()
        for i in response_json['items']:
            self.tracks += i['uri'] + ','
        self.tracks = self.tracks[:-1]

        return time_range

    def create_playlist(self):
        print('Creating Top Tracks playlist...')

        # POST request to create a playlist
        query = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.user_id)
        num_tracks = str(self.tracks.count(',') + 1)
        request_body = ''
        if self.time_range == 'short_term':
            request_body = json.dumps({
                'name': 'Your Top ' + num_tracks + ' Songs', 
                'public': False,
                'description': 'Your most played songs over the past month!'
            })
        elif self.time_range == 'medium_term':
            request_body = json.dumps({
                'name': 'Your Top ' + num_tracks + ' Songs', 
                'public': False,
                'description': 'Your most played songs over the past 6 months!'
            })
        elif self.time_range == 'long_term':
            request_body = json.dumps({
                'name': 'Your Top ' + num_tracks + ' Songs', 
                'public': False,
                'description': 'Your most played songs over the past year!'
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

    def start(self):
        print('Refreshing token...')
        refreshCaller = Refresh()
        self.access_token = refreshCaller.refresh()
        self.time_range = self.find_songs('short_term', 50)

a = TopTracks()
a.start()
a.add_to_playlist()