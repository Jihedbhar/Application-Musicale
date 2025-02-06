# **Projet de TP : Analyse des Données Musicales Spotify** 🎵

Ce projet de TP vise à analyser les données musicales de Spotify afin de visualiser et interpréter diverses métriques, telles que la popularité des morceaux, des artistes et des genres. L'interface utilisateur est construite avec **Streamlit**, tandis que les visualisations sont générées à l'aide de **Seaborn** et **Matplotlib**.

---

## **Objectifs du Projet**

Ce projet permet d'explorer un jeu de données Spotify et d'obtenir des insights à travers différentes visualisations :

- 🎧 Analyse de la **popularité des morceaux**
- 🎤 Identification des **artistes les plus populaires**
- 🎵 Classement des **genres musicaux les plus populaires**
- ⏳ Étude de la **relation entre la durée des morceaux et leur popularité**
- 📊 Exploration de la **corrélation entre différentes caractéristiques audio des morceaux**

L'application utilise **Streamlit** pour une interface interactive et les bibliothèques **Seaborn/Matplotlib** pour la génération des graphiques.

---

## **Installation et Configuration**

### **1. Cloner le projet**

1. Commencez par cloner le projet sur votre machine locale :

```bash
git clone https://votre-lien-de-projet.git
cd nom_du_projet
```


2. Installer les dépendances avec Poetry
Assurez-vous d'avoir Poetry installé. Si ce n'est pas le cas, installez-le avec :

``` bash

pip install poetry
```
Ensuite, installez toutes les dépendances du projet avec :

``` bash
poetry install
```

3. Lancer l'application Streamlit
Exécutez la commande suivante pour lancer l'interface utilisateur :

```bash

python main.py
```
4. Chargement des Données

Le projet utilise un fichier CSV des morceaux Spotify. Assurez-vous que le fichier spotify_tracks_cleaned.csv est placé dans le dossier data/.
Si vous utilisez un autre fichier, mettez à jour le chemin dans le code si nécessaire.


Aperçu de l'Application
1. Page d’Accueil
La page d'accueil donne un aperçu des fonctionnalités de l'application avec des options de visualisation interactive.




2. Top 10 des Morceaux par Popularité
Un tableau présentant les morceaux les plus populaires selon leur score de popularité.



3. Top 10 des Artistes par Popularité
Un graphique affichant les artistes les plus populaires dans le dataset.



4. Top 20 des Genres Musicaux les Plus Populaires
Un classement des genres musicaux les plus populaires, visualisés sous forme de graphique.



5. Autres Visualisations
L'application propose également d'autres graphiques pour explorer les données sous différents angles.



6. Résumé et Insights Clés
Une synthèse des principales conclusions issues de l'analyse des données.


# 🎵 Projet de Visualisation Spotify  

## 🚀 Fonctionnalités  
✔️ **Visualisation interactive** des données Spotify  
✔️ **Filtrage dynamique** par **genre**, **artiste** et **popularité**  
✔️ **Affichage de statistiques descriptives** sur les morceaux  
✔️ **Comparaison des caractéristiques audio** (tempo, énergie, danseabilité...)  

---

## 🛠 Technologies Utilisées  
| Outil         | Usage |
|--------------|--------------------------------|
| 🐍 **Python 3.8+** | Langage de programmation |
| 🎨 **Streamlit** | Interface utilisateur interactive |
| 📊 **Pandas** | Manipulation et analyse des données |
| 📉 **Seaborn & Matplotlib** | Visualisation des données |
| 📦 **Poetry** | Gestion des dépendances |

---

## 🧪 Tests Unitaires  
Pour exécuter les tests, utilisez la commande suivante :  

```bash
pytest tests/
```
Auteur
Mohamed Jihed Bhar
📍 Tunis, Tunisie
✉️ jihed.bhar@dauphine.tn
