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

with st.expander('Data Visualisation'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# Data Preparation
with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island', ('Bisco', 'Dream', 'Torgersen'))
  gender = st.selectbox('Gender', ('male', 'female'))
  bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.6, 43.9)
