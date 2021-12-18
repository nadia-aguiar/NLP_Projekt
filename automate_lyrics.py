import os
import json
import spotipy
import lyricsgenius as lg

spotify_client_id = os.environ['SPOTIPY_CLIENT_ID']
spotify_secret = os.environ['SPOTIPY_CLIENT_SECRET']
spotify_redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']
genius_access_token = os.environ['GENIUS_ACCESS_TOKEN']

scope = "user-read-currently-playing"

# Create our spotifyOAuth object
oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id,
                                    client_secret=spotify_secret,
                                    redirect_uri=spotify_redirect_uri,
                                    scope=scope)

                                    
token_dict = oauth_object.get_access_token()
token=token_dict['access_token']

#our spotify object
spotify_object = spotipy.Spotify(auth=token)

#our genius object
genius = lg.Genius(genius_access_token)

current = spotify_object.currently_playing()
#print(json.dumps(current, sort_keys=False, indent=4))

artist_name = current['item']['album']['artists'][0]['name']
song_title = current['item']['name']

song = genius.search_song(title=song_title, artist=artist_name)
lyrics=song.lyrics
lyrics_save = song.save_lyrics()
print(lyrics)
#print(json.dumps(lyrics_save))

#save_lyrics(filename=None, extension='json', overwrite=False, ensure_ascii=True, sanitize=True, verbose=True)

