from food import Aliment
import argparse
import sys

print("Running script...")

parser = argparse.ArgumentParser("Food Informations")
parser.add_argument('-f', '--food', help="your food name", default='tomate')

# Récupération de l'argument tapé dans le terminal
args = parser.parse_args()
food_name = args.food

# Instanciation de l'objet Food
mon_aliment = Aliment()

try:
    print(f"Recherche des informations pour : '{food_name}'...")

    # Récupération et affichage des données (NOMS CORRIGÉS)
    mon_aliment.recuperer_infos_aliment(food_name)
    mon_aliment.afficher_infos_aliment()

    # Sauvegarde dans le fichier CSV (NOM CORRIGÉ)
    fichier_csv = "historique_aliments.csv"
    mon_aliment.sauvegarder_dans_csv(fichier_csv)
    print(f" Informations sauvegardées avec succès dans '{fichier_csv}'.")

except Exception as e:
    # Gestion des erreurs si l'aliment n'est pas trouvé
    print(f"\n {e}")
    sys.exit(1)