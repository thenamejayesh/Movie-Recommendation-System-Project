import streamlit as st
import pickle
import pandas as pd

# 1. Load your provided files
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 2. Function to recommend movies based on user input
def recommend(movie_name):
    # Standardize input to handle case sensitivity
    movie_name = movie_name.strip()
    
    try:
        # Find the index of the movie entered by the user
        movie_index = movies[movies['title'].str.lower() == movie_name.lower()].index[0]
        distances = similarity[movie_index]
        
        # Get the top 5 most similar movies (excluding the movie itself)
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        recommended_posters = []
        
        for i in movies_list:
            # Get the title and poster link for each recommended movie
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_posters.append(movies.iloc[i[0]].poster)
            
        return recommended_movies, recommended_posters
    except IndexError:
        return None, None

# 3. Streamlit User Interface
st.title('Movie Recommendation System')

# Replaced selectbox with text_input for free typing
user_input = st.text_input('Type a movie name (e.g., Avatar, Spectre):')

if st.button('Recommend'):
    if user_input:
        names, posters = recommend(user_input)
        
        if names:
            # Display results in columns
            cols = st.columns(5)
            for idx, col in enumerate(cols):
                with col:
                    st.text(names[idx])
                    # Displays the poster from the link in your CSV
                    st.image(posters[idx])
        else:
            st.error("Movie not found. Please check the spelling and try again.")
    else:
        st.warning("Please enter a movie name.")
