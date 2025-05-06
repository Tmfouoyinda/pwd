import random
import string

class PasswordGenerator:
    
    def __init__(self, length=12):
        self.length = length
    
    def generate(self):
        print("Le mot de passe que vous souhaitez génerer contiendra {0} caractères aléatoires.".format(self.length))
        print("Longueur du mot de passe {0}. Entrez une nouvelle valeur ou appuyez la touche Entrée.".format(self.length))
        choice = input("")
        
        if choice == '':
            choice = 0
        
        choice = int(choice)
        
        if choice != 0:
            self.set_length(choice)
        
        characters = string.ascii_letters + string.digits + string.punctuation
        pwd = ''.join(random.choice(characters) for _ in range(self.length))
        print(pwd)
        return pwd 
    def set_length(self, length):
        self.length = length

if __name__ == "__main__":
    pwd = PasswordGenerator(12)
    password = pwd.generate()
