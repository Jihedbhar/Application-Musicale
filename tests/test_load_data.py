import pandas as pd
import streamlit as st

def test_data_load():
    try:
        df = pd.read_csv('data/spotify_tracks_cleaned.csv')
        st.write("Données chargées avec succès ! Voici un aperçu des premières lignes :")
        st.write(df.head())   
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {str(e)}")

if __name__ == "__main__":
    test_data_load()