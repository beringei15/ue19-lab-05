# ue19-lab-05
# Application Python utilisant une Jokes API pour afficher une blague en Anglais

Bienvenue dans ue19-lab-05, une application Python qui interroge JokesAPI pour récupérer et afficher une blague. Ce projet est conçu pour être simple à utiliser et facilement extensible grâce à Docker.

# Fonctionnalités
Interroge JokesAPI : Utilise la bibliothèque requests pour récupérer des données de l'API et afficher la blague.
Conteneurisation avec Docker : L'application peut être exécutée dans un environnement Dockerisé, garantissant portabilité et cohérence.
Facile à installer et à utiliser : Fournit un fichier requirements.txt pour gérer les dépendances et un fichier Dockerfile pour l'intégration dans Docker.

# Prérequis

Prérequis
Assurez-vous d'avoir les éléments suivants installés :

- Python 3.8+
- Pip (le gestionnaire de paquets Python)
- Docker (optionnel, mais recommandé)

# Installation

# Étape 1 : Cloner le repository
git clone https://github.com/votre-utilisateur/ue19-lab-05.git
cd ue19-lab-05

# Étape 2 : Installer les dépendances
pip install -r requirements.txt

# Utilisation
python app.py

# Lancer l'application avec Docker
1. Construire l'image Docker :
docker build -t api-app .

2. Exécuter le conteneur :
docker run --rm api-app
