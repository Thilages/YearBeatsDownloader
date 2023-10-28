# importing spotipy module since using spotify api is hard as they say
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup

# can be obtained by creating a app in spotify developers
client_id = "2f9867b0fdd147369"
client_secret = "ef51775e13e74043894"

# authenticating to the users account
user = SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri="https://example.com",scope="playlist-modify-private")
app = Spotify(auth_manager=user)
user_id = app.current_user()["id"]

user_input = input("Enter the year:")
if int(user_input)>2023:
    print("enter the year that is valuable")

# extracting data of the songs for the billboard website
else:
    website = f"https://www.billboard.com/charts/year-end/{user_input}/hot-100-songs/"
    response = requests.get(website).text
    soup = BeautifulSoup(response,"html.parser")
    songs = soup.find_all("h3",attrs={"id":"title-of-a-story"},limit=100)
    song_list = [song.getText().strip() for song in songs]

    # obtaining the uri of the searched songs
    searched_songs = []
    for song in song_list:
        result = app.search(song)
        uri = result["tracks"]["items"][0]["uri"]
        searched_songs.append(uri)

    # creating and adding the searched songs to the created playlist
    play_list = app.user_playlist_create(user_id, f"{user_input}-hitlist",public=False)
    app.playlist_add_items(play_list["id"],searched_songs)




