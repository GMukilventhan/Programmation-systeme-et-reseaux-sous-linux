import re

while True:
    phone_number = input("Saisir FIN ou un N° de Téléphone 1er chiffre zéro les suivants sont entre 0 et 9. attention possiblilité -,.,ou en blanc:")
    if phone_number.upper() == "FIN":
        print("Au revoir")
        break
    elif re.match(r"^0[0-9]([-. ]?[0-9]{2}){4}$", phone_number):
        print("La saisie est valide")
    else:
        print("La saisie n'est pas valide.")
