# Automate Spotify
This program allows you to automate specific functions in Spotify using the Spotify API!

## Create a 'Discover Weekly' playlist (now you don't have to wait an entire week for new songs!)

## Create a 'Your Recommendations' playlist based on songs or artists you like!
- Personalize your recommended songs by using the get_seed function to input an artist's or track's URI
- Input the number of songs you want in your playlist from 1-100 using the recommendations function

## Find who your top artists are for the past month, past six months, or past year!
Use the find_artists function to customize the timeframe you want and the number of artists
- time_range values
    - 'short_term': one month
    - 'medium_term': six months
    - 'long_term': one year
- Input a number of artists from 1-50 (num_artists)

## Find out what your top songs are for the past month, past six months, or past year!
- Use the find_songs function to customize the timeframe you want and the number of songs
- time_range values
    - 'short_term': one month
    - 'medium_term': six months
    - 'long_term': one year
- Input a number of songs from 1-50 (num_songs)

# How to use/ set-up for yourself
- [Type up an explanation on how to set up a personal secrets file]

# Miscellaneous
## Bugs
- Recent does not seem to work 
- top_tracks function in recommend is not useful right now because recommendations function uses track_ids and artist_ids to compute recommendations, while top_tracks directly adds to the tracks

## Ideas
- put recently played songs in a playlist named 'Recently Played' if possible and not related to the playlist uri?
- mess around with returning the link to an image from a song/ playlist
- remove all liked songs by an artist from "Liked Songs" (don't think this is possible)
- add playlist picture from Discover Weekly 