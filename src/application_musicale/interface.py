import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from application_musicale.viz import genre_popularity, plot_most_popular_artists_by_top_genres, plot_duration_vs_popularity, plot_energy_by_genre, plot_energy_vs_popularity_by_genre
from application_musicale.data_loader import load_data

def main():
    # Réglage de la page pour avoir une mise en page large
    st.set_page_config(page_title="Application Musicale", page_icon="🎵", layout="wide")

    # Affichage de l'image banner.jpg
    st.image("images/banner.jpg", width=150)

    st.markdown("""
    <div style="text-align: center;">
        <h1>Bienvenue dans l'Application Musicale 🎶</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Style CSS pour personnaliser l'affichage
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
        /* Contrôler la taille des graphiques */
        .stImage img, .stPlot {
            width: 80% !important;
            height: auto !important;
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
            st.rerun()

    st.markdown('<div class="footer">© 2025 - Projet universitaire</div>', unsafe_allow_html=True)

def show_dashboard():
    df = load_data("C:/Users/Jihed B/Application_Musicale/spotify_tracks.csv")  

    if df is not None:
        st.markdown('<h2 style="text-align:center;">Dashboard</h2>', unsafe_allow_html=True)

        # Visualisations en grand format, une par ligne
        st.subheader("Popularité par genre")
        fig = genre_popularity(df)
        st.pyplot(fig)
        st.markdown("""
            Cette visualisation montre la popularité moyenne des morceaux par genre musical. 
            On peut observer quels genres dominent en termes de popularité et quels genres sont moins populaires.
                    """, unsafe_allow_html=True)

        st.subheader("Top 20 artistes les plus populaires")
        fig = plot_most_popular_artists_by_top_genres(df)
        st.pyplot(fig)
        st.markdown("""
        Ce graphique présente les 20 artistes les plus populaires. 
        Vous pouvez ainsi comparer la popularité relative des différents artistes.
        """, unsafe_allow_html=True)

        st.subheader("Durée vs Popularité")
        fig = plot_duration_vs_popularity(df)
        st.pyplot(fig)
        st.markdown("""
        Cette visualisation met en évidence la relation entre la durée des morceaux et leur popularité. 
        Vous pouvez remarquer si les morceaux plus longs ont tendance à être plus populaires ou non.
        """, unsafe_allow_html=True)

        st.subheader("Énergie moyenne par genre")
        fig = plot_energy_by_genre(df)
        st.pyplot(fig)
        st.markdown("""
        Ce graphique montre l'énergie moyenne des morceaux en fonction du genre musical. 
        Les genres plus énergiques comme l'EDM peuvent être comparés à des genres plus calmes comme le jazz.
        """, unsafe_allow_html=True)

        st.subheader("Énergie vs Popularité par Genre")
        fig = plot_energy_vs_popularity_by_genre(df)
        st.pyplot(fig)
        st.markdown("""
        Cette visualisation montre la relation entre l'énergie des morceaux et leur popularité, séparée par genre. 
        Cela peut aider à identifier les genres qui combinent une forte énergie et une grande popularité.
        """, unsafe_allow_html=True)

    else:
        st.error("Les données n'ont pas pu être chargées. Veuillez vérifier le chemin du fichier.")

if __name__ == "__main__":
    if "dashboard" not in st.session_state:
        st.session_state.dashboard = False
    main()
