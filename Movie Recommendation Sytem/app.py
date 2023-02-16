import numpy as np
import pandas as pd
import streamlit as st
from pickle import load


movies = load(open('movie_lst.pkl', 'rb'))
similarity = load(open('similarity.pkl', 'rb'))




st.header('Movie Recommendation System')

option = st.selectbox(
    'Select movie for recommendation',
    movies.title)

if st.button('Recommend'):
        index = movies[movies['title'] == option].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x : x[1])
        for i in distances[1:6]:
            st.markdown(movies.iloc[i[0]].title)
