
username = 'hypster.'
clientID = '66ab12a5437c4a5f9558c5810ba546a5'
clientSecret = 'b7b08fce65984fb9a7cadf7bf9853c80'
redirect_uri = 'http://google.com/callback/'

import json
import spotipy
import webbrowser

redirect_uri = 'http://google.com/callback/'


oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri) 
token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user() 
  
# To print the response in readable format. 
print(json.dumps(user_name, sort_keys=True, indent=4)) 


while True: 
    print("Welcome to the project, " + user_name['display_name']) 
    print("0 - Exit the console") 
    print("1 - Search for a Song") 
    user_input = int(input("Enter Your Choice: ")) 
    if user_input == 1: 
        search_song = input("Enter the song name: ") 
        results = spotifyObject.search(search_song, 1, 0, "track") 
        songs_dict = results['tracks'] 
        song_items = songs_dict['items'] 
        song = song_items[0]['external_urls']['spotify'] 
        webbrowser.open(song) 
        print('Song has opened in your browser.') 
    elif user_input == 0: 
        print("Good Bye, Have a great day!") 
        break
    else: 
        print("Please enter valid user-input.") 