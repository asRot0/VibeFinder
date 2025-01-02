import pandas as pd
import numpy as np
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.metrics.pairwise import cosine_similarity

# Spotify API credentials
CLIENT_ID = "spotify client id"
CLIENT_SECRET = "spotify client secret"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load dataset and preprocessed features
data_path = 'data/cleaned_spotify_million_songs.csv'
features_path = 'data/preprocessed_features.npy'
data = pd.read_csv(data_path)
features = np.load(features_path)


# Get album cover URL from Spotify
def get_album_cover(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    if results and results["tracks"]["items"]:
        return results["tracks"]["items"][0]["album"]["images"][0]["url"]
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"  # Placeholder image


# Recommend songs
def recommend_songs(song_title, data, features, start_index=0, count=5):
    try:
        song_idx = data[data['song'] == song_title].index[0]
        similarity_scores = cosine_similarity([features[song_idx]], features)[0]
        similar_indices = similarity_scores.argsort()[::-1][1:]

        # Limit recommendations to start_index and count
        recommendations = []
        album_covers = []
        for idx in similar_indices[start_index:start_index + count]:
            artist = data.iloc[idx]['artist']
            song = data.iloc[idx]['song']
            recommendations.append(song)
            album_covers.append(get_album_cover(song, artist))

        return recommendations, album_covers
    except IndexError:
        return f"Song '{song_title}' not found in the dataset.", []
    except Exception as e:
        return f"An error occurred: {str(e)}", []


# Streamlit UI
st.title("🎵 VibeFinder\n Music Recommendation System")
st.markdown("Discover songs similar to your favorites, along with their album covers!")

# Song selection dropdown
song_list = data['song'].values
selected_song = st.selectbox("Select a Song:", song_list)

# Reset rows if the selected song changes
if "prev_selected_song" not in st.session_state or st.session_state.prev_selected_song != selected_song:
    st.session_state.prev_selected_song = selected_song
    st.session_state.start_index = 0
    st.session_state.recommendation_rows = []

# Show Recommendations
if st.button("Show Recommendations"):
    recommendations, covers = recommend_songs(selected_song, data, features, st.session_state.start_index, 5)
    if isinstance(recommendations, list):
        # Save the new row in session state
        st.session_state.recommendation_rows.append((recommendations, covers))
        st.session_state.start_index += 5

# Display all rows
for recommendations, covers in st.session_state.recommendation_rows:
    cols = st.columns(5)
    for i, col in enumerate(cols):
        if i < len(recommendations):
            with col:
                st.text(recommendations[i])
                st.image(covers[i])

# More button to add additional rows
if st.session_state.start_index < len(data):
    if st.button("More"):
        recommendations, covers = recommend_songs(selected_song, data, features, st.session_state.start_index, 5)
        if isinstance(recommendations, list):
            st.session_state.recommendation_rows.append((recommendations, covers))
            st.session_state.start_index += 5
