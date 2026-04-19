import unittest
import os
from food import Aliment

class TestFood(unittest.TestCase):
    """ class test food """

    def test_get_nom(self):
        """ Teste l'assignation et la récupération du nom """
        print('test_get_nom')
        food_one = Aliment()
        food_two = Aliment()

        food_two.set_nom('coconut')

        self.assertEqual(food_one.get_nom(), None)
        self.assertEqual(food_two.get_nom(), 'coconut')

    def test_valeurs_nutritionnelles(self):
        """ Teste les getters et setters des nutriments """
        print('test_valeurs_nutritionnelles')
        mon_aliment = Aliment()
        
        # On simule l'ajout de données
        mon_aliment.set_calories(150.5)
        mon_aliment.set_proteines(5.0)
        mon_aliment.set_glucides(20.0)
        mon_aliment.set_lipides(3.5)

        # On vérifie qu'elles sont bien retenues
        self.assertEqual(mon_aliment.get_calories(), 150.5)
        self.assertEqual(mon_aliment.get_proteines(), 5.0)
        self.assertEqual(mon_aliment.get_glucides(), 20.0)
        self.assertEqual(mon_aliment.get_lipides(), 3.5)

    def test_recuperer_infos_aliment(self):
        """ Teste la fonction de scraping avec un vrai aliment """
        print('test_recuperer_infos_aliment')
        mon_aliment = Aliment()
        
        # On teste avec la tomate
        mon_aliment.recuperer_infos_aliment('tomate')
        
        # On vérifie que le nom est bon et que les calories ont été trouvées (> 0)
        self.assertEqual(mon_aliment.get_nom(), 'tomate')
        self.assertTrue(mon_aliment.get_calories() > 0.0)

    def test_sauvegarder_dans_csv(self):
        """ Teste la création du fichier CSV """
        print('test_sauvegarder_dans_csv')
        mon_aliment = Aliment()
        mon_aliment.set_nom('aliment_test')
        mon_aliment.set_calories(100.0)
        
        nom_fichier_test = "test_temporaire.csv"
        
        # On sauvegarde
        mon_aliment.sauvegarder_dans_csv(nom_fichier_test)
        
        # On vérifie que le fichier a bien été créé physiquement sur l'ordinateur
        self.assertTrue(os.path.exists(nom_fichier_test))
        
        # On nettoie en supprimant le faux fichier après le test
        if os.path.exists(nom_fichier_test):
            os.remove(nom_fichier_test)

if __name__ == '__main__':
    unittest.main()