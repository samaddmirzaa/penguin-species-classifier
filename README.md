# 🐧 Penguin Species Classifier

An interactive machine learning web app that predicts penguin species based on 
physical measurements. Built with Random Forest and deployed with Streamlit.

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://faa7vlfa7wwhtnqz4kgjrs.streamlit.app)

## What it does

The app takes physical measurements of a penguin as input and predicts whether 
it is an Adelie, Chinstrap, or Gentoo penguin — along with the probability of 
each species.

## Input Features

| Feature | Description |
|---|---|
| Island | Island where the penguin was observed |
| Bill Length (mm) | Length of the penguin's bill |
| Bill Depth (mm) | Depth of the penguin's bill |
| Flipper Length (mm) | Length of the flipper |
| Body Mass (g) | Body weight in grams |
| Sex | Male or female |

## How it works

1. User adjusts the input sliders and dropdowns in the sidebar
2. Input is combined with the training data and one-hot encoded
3. A Random Forest Classifier is trained on the Palmer Penguins dataset
4. The model predicts the species and returns probabilities for all three classes

## Tech Stack

- Python
- Streamlit
- Scikit-learn (Random Forest Classifier)
- Pandas
- NumPy

## Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Dataset

[Palmer Penguins Dataset](https://github.com/dataprofessor/data/blob/master/penguins_cleaned.csv)
— a popular alternative to the Iris dataset for classification tasks, containing 
measurements of three penguin species across three Antarctic islands.
