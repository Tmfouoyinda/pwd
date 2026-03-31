import random
import string


class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length

    def generate_password(self):
        print(f"Le mot de passe que vous souhaitez génerer contiendra {self.length} caractères aléatoires.", )
        print(f"Longueur du mot de passe {self.length}. Entrez une nouvelle valeur ou appuyez la touche Entrée.",)
        choice = input("")

        while True:
            try :

                if choice == '':
                    choice = 0

                choice = int(choice)
                break
            except ValueError:
                print("Le nombre n'est pas valide")
                continue

        characters = string.ascii_letters + string.digits + string.punctuation
        pwd = ''.join(random.choice(characters) for _ in range(self.length))
        print(pwd)
        return pwd

    def set_password(self, length):
        self.length = length

if __name__ == "__main__":
    pwd = PasswordGenerator(12)
    password = pwd.generate_password()
