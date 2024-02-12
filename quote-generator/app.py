from flask import Flask, render_template
import json
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Charger le contenu du fichier JSON
    with open('data.json', 'r', encoding='utf-8') as file:
        citations = json.load(file)

    # Générer un index aléatoire
    index_aleatoire = random.randint(0, len(citations) - 1)

    # Récupérer les informations à partir de l'index généré
    citation_aleatoire = citations[index_aleatoire]

    # Rendre le template HTML avec la citation aléatoire
    return render_template('index.html', citation=citation_aleatoire)

if __name__ == '__main__':
    app.run(debug=True)
