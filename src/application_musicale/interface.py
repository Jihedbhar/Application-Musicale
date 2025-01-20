import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from application_musicale.viz import genre_popularity, plot_most_popular_artists_by_top_genres, plot_duration_vs_popularity, plot_energy_by_genre, plot_energy_vs_popularity_by_genre
from application_musicale.data_loader import load_data

def main():
    st.set_page_config(page_title="Application Musicale", page_icon="🎵", layout="wide")

    # En-tête avec un fond personnalisé
    st.markdown(""" 
        <style>
        .header {
            background-color: #4CAF50;
            padding: 40px;
            border-radius: 8px;
            text-align: center;
            color: white;
            width: 100%;
        }
        .intro {
            font-size: 1.4em;
            color: #ffefdb;
            text-align: center;
            margin: 20px 0;
        }
        .footer {
            font-size: 0.9em;
            text-align: center;
            color: #888;
            margin-top: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header"><h1>Bienvenue dans l\'Application Musicale 🎶</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="intro">Découvrez les tendances musicales et maximisez vos ventes grâce à l\'analyse des données.</div>', unsafe_allow_html=True)

    if "dashboard" in st.session_state and st.session_state.dashboard:
        show_dashboard()
    else:
        st.markdown('<div class="intro">Cliquez ci-dessous pour accéder au dashboard.</div>', unsafe_allow_html=True)
        if st.button("Voir le dashboard"):
            st.session_state.dashboard = True
            st.experimental_rerun()

    st.markdown('<div class="footer">© 2025 - Projet universitaire</div>', unsafe_allow_html=True)

def show_dashboard():
    df = load_data("C:/Users/Jihed B/Application_Musicale/spotify_tracks.csv")  

    if df is not None:
        st.markdown('<h2 style="text-align:center;">Dashboard</h2>', unsafe_allow_html=True)

        # 1. Popularité par genre
        st.subheader("Popularité par genre")
        st.pyplot(genre_popularity(df))
        st.markdown("""
            <p style="color: #f4f4f4;">Cette visualisation montre que le pop-film, k-pop, chill sont les genres les plus populaires.</p>
        """, unsafe_allow_html=True)

        # 2. Top 20 artistes les plus populaires
        st.subheader("Top 20 artistes les plus populaires")
        st.pyplot(plot_most_popular_artists_by_top_genres(df))
        st.markdown("""
            <p style="color: #f4f4f4;">Ce graphique présente les 20 artistes les plus populaires basés sur la moyenne de la popularité de leurs morceaux.
            Les artistes les plus populaires peuvent servir de références pour des collaborations ou des recommandations marketing.</p>
        """, unsafe_allow_html=True)

        # 3. Durée vs Popularité
        st.subheader("Durée vs Popularité")
        st.pyplot(plot_duration_vs_popularity(df))
        st.markdown("""
            <p style="color: #f4f4f4;">Cette analyse explore la relation entre la durée des morceaux et leur popularité.
            On peut ainsi observer si les morceaux plus courts sont plus tendance auprès des auditeurs.</p>
        """, unsafe_allow_html=True)

        # 4. Énergie moyenne par genre
        st.subheader("Énergie moyenne par genre")
        st.pyplot(plot_energy_by_genre(df))
        st.markdown("""
            <p style="color: #f4f4f4;">Ce graphique affiche l'énergie moyenne des morceaux selon les genres.
            Les genres avec une forte énergie sont generalement associés à des ambiances plus dynamiques.</p>
        """, unsafe_allow_html=True)

        # 5. Énergie vs Popularité par Genre
        st.subheader("Énergie vs Popularité par Genre")
        st.pyplot(plot_energy_vs_popularity_by_genre(df))
        st.markdown("""
            <p style="color: #f4f4f4;">Cette visualisation montre la corrélation entre l'énergie des morceaux et leur popularité.
            Il y'a une corrélation positive faible qui suggère que les morceaux plus énergiques sont préférés par le public.</p>
        """, unsafe_allow_html=True)

        
    else:
        st.error("Les données n'ont pas pu être chargées. Veuillez vérifier le chemin du fichier.")

if __name__ == "__main__":
    if "dashboard" not in st.session_state:
        st.session_state.dashboard = False
    main()
