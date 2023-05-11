import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd

username = 'Paulo Oyama'
auth_manager = SpotifyClientCredentials()
connection = spotipy.Spotify(auth_manager=auth_manager)

scope = 'user-library-read playlist-modify-public playlist-read-private'

token = util.prompt_for_user_token(username,scope)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

sourcePlaylistID = 'https://open.spotify.com/playlist/37i9dQZF1EpuFo9vaSxlPo'
sourcePlaylist = sp.user_playlist(username, sourcePlaylistID)
tracks = sourcePlaylist["tracks"]
songs = tracks["items"]

track_ids = []
track_names = []

for i in range(0, len(songs)):
    if songs[i]['track']['id'] != None: # Removes the local tracks in your playlist if there is any
        track_ids.append(songs[i]['track']['id'])
        track_names.append(songs[i]['track']['name'])

features = []
for i in range(0,len(track_ids)):
    audio_features = sp.audio_features(track_ids[i])
    for track in audio_features:
      
      if track is None:
        print(track)
        features.append({'danceability': 0, 'energy': 0, 'key': 0, 'loudness': 0, 'mode': 0, 'speechiness': 0, 'acousticness': 0, 'instrumentalness': 0, 'liveness': 0, 'valence': 0, 'tempo': 0, 'type': 'audio_features', 'id': '00000', 'uri': 'spotify:track:0', 'track_href': 'https://api.spotify.com/', 'analysis_url': 'https://api.spotify.com/', 'duration_ms': 0, 'time_signature': 0})
      else:
        features.append(track)
print(track_ids)
print()
print(track_names)
print()
print(features)
# echo "# RecommendationApp" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
#git remote add origin https://github.com/PauloOyama/RecommendationApp.git
# git push -u origin main
playlist_df = pd.DataFrame(features, index = track_names)