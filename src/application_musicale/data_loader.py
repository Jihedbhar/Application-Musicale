import pandas as pd

def load_data(filepath="spotify_tracks.csv"):
    """
    Charge les données depuis un fichier CSV local.
    Args:
    - filepath (str) : Le chemin vers le fichier CSV.
    
    Returns:
    - DataFrame : Le DataFrame contenant les données.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return None
    
if __name__ == "__main__":
    # Charger les données
    df = load_data("C:/Users/Jihed B/Application_Musicale/spotify_tracks.csv")  # Met le bon chemin ici

    # Afficher les 5 premières lignes
    print(df.head())