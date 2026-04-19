"""
Module gérant la classe Aliment et le scraping des données nutritionnelles.
Ce module utilise BeautifulSoup pour extraire les données depuis infocalories.fr.
"""

import csv
import re

import requests
from bs4 import BeautifulSoup

# Constante pour l'URL de base
BASE_URL = "https://www.infocalories.fr/calories/calories-"


class Aliment:
    """
    Classe représentant un aliment et ses valeurs nutritionnelles.
    Elle permet de récupérer ces valeurs via du web scraping.
    """

    def __init__(self):
        """Initialise l'objet Aliment avec des valeurs par défaut."""
        self.__nom = None
        self.__calories = 0.0
        self.__proteines = 0.0
        self.__glucides = 0.0
        self.__lipides = 0.0

    def get_nom(self):
        """Retourne le nom de l'aliment."""
        return self.__nom

    def set_nom(self, nouveau_nom):
        """Définit le nom de l'aliment."""
        self.__nom = nouveau_nom

    def get_calories(self):
        """Retourne la valeur énergétique en calories."""
        return self.__calories

    def set_calories(self, calories):
        """Définit les calories en convertissant la valeur en float."""
        self.__calories = float(calories) if calories else 0.0

    def get_proteines(self):
        """Retourne la quantité de protéines."""
        return self.__proteines

    def set_proteines(self, proteines):
        """Définit les protéines en convertissant la valeur en float."""
        self.__proteines = float(proteines) if proteines else 0.0

    def get_glucides(self):
        """Retourne la quantité de glucides."""
        return self.__glucides

    def set_glucides(self, glucides):
        """Définit les glucides en convertissant la valeur en float."""
        self.__glucides = float(glucides) if glucides else 0.0

    def get_lipides(self):
        """Retourne la quantité de lipides."""
        return self.__lipides

    def set_lipides(self, lipides):
        """Définit les lipides en convertissant la valeur en float."""
        self.__lipides = float(lipides) if lipides else 0.0

    def recuperer_infos_aliment(self, nom_aliment):
        """
        Scrape les valeurs nutritionnelles de l'aliment depuis le site web.
        """
        nom_url = nom_aliment.lower().replace(" ", "-")
        url = f"{BASE_URL}{nom_url}.php"

        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(url, headers=headers, timeout=10)

        if reponse.status_code != 200:
            raise ValueError(f"Erreur {reponse.status_code} : Page introuvable.")

        soup = BeautifulSoup(reponse.text, 'html.parser')
        self.set_nom(nom_aliment)
        texte_page = soup.get_text(separator=' ', strip=True)

        match_cal = re.search(
            r"Calories\s*[:]\s*(\d+[\.,]?\d*)", texte_page, re.IGNORECASE
        )
        val_cal = match_cal.group(1).replace(',', '.') if match_cal else 0.0
        self.set_calories(val_cal)

        def extraire_avant(label):
            """Extrait la valeur numérique située juste avant un mot-clé donné."""
            motif = rf"(\d+[\.,]?\d*)\s*g\s*(?:de\s+)?{label}"
            match = re.search(motif, texte_page, re.IGNORECASE)
            if match:
                return match.group(1).replace(',', '.')
            return 0.0

        self.set_proteines(extraire_avant("protéines"))
        self.set_glucides(extraire_avant("glucides"))
        self.set_lipides(extraire_avant("lipides"))

    def afficher_infos_aliment(self):
        """Affiche les propriétés de l'aliment dans la console."""
        barre = "-" * 65
        entete = (
            f"{'NOM':<18} {'CALORIES':<12} {'PROTÉINES':<12} "
            f"{'GLUCIDES':<12} {'LIPIDES'}"
        )

        nom_a_afficher = self.__nom if self.__nom else "Inconnu"
        donnees = (
            f"{nom_a_afficher:<18} {self.__calories:<12.1f} "
            f"{self.__proteines:<12.1f} {self.__glucides:<12.1f} "
            f"{self.__lipides:<10.1f}"
        )

        print(barre)
        print(entete)
        print(donnees)
        print(barre)

    def sauvegarder_dans_csv(self, nom_fichier):
        """Sauvegarde les informations de l'aliment dans un fichier CSV local."""
        with open(nom_fichier, mode='a', newline='', encoding='utf-8') as fichier:
            writer = csv.writer(fichier)
            writer.writerow([
                self.__nom, self.__calories, self.__proteines,
                self.__glucides, self.__lipides
            ])


if __name__ == "__main__":
    mon_aliment_test = Aliment()
    tests = ["beurre cacahuetes", "tomate", "farine patate douce"]

    for nom_test in tests:
        try:
            mon_aliment_test.recuperer_infos_aliment(nom_test)
            mon_aliment_test.afficher_infos_aliment()
        except ValueError as erreur:
            print(f"Erreur sur {nom_test} : {erreur}")