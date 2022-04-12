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
        self.artist_ids = ''
        self.track_ids = ''
        # self.seed_names = []

    def get_seed(self, uri):
        ('Getting song or artist seed...')
        x = uri.split(':')
        if x[1] == 'artist':
            self.artist_ids += x[2] + ','
        elif x[1] == 'track':
            self.track_ids += x[2] + ','
            
    
    def get_track_name(self):
        query = 'https://api.spotify.com/v1/me/top/{}'.format('tracks')
        
        response = requests.get(query, 
                                headers={'Content-Type':'application/json', 
                                        'Authorization':'Bearer {}'.format(self.access_token)},
                                params={'time_range':time_range,
                                        'limit':5}) 

    # option to use top tracks as the inputs for recs 
    # time_range: short_term (4 weeks), medium_term(6 months), long_term(1 year)
    def top_tracks(self, time_range):
        print('Getting your top tracks...')
        query = 'https://api.spotify.com/v1/me/top/{}'.format('tracks')
        
        response = requests.get(query, 
                                headers={'Content-Type':'application/json', 
                                        'Authorization':'Bearer {}'.format(self.access_token)},
                                params={'time_range':time_range,
                                        'limit':5}) 
        
        response_json = response.json()
        for i in response_json['items']:
            self.tracks += i['uri'] + ','
        self.tracks = self.tracks[:-1]

    # num_songs: 1-100
    def recommendations(self, num_songs):
        ('Getting recommendations...')
        query = 'https://api.spotify.com/v1/recommendations'

        response = requests.get(query, 
                                headers={'Content-Type':'application/json', 
                                        'Authorization':'Bearer {}'.format(self.access_token)},
                                params={'limit': num_songs,
                                        # up to 5 seed values 
                                        'seed_artists': self.artist_ids,
                                        'seed_tracks': self.track_ids,})  
        
        response_json = response.json()
        for i in response_json['tracks']:
            self.tracks += i['uri'] + ','
        self.tracks = self.tracks[:-1]

    def create_playlist(self):
        print('Creating Recommendations playlist...')

        # POST request to create a playlist
        query = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.user_id)
        # seed_names = ''.join(self.seed_names)
        request_body = json.dumps({
            'name': 'Your Recommendations', 
            'public': False,
            'description': 'Suggested for songs for you!' # based on ' + seed_names + '!'
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

a = TopTracks()
a.start()
a.get_seed('spotify:artist:4V8LLVI7PbaPR0K2TGSxFF')
a.get_seed('spotify:track:1zoTGEJRVGu0XP7aC9LF0t')
a.recommendations(10)
a.add_to_playlist()