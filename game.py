
# pylint: disable=missing-docstring
import  random
import string
import requests
class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
            
    def test_empty_word_is_invalid(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Forcer la grille à un scénario de test :
        self.assertIs(new_game.is_valid('EUREKA'), True)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # S'assurer que la grille n'a pas été modifiée

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Forcer la grille à un scénario de test :
        self.assertIs(new_game.is_valid('SANDWICH'), False)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # S'assurer que la grille n'a pas été modifiée
        
    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)
    
    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']