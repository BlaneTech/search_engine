# search_engine
Build a search engine using elasticsearch

# Ceci est un projet qui consistait à réaliser un moteur de recherche en utilisant elastisearch

# 1. Pour executer le code, il faut:

# 1.1 Créer un environnement virtuel.
    Positionner vous dans le repertoire du projet et lancer les commandes suivantes:

    python3 -m venv nom_de_votre_environnement_virtuel

    source nom_de_votre_environnement_virtuel/bin/activate

# 1.2 installer les dépendances:

    pip install -r requirements.txt

# 1.3 Lancer elasticsearch
## Vous devez au préalable avoir docker et docker-compose installer sur votre machine (ce n'est pas grave si vous savez pas utiliser docker. L'installion juste suufira)

## Lancer la commande suivante pour démarrer elasticsearch:

    docker-compose up

# Up le tour est jouer, il ne vous reste plus qu'à executer le fichier 
    app.py


# Penser à arrêter docker-compse après avoir fini de tester car celà consome beaucoup trop de ressource

## la commande est la suivante: 
    
    docker-compose stop