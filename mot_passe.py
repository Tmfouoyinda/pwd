import secrets
import string

long = int(input("Longueur du mdp : "))

if long <= 4:
    print("Il faut minimum 4 caracteres ")
    exit()

mdp = [
    secrets.choice(string.ascii_lowercase),secrets.choice(string.ascii_uppercase),
    secrets.choice(string.digits),secrets.choice(string.punctuation),
]

#complet
caracteres = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
)


for i in range(long - 4):
    mdp.append(secrets.choice(caracteres))

secrets.SystemRandom().shuffle(mdp)
print("Mot de passe Ultra-securise:")
print("".join(mdp))
