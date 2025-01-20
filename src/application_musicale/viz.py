import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from application_musicale.data_loader import load_data  # Importer ta fonction de chargement de données



def genre_popularity(df):
    genre_popularity = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False)
    top_20_genres = genre_popularity.head(20)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_20_genres.index, y=top_20_genres.values, color='steelblue')  # Utilisation d'une couleur unique
    
    plt.title("Top 20 des genres musicaux les plus populaires", fontsize=14, fontweight='bold')
    plt.xlabel("Genre", fontsize=12)
    plt.ylabel("Popularité", fontsize=12)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    
    # Suppression des bordures superflues pour réduire le chartjunk
    sns.despine()
    
    # Ajout de lignes de référence pour faciliter la lecture des valeurs
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Suppression des lignes de graduation en bas et à gauche (moins d'encombrement visuel)
    plt.tick_params(left=False, bottom=False)

    plt.tight_layout()
    return plt.gcf()


def plot_most_popular_artists_by_top_genres(df):
    # Trouver les 20 genres les plus populaires
    top_20_genres = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(20).index
    df_top_genres = df[df['track_genre'].isin(top_20_genres)]
    
    # Trouver l'artiste le plus populaire pour chaque genre
    top_artists = df_top_genres.groupby(['track_genre', 'artists'])['popularity'].mean().reset_index()
    most_popular_artists = top_artists.loc[top_artists.groupby('track_genre')['popularity'].idxmax()]

    # Trier les artistes par popularité décroissante
    most_popular_artists = most_popular_artists.sort_values(by='popularity', ascending=False)
    
    # Création du graphique
    plt.figure(figsize=(14, 7))
    sns.barplot(x=most_popular_artists['track_genre'], y=most_popular_artists['popularity'], hue=most_popular_artists['artists'], dodge=False, palette='muted')
    
    plt.title("Artistes les Plus Populaires par Genre (Top 20 Genres)", fontsize=14)
    plt.xlabel("Genres Musicaux", fontsize=12)
    plt.ylabel("Popularité Moyenne", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    
    # Suppression des bordures inutiles et ajustement de la légende
    sns.despine()
    plt.legend(title="Artistes", bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=10, frameon=False)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    return plt.gcf()







def plot_duration_vs_popularity(df):
    df['duration_sec'] = df['duration_ms'] / 1000
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='duration_sec', y='popularity', color='blue', alpha=0.5, s=40, edgecolor=None)
    
    plt.title('Relation entre la Durée des Morceaux et la Popularité', fontsize=14)
    plt.xlabel('Durée des Morceaux (sec)', fontsize=12)
    plt.ylabel('Popularité', fontsize=12)
    
    sns.despine()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    return plt.gcf()

def plot_energy_by_genre(df):
    genre_energy = df.groupby('track_genre').agg({'energy': 'mean', 'popularity': 'mean'})
    top_50_genres = genre_energy.sort_values(by='popularity', ascending=False).head(50)
    top_50_genres = top_50_genres.sort_values(by='energy', ascending=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_50_genres.index, y=top_50_genres['energy'], palette='magma')
    
    plt.title("Énergie Moyenne des 50 Genres Musicaux les Plus Populaires", fontsize=14)
    plt.xlabel("Genre", fontsize=12)
    plt.ylabel("Énergie Moyenne", fontsize=12)
    
    sns.despine()
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    return plt.gcf()

def plot_energy_vs_popularity_by_genre(df):
    # Agrégation des données par genre
    genre_data = df.groupby('track_genre').agg({'energy': 'mean', 'popularity': 'mean'}).reset_index()

    # Créer le scatterplot
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='energy', y='popularity', data=genre_data, color='blue', s=100, alpha=0.7)

    # Titre et labels
    plt.title("Relation entre l'Énergie Moyenne et la Popularité Moyenne par Genre Musical", fontsize=16)
    plt.xlabel("Énergie Moyenne", fontsize=12)
    plt.ylabel("Popularité Moyenne", fontsize=12)

    # Affichage du graphique
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.grid(True)
    return plt.gcf()

def plot_danceability_vs_popularity(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='danceability', y='popularity', hue='track_genre', data=df, palette='viridis', alpha=0.5)
    plt.title("Relation entre Danseabilité et Popularité par Genre Musical")
    plt.xlabel("Danseabilité")
    plt.ylabel("Popularité")
    plt.tight_layout()
    return plt.gcf()



# Charger les données
df = load_data(r"C:\Users\Jihed B\Application_Musicale\spotify_tracks.csv")

# Visualisations
if df is not None:
    genre_popularity(df)
    plot_most_popular_artists_by_top_genres(df)
    plot_duration_vs_popularity(df)
    plot_energy_by_genre(df)
    plot_energy_vs_popularity_by_genre(df)
    plot_danceability_vs_popularity
    