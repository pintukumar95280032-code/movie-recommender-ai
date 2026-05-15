import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Page Configuration & Style
st.set_page_config(page_title="Movie AI", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #111111; color: #ffffff; }
    .stButton>button { background-color: #e50914; color: white; border-radius: 5px; border: none; }
    </style>
    """, unsafe_allow_html=True)

# 2. Helper function for API
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&append_to_response=videos"
    try:
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path')
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path if poster_path else ""
        
        trailer_link = ""
        videos = data.get('videos', {}).get('results', [])
        for video in videos:
            if video['type'] == 'Trailer' and video['site'] == 'YouTube':
                trailer_link = f"https://www.youtube.com/watch?v={video['key']}"
                break
        return full_path, data.get('vote_average'), trailer_link
    except:
        return "", 0, ""

# 3. Load Data & Calculate Similarity (NO NEED FOR similarity.pkl)
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# We calculate similarity here to avoid uploading heavy .pkl files
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vector)

# 4. App Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home / Search", "Explore by Genre"])

if page == "Home / Search":
    st.title('🎬 Movie Recommender AI')
    selected_movie = st.selectbox('Type a movie name:', movies['title'].values)

    if st.button('Get Recommendations'):
        movie_index = movies[movies['title'] == selected_movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        cols = st.columns(5)
        for i in range(5):
            m_id = movies.iloc[movies_list[i][0]].movie_id
            m_title = movies.iloc[movies_list[i][0]].title
            poster, rating, trailer = fetch_movie_details(m_id)
            with cols[i]:
                st.image(poster)
                st.write(f"**{m_title}**")
                st.caption(f"⭐ {rating}/10")
                if trailer:
                    st.video(trailer)

else:
    st.title('📂 Explore Movies by Genre')
    genre_list = ['Action', 'Adventure', 'Fantasy', 'ScienceFiction', 'Comedy', 'Drama', 'Horror']
    selected_genre = st.selectbox('Choose a Genre:', genre_list)
    
    genre_movies = movies[movies['tags'].str.contains(selected_genre.lower())].head(10)
    
    st.write(f"### Top {selected_genre} Movies:")
    grid = st.columns(5)
    for idx, row in enumerate(genre_movies.iloc[:10].itertuples()):
        poster, rating, trailer = fetch_movie_details(row.movie_id)
        with grid[idx % 5]:
            st.image(poster)
            st.write(f"**{row.title}**")
            if trailer:
                st.caption(f"[Watch Trailer]({trailer})")