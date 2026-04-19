"""
Module de tests unitaires pour la classe Aliment.
Vérifie le cycle de vie de l'objet : nommage, nutriments, scraping et export.
"""

import unittest
import os
from food import Aliment

class TestFood(unittest.TestCase):
    """Suite de tests pour valider l'intégrité des données de la classe Aliment."""

    def test_get_nom(self):
        """Vérifie que le nom est correctement assigné et récupéré."""
        food_one = Aliment()
        food_two = Aliment()

        food_two.set_nom('coconut')

        self.assertEqual(food_one.get_nom(), None)
        self.assertEqual(food_two.get_nom(), 'coconut')

    def test_valeurs_nutritionnelles(self):
        """Vérifie le stockage des flottants pour les calories et macronutriments."""
        mon_aliment = Aliment()
        
        mon_aliment.set_calories(150.5)
        mon_aliment.set_proteines(5.0)
        mon_aliment.set_glucides(20.0)
        mon_aliment.set_lipides(3.5)

        self.assertEqual(mon_aliment.get_calories(), 150.5)
        self.assertEqual(mon_aliment.get_proteines(), 5.0)
        self.assertEqual(mon_aliment.get_glucides(), 20.0)
        self.assertEqual(mon_aliment.get_lipides(), 3.5)

    def test_recuperer_infos_aliment(self):
        """Vérifie que le scraping sur 'tomate' retourne des données cohérentes."""
        mon_aliment = Aliment()
        mon_aliment.recuperer_infos_aliment('tomate')
        
        self.assertEqual(mon_aliment.get_nom(), 'tomate')
        self.assertGreater(mon_aliment.get_calories(), 0.0)

    def test_sauvegarder_dans_csv(self):
        """Vérifie la création effective du fichier CSV sur le système de fichiers."""
        mon_aliment = Aliment()
        mon_aliment.set_nom('test_unitaire')
        mon_aliment.set_calories(10.0)
        
        nom_temp = "test_temporaire.csv"
        
        # Action de sauvegarde
        mon_aliment.sauvegarder_dans_csv(nom_temp)
        
        # Assertion sur l'existence du fichier
        existe = os.path.exists(nom_temp)
        self.assertTrue(existe)
        
        # Nettoyage
        if existe:
            os.remove(nom_temp)

if __name__ == '__main__':
    unittest.main()