# Client ID:
# Client Secret:

# This Authorization has the scopes: 
#   playlist-modify-public 
#   playlist-modify-private

# GET request to authorize 
# https://accounts.spotify.com/authorize?client_id=(clientID)&response_type=code&redirect_uri=(URL Encoded Redirect URI)&scope=playlist-modify-public%20playlist-modify-private

# paste in terminal to get access token
# curl -H "Authorization: Basic (Base64 Encoded "clientID:clientSecret")" -d grant_type=authorization_code -d code=(Can be found after copy pasting GET request into browser) -d redirect_uri=(URL Encoded Redirect URI) https://accounts.spotify.com/api/token

base_64 = '' # Base 64 Encoded "clientID:clientSecret"
refresh_token = '' # Get from curl command
spotify_user_id = '' # Your spotify username
discover_weekly_id = '' # Discover Weekly playlist uri

