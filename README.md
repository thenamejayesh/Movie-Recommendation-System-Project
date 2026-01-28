

# 🎬 Movie Recommendation System

Live Project Link :https://movie-recommendation-system-project-hvdfnunybjxgw2wjwyi9pd.streamlit.app/

A **content-based Movie Recommendation System** built using **Python and Streamlit**.
The app recommends similar movies and displays their **posters** using the **TMDB API**.

---

## 🚀 Features

* 🔍 Search movie by name (no dropdown)
* 🎥 Recommends top 5 similar movies
* 🖼️ Displays movie posters
* ⚡ Fast and lightweight
* 🌐 Deployed using Streamlit Cloud
* 🧠 Uses cosine similarity for recommendations

---

## 🛠️ Tech Stack

* Python
* Pandas
* Streamlit
* Pickle
* TMDB API

---

## 📁 Project Structure

```
movie-recommendation/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

* Movie data sourced from **Kaggle**
* Preprocessed and converted into:

  * `movies.pkl`
  * `similarity.pkl`

> Dataset contains movie titles and features used to calculate similarity.

---

## 🔑 TMDB API (For Movie Posters)

This project uses **TMDB (The Movie Database) API** to fetch movie posters.

### Steps to get API key:

1. Visit : https://www.kaggle.com/datasets/ahsanaseer/top-rated-tmdb-movies-10k
2. Create an account
3. Go to **Settings → API**
4. Request **API Key (v3 auth)**

### Add API key in `app.py`:

```python
API_KEY = "your_tmdb_api_key_here"
```

---

## ▶️ How to Run Locally

1. Clone the repository

```bash
git clone https://github.com/your-username/movie-recommendation.git
cd movie-recommendation
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New App**
4. Select repository
5. Set main file as `app.py`
6. Deploy 🎉

---

## 📸 App Preview

* Enter a movie name
* Click **Recommend**
* View recommended movies with posters

* <img width="988" height="732" alt="image" src="https://github.com/user-attachments/assets/b9b9a5be-aa59-41c3-b845-ee8e185fd1b3" />


---

## ✅ Example Movies to Test

* Avatar
* Titanic
* Inception
* The Dark Knight

---

## 📌 Future Improvements

* 🔎 Auto-suggestions while typing
* 🎞️ Movie trailers
* ⭐ Ratings & filters
* 🎨 Enhanced animations and UI
* 📱 Mobile responsiveness

---

## 🙌 Acknowledgements

* Kaggle for dataset
* TMDB for movie posters
* Streamlit for deployment

---

## 📬 Contact

If you like this project or want improvements, feel free to connect!


