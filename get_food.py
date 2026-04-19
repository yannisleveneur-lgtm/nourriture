"""
Script de récupération des informations nutritionnelles via la ligne de commande.
Ce script utilise la classe Aliment pour scraper des données et les sauvegarder.
"""

import sys
import argparse
from food import Aliment

# Constante globale en majuscule pour respecter la PEP 8
FICHIER_HISTORIQUE = "historique_aliments.csv"

def main():
    """
    Fonction principale : gère les arguments, lance le scraping et sauvegarde.
    """
    parser = argparse.ArgumentParser(description="Recherche d'informations nutritionnelles.")
    parser.add_argument('-f', '--food', help="Nom de l'aliment à rechercher", default='tomate')

    args = parser.parse_args()
    nom_recherche = args.food

    mon_aliment = Aliment()

    try:
        print(f"Recherche des informations pour : '{nom_recherche}'...")

        # Récupération et affichage des données
        mon_aliment.recuperer_infos_aliment(nom_recherche)
        mon_aliment.afficher_infos_aliment()

        # Sauvegarde dans le fichier CSV défini en constante
        mon_aliment.sauvegarder_dans_csv(FICHIER_HISTORIQUE)
        print(f"Informations sauvegardées dans '{FICHIER_HISTORIQUE}'.")

    except ValueError as err:
        print(f"Erreur de données : {err}")
        sys.exit(1)
    except ConnectionError as err:
        print(f"Erreur de connexion réseau : {err}")
        sys.exit(1)

if __name__ == '__main__':
    main()