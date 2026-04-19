"""
Application Flask pour afficher les informations nutritionnelles.
Ce script sert de serveur web pour l'interface utilisateur.
"""

from flask import Flask, render_template, request
from food import Aliment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la page d'accueil et traite la recherche d'aliment."""
    aliment_data = None
    erreur = None

    if request.method == 'POST':
        # On récupère le nom tapé par l'utilisateur dans le formulaire
        nom_saisi = request.form.get('food_name')
        if nom_saisi:
            try:
                # On utilise ta classe Aliment pour scraper les infos
                mon_aliment = Aliment()
                mon_aliment.recuperer_infos_aliment(nom_saisi)
                aliment_data = mon_aliment
            except ValueError:
                erreur = f"Désolé, l'aliment '{nom_saisi}' n'a pas été trouvé."
            except Exception as e: # pylint: disable=broad-except
                erreur = f"Une erreur technique est survenue : {e}"

    return render_template('index.html', aliment=aliment_data, erreur=erreur)

if __name__ == '__main__':
    # Lance le serveur sur http://127.0.0.1:5000
    app.run(debug=True)