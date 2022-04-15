# Automate Spotify
This program allows you to create 'Discover Weekly', 'Your Recommendations', and 'Your Top 1-50 Songs' playlists and find out your top 1-50 listened to artists whenever you want using the Spotify API!

## How to use/ set-up for yourself
NOTE: Unfortunately, the Spotify API documentation and authorization method has changed since I coded this program, so it's not currently possible to set up the secrets file for personal use. In the future, I really hope to learn some js to update the authorization method and turn this little project into an actual website though!
- If for whatever reason you're still interested in this project, the method I used to code this is from Euan Morgan, using this video: https://youtu.be/-FsFT6OwE1A

## Functions
### Create a 'Discover Weekly' playlist (now you don't have to wait an entire week for new songs!)

### Create a 'Your Recommendations' playlist based on songs or artists you like!
- Personalize your recommended songs by using the get_seed function to input an artist's or track's URI
- Input the number of songs you want in your playlist from 1-100 using the recommendations function

### Find who your top artists are for the past month, past six months, or past year!
Use the find_artists function to customize the timeframe you want and the number of artists
- time_range values
    - 'short_term': one month
    - 'medium_term': six months
    - 'long_term': one year
- Input a number of artists from 1-50 (num_artists)

### Find out what your top songs are for the past month, past six months, or past year!
- Use the find_songs function to customize the timeframe you want and the number of songs
- time_range values
    - 'short_term': one month
    - 'medium_term': six months
    - 'long_term': one year
- Input a number of songs from 1-50 (num_songs)

## Miscellaneous
### Bugs
- top_tracks function in recommend is not an option to use right now because recommendations function uses track_ids and artist_ids to compute recommendations, while top_tracks directly adds to the tracks