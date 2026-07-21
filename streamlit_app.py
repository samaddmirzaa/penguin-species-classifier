import streamlit as st
import numpy as np
import pandas as pd

st.title('🤖 Machine Learning App')

st.write('This app is a Mahcine Learning model.')

with st.expander('Data'):
  st.write('**Raw Data**')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
df

st.write('**X**')
X = df.drop(columns='species')
X

st.write('**y**')
y = df.species
y
