import random
import string

def generer_mdp(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mdp = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mdp

longueur = int(input("Longueur du mot de passe : "))
print(f"Mot de passe généré : {generer_mdp(longueur)}")