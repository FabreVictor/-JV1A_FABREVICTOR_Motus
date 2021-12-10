from colorama import init
init()
from colorama import Fore, Back, Style


import random
listemot =["majors","ziguai", "rassis", "aborde", "mandat", "piegea", "alerte", "jeunai", "ululat", "salsas"] #sort un mot aleatoire dans la liste
solution = random.choice(listemot)
print(solution)

solution = "alerte"
essai = 8
mot_reponse=input(" choisir un mot de reponse en 6 lettre: \n")
affichage =""
victoire=False
lettrevalide=0


def motus( mot_reponse,essai ):
    lettrecouleur=""
    affichage=""
    for i in range (len(solution)):   #affiche couleur (ne marche pas la comparaison des deux "string fasi n'import quoi")
        if mot_reponse[i] == solution[i]:
            lettrecouleur=Back.RED+mot_reponse[i]+Back.RESET
            affichage = affichage + lettrecouleur
        else:
            if mot_reponse[i] not in solution :
                lettrecouleur=Back.BLUE+mot_reponse[i]+Back.RESET
                affichage = affichage + lettrecouleur
            else:
                lettrecouleur=Back.YELLOW+mot_reponse[i]+Back.RESET
                affichage = affichage + lettrecouleur 
    print (affichage)
    essai = essai - 1    #decompte des essai (ne marche pa sessai n'est pas un entier apparament)
    return essai

def testvictoire(affichage):
    for i in range (len(affichage)):
        if affichage[i] == affichage[i]+Back.RED+mot_reponse[i]+Back.RESET:
          lettrevalide=lettrevalide=0+1
        if lettrevalide >=6:
            victoire=True
    return victoire  

while essai > 0 or victoire == False:
    motus( mot_reponse,affichage )
    testvictoire(affichage)
    

       
