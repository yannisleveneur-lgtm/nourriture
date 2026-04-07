class Food:
    """ class food """
    __name = None
    __calories = None
    __fat = None
    __carbs = None
    __proteins = None

    def get_name(self):
        """ function : get the food name """
        return self.__name

    def set_name(self,name):
        """ function : set the food name """
        self.__name = name

    def get_calories(self):
        """ function : get the property named calories of the food """
        

    def set_calories(self,calories):
        """ function : set the property named calories of the food """
        

    def get_fat(self):
        """ function : get the property named fat of the food """
        

    def set_fat(self,fat):
        """ function : set the property named fat of the food """
        

    def get_carbs(self):
        """ function : get the property named carbs of the food """
        

    def set_carbs(self,carbs):
        """ function : set the property named carbs of the food """
        

    def get_proteins(self):
        """ function : get the property named proteins of the food """
    
    
    def set_proteins(self,proteins):
        """ function : get the property named proteins of the food """
        

    def retrieve_food_infos(self,food_name):
        """ function : scrap the properties of the food from a website given its name
        
        - think of making the URL a global variable
        - check whether the request succeed before trying to parse the payload
        - if not succesfull, raise an error
        
        """
        

    def display_food_infos(self):
        """ function : display the properties of the food 
        the outlook should be similar to this:
                ------------------------------------------------
                name	    calories	fat	    carbs	proteins
                tomate	    21.0		0.3	    4.6	    0.8
                ------------------------------------------------
        """
    
    

    def save_to_csv_file(self, file_name):
        """ function : save the properties of the food in a csv file 
        - use function with for file opening
        """


    def is_fat(self):
        """ function : return true or false whether the food has more than 20% of fat 
        - define a fat threshold and write the function accordingly
        """


# Exo


def retrieve_food_infos(self, food_name):
        """ function : scrap the properties of the food from a website given its name
        
        - think of making the URL a global variable
        - check whether the request succeed before trying to parse the payload
        - if not succesfull, raise an error
        """
        import requests
        from bs4 import BeautifulSoup

        self.set_name(food_name)
        GLOBAL_URL = "https://www.infocalories.fr/calories-aliments-C.php"
        
        response = requests.get(GLOBAL_URL)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.find_all('tr')
            
            for row in rows:
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 5:
                    row_name = cols[0].text.strip().lower()
                    if food_name.lower() in row_name:
                        # Fonction interne pour nettoyer le texte
                        def clean(text):
                            t = text.lower().replace(',', '.').replace('kcal', '').replace('g', '').strip()
                            return float(t) if t else 0.0
                            
                        self.set_calories(clean(cols[1].text))
                        self.set_proteins(clean(cols[2].text))
                        self.set_carbs(clean(cols[3].text))
                        self.set_fat(clean(cols[4].text))
                        return
            
            # Si on ne trouve pas l'aliment sur la page
            self.set_calories(0.0)
            self.set_proteins(0.0)
            self.set_carbs(0.0)
            self.set_fat(0.0)
        else:
            raise ConnectionError(f"La requête a échoué. Code : {response.status_code}")
        



def display_food_infos(self):
        """ function : display the properties of the food 
        the outlook should be similar to this:
                ------------------------------------------------
                name	    calories	fat	    carbs	proteins
                tomate	    21.0		0.3	    4.6	    0.8
                ------------------------------------------------
        """
        cal = self.get_calories() if self.get_calories() is not None else 0.0
        fat = self.get_fat() if self.get_fat() is not None else 0.0
        carbs = self.get_carbs() if self.get_carbs() is not None else 0.0
        prot = self.get_proteins() if self.get_proteins() is not None else 0.0
        name = self.get_name() if self.get_name() is not None else "Unknown"

        print("-" * 60)
        print(f"{'name':<15}{'calories':<12}{'fat':<10}{'carbs':<10}{'proteins':<10}")
        print(f"{name:<15}{cal:<12.1f}{fat:<10.1f}{carbs:<10.1f}{prot:<10.1f}")
        print("-" * 60)



def save_to_csv_file(self, file_name):
        """ function : save the properties of the food in a csv file 
        - use function with for file opening
        """
        import csv
        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter='\t')
            
            if file.tell() == 0:
                writer.writerow(['name', 'calories', 'fat', 'carbs', 'proteins'])
            
            writer.writerow([self.get_name(), self.get_calories(), self.get_fat(), self.get_carbs(), self.get_proteins()])



def is_fat(self):
        """ function : return true or false whether the food has more than 20% of fat 
        - define a fat threshold and write the function accordingly
        """
        FAT_THRESHOLD = 20.0 
        fat_value = self.get_fat()
        
        if fat_value is not None:
            return float(fat_value) > FAT_THRESHOLD
        return False
        
