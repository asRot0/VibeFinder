# 🎵 *`VibeFinder`*: Music Recommendation System

![Spotify Logo](https://upload.wikimedia.org/wikipedia/commons/2/26/Spotify_logo_with_text.svg)  
**Discover music that matches your vibe!**

## 🌟 **What is VibeFinder?**
VibeFinder is an intelligent music recommendation system designed to suggest songs based on your current mood or a favorite track. Using cutting-edge machine learning techniques and the Spotify Million Song Dataset, VibeFinder analyzes similarities between tracks to bring you personalized music recommendations, complete with album covers.  

---

## 🧠 **How Does It Work?**
1. **Input Selection**: Choose a song from a dropdown menu.
2. **Song Analysis**: 
   - Songs are represented as high-dimensional feature vectors derived from their audio properties (e.g., tempo, energy, danceability).
   - Cosine similarity is calculated to find tracks most similar to your selection.
3. **Recommendations**:
   - Display top recommendations in an interactive UI.
   - Optionally, preview songs (using Spotify API).

---

## 🔬 **AI/ML Techniques Used**
- **Feature Engineering**: Extraction of audio features from the dataset for similarity computation.
- **Cosine Similarity**: Measures closeness of song feature vectors.
- **Streamlit**: Deploys the app for an interactive and user-friendly interface.

### *`Cosine Similarity`*
Cosine similarity is employed to measure the similarity between the feature vectors of different songs. It calculates the cosine of the angle between two vectors, with values ranging from -1 (completely dissimilar) to 1 (completely similar).  

The formula is:
\[
\text{Cosine Similarity} = \frac{A \cdot B}{\|A\| \|B\|}
\]

Where:
- \( A \) and \( B \) are the feature vectors of two songs.
- \( A \cdot B \) is the dot product of the vectors.
- \( \|A\| \) and \( \|B\| \) are the magnitudes of the vectors.

In the context of VibeFinder:
1. A song's feature vector is compared against all other songs in the dataset.
2. Songs with the highest similarity scores are considered most similar and are recommended.

This approach ensures that the recommendations are based on the inherent musical characteristics of each track, providing a scientifically grounded and intuitive way to discover new music.

---

## 📂 **Project Structure**
```
VibeFinder/
├── data/          # Raw and processed datasets
├── notebooks/     # Jupyter notebooks for EDA and analysis
├── src/           # Python scripts for data preprocessing, modeling, and recommendations
├── reports/       # Visualizations, reports, and documentation
├── models/        # Trained ML models
├── app/           # Streamlit application code
└── requirements.txt # Dependencies
```

---

## 📊 Dataset Used
[Spotify Million Song Dataset](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)

This dataset contains song names, artists names, link to the song and lyrics. This dataset can be used for recommending songs, classifying or clustering songs.

---

## 🚀 Deploying VibeFinder
Run the App:
```
streamlit run app.py
```
- Ensure all dependencies are installed using `requirements.txt`.
- The app will run locally, and a browser window will open with the interactive interface.
