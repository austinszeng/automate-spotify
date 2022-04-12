import json, requests 
from secrets import user_id
from refresh import Refresh 
import datetime

# make a new playlist and fill it with the top tracks for (every) year/ month/ week/ day
class TopArtists:
    def __init__(self):
        self.user_id = user_id
        self.new_playlist_id = ''
        self.artists = []
        self.access_token = ''
        self.time_range = ''

    # num_songs: 1-50
    # time_range: short_term (4 weeks), medium_term(6 months), long_term(1 year)
    def find_artists(self, time_range, num_artists):
        print('Getting your top artists...')
        query = 'https://api.spotify.com/v1/me/top/{}'.format('artists')
        
        response = requests.get(query, 
                                headers={'Content-Type':'application/json', 
                                        'Authorization':'Bearer {}'.format(self.access_token)},
                                params={'time_range':time_range,
                                        'limit':num_artists}) 
        
        response_json = response.json()
        for i in response_json['items']:
            self.artists.append(i['name'])

        return time_range

    def create_list(self):
        num_artists = str(len(self.artists))
        if self.time_range == 'short_term':
            print('Your top ' + num_artists + ' artists over the past month!\n')
        if self.time_range == 'medium_term':
            print('Your top ' + num_artists + ' artists over the past 6 months!\n')
        if self.time_range == 'long_term':
            print('Your top ' + num_artists + ' artists over the past year!\n')
        j = 1
        for i in self.artists:
            print(str(j) + '. ' + i) # also display most played song of theirs
            j += 1

    def start(self):
        print('Refreshing token...')
        refreshCaller = Refresh()
        self.access_token = refreshCaller.refresh()
        self.time_range = self.find_artists('short_term', 10)

a = TopArtists()
a.start()
a.create_list()