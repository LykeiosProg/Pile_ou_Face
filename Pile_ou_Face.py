import random


for piece in range(1):
    Pile = 1
    Face = 2
    piece = random.randint(1, 2)
    if piece == 1:
        print("Pile")
    elif piece == 2:
        print("Face")
while True:
    reponse = input("Voulez-vous rejouer ou vous arrêter ? Tapez \"O\" pour rejouer ou \"N\" pour arrêter.")

    if reponse.upper() == "N":
        print("Partie terminée.")
        exit()
        break
    elif reponse.upper() == "O":
        print("Nouvelle partie.")
        for piece in range(1):
            Pile = 1
            Face = 2
            piece = random.randint(1, 2)
            if piece == 1:
                print("Pile")
            elif piece == 2:
                print("Face")
        

    else:
        print("Veuillez choisir entre \"O\" pour rejouer ou \"N\" pour arrêter.")


    
        
        
