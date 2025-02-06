import os
import numpy as np 

# Définir le chemin relatif vers le fichier interface.py
interface_path = os.path.join("src", "application_musicale", "interface.py")

# Lancer l'application Streamlit
os.system(f"streamlit run {interface_path}")