import unittest
import os
from food import Aliment

class TestFood(unittest.TestCase):
    """ class test food """
    
    # --- TEST 1 : Les noms (Getters et Setters) ---
    def test_get_name(self):
        """ test_get_name """
        print('\n--- test_get_name ---')
        food_one = Aliment()
        food_two = Aliment()

        food_two.set_nom('coconut')

        self.assertEqual(food_one.get_nom(), None)
        self.assertEqual(food_two.get_nom(), 'coconut')

    # --- TEST 2 : Le scraping des lipides ---
    def test_is_fat(self):
        """ test_is_fat
        you may test 3 different foods
        """
        print('\n--- test_is_fat ---')
        food_1 = Aliment()
        food_2 = Aliment()
        food_3 = Aliment()

        food_1.recuperer_infos_aliment("tomate")
        food_2.recuperer_infos_aliment("beurre cacahuetes")
        food_3.recuperer_infos_aliment("avocat")

        # Vérifie que les lipides sont bien récupérés (ce sont des nombres à virgule)
        self.assertIsInstance(food_1.get_lipides(), float)
        self.assertIsInstance(food_2.get_lipides(), float)
        self.assertIsInstance(food_3.get_lipides(), float)
        
        # Vérifie que le beurre de cacahuète est gras (> 0)
        self.assertGreater(food_2.get_lipides(), 0.0)

    # --- TEST 3 : L'affichage en console ---
    def test_afficher_infos(self):
        """ Test de la fonction afficher_infos_aliment """
        print('\n--- test_afficher_infos ---')
        food = Aliment()
        food.set_nom("Fraise")
        food.set_calories(32)
        food.set_proteines(0.7)
        food.set_glucides(7.6)
        food.set_lipides(0.3)
        
        # On vérifie juste que l'affichage ne fait pas planter le code
        try:
            food.afficher_infos_aliment()
        except Exception as e:
            self.fail(f"L'affichage a planté avec l'erreur : {e}")

    # --- TEST 4 : La création du fichier CSV ---
    def test_sauvegarder_csv(self):
        """ Test de la fonction sauvegarder_dans_csv """
        print('\n--- test_sauvegarder_csv ---')
        food = Aliment()
        food.set_nom("Pomme")
        food.set_calories(52)
        
        fichier_test = "fichier_test_temporaire.csv"
        
        # On sauvegarde
        food.sauvegarder_dans_csv(fichier_test)
        
        # On vérifie que le fichier a bien été créé sur l'ordinateur
        self.assertTrue(os.path.exists(fichier_test))
        
        # On supprime le fichier de test pour laisser le dossier propre
        if os.path.exists(fichier_test):
            os.remove(fichier_test)

if __name__ == '__main__':
    unittest.main()