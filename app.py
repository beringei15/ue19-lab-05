import requests

def random_joke():
    """
    Récupère une blague aléatoire depuis JokesAPI.
    """
    url = "https://v2.jokeapi.dev/joke/Any"
    params = {
        "type": "single",  # On récupère des blagues d'une seule ligne
        "lang": "en",      # Langue anglaise
        "blacklistFlags": "nsfw,religious,political,racist,sexist,explicit"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Vérifie si la requête a réussi
        joke_data = response.json()
        
        # Vérifie si une blague a été reçue
        if joke_data.get("type") == "single":
            print(f"Blague : {joke_data['joke']}")
        else:
            print("Aucune blague trouvée.")
    except requests.RequestException as e:
        print(f"Erreur lors de la requête API : {e}")
    except ValueError as e:
        print(f"Erreur lors du traitement des données reçues : {e}")

if __name__ == "__main__":
    print("Voici une blague aléatoire :")
    random_joke()
