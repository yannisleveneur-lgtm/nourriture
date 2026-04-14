from food import Aliment
import argparse

import sys
print("Running script...")

parser = argparse.ArgumentParser("Food Informations")
parser.add_argument('-f', '--food', help="your food name", default='tomate')

# use the parser to get all the needed arguments
# retrieve and display food infos
# save the displayed infos to a csv file

# Récupération de l'argument tapé dans le terminal,
args = parser.parse_args()
food_name = args.food

# Instanciation de l'objet Food,
mon_aliment = Food()

try:
    print(f"Recherche des informations pour : '{food_name}'...")

# Récupération et affichage des données,
    mon_aliment.retrieve_food_infos(food_name)
    mon_aliment.display_food_infos()

# Sauvegarde dans le fichier CSV,
    fichier_csv = "historique_aliments.csv"
    mon_aliment.save_to_csv_file(fichier_csv)
    print(f" Informations sauvegardées avec succès dans '{fichier_csv}'.")

except ValueError as e:
    # Gestion des erreurs si l'aliment n'est pas trouvé
    print(f"\n {e}")
    sys.exit(1)
