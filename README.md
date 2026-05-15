# 🎬 Movie Recommender AI (Lightweight & Pro)

A high-performance ❯ Machine Learning ❮ web application that recommends movies with precision. This version is specifically optimized for cloud deployment by using on-the-fly computation, making it fast and storage-efficient.

## 🚀 Key Features
- [ Intelligent Recommendation ] : Suggests movies similar to your favorites using NLP and Cosine Similarity.
- [ Optimized Deployment ] : No need for heavy `.pkl` or `.csv` files. Similarity is computed dynamically to save space.
- [ Real-time Media ] : Fetches official posters and ratings dynamically via TMDB API.
- [ Integrated Trailers ] : Watch official movie trailers directly inside the application.
- [ Genre Discovery ] : Explore top movies across categories like Action, Comedy, and Sci-Fi.
- [ Premium UI ] : A sleek, Netflix-inspired Dark Mode interface built with Streamlit.

## 🛠️ Tech Stack
- [ Language ] : Python 3.10+
- [ Machine Learning ] : Scikit-learn (CountVectorizer, Cosine Similarity)
- [ Data Handling ] : Pandas, Numpy, Pickle
- [ Frontend ] : Streamlit
- [ API ] : The Movie Database (TMDB)

## 📁 Project Structure (Optimized)
- ➔ app.py: The main application logic with real-time vectorization.
- ➔ movie_recommender.ipynb: Full documentation of data cleaning and model building.
- ➔ movie_dict.pkl: Compact movie dataset for quick loading.
- ➔ requirements.txt: Essential libraries for seamless cloud hosting.

## ⚙️ How to Run Locally
1. Clone this repository.
2. Install dependencies: 
   `pip install -r requirements.txt`
3. Launch the app: 
   `streamlit run app.py`

## 📊 Data Source
The model is trained on the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

---
Developed by ❯ Pintu Kumar ❮ | Final Year B.Tech CSE | Mangalayatan University
