import json, requests 
from secrets import spotify_user_id, playlist_id
from refresh import Refresh 

class RecentlyPlayed:
    def __init__(self):
        self.spotify_user_id = spotify_user_id
        self.playlist_id = playlist_id 
        self.tracks = ''
        self.access_token = ''

    def find_songs(self):
        print('Finding recently played songs...')

        query = 'https://api.spotify.com/v1/me/player/recently-played'

        response = requests.get(query, 
                                headers={'Content-Type':'application/json', 
                                        'Authorization':'Bearer {}'.format(self.access_token)},
                                params={'limit':50})

        response_json = response.json()

        for i in response_json['items']: 
            self.tracks += i['track']['uri'] + ','
        self.tracks = self.tracks[:-1]
        self.replace_songs()

    def replace_songs(self):
        print('Replacings songs in your "Recently Played" playlist...')

        query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(self.playlist_id)

        response = requests.put(query, 
                                headers={'Content-Type':'application/json', 
                                        'Authorization':'Bearer {}'.format(self.access_token)},
                                params = {'uris': self.tracks})


    def start(self):
        print('Refreshing token...')
        refreshCaller = Refresh()
        self.access_token = refreshCaller.refresh()
        self.find_songs()

a = RecentlyPlayed()
a.start()
