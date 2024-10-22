import sys


LISTE = []

MENU = """Choisissez parmis les 5 options suivantes : 
1: Ajouter un élément à la liste: 
2: Retirer un élément à la liste: 
3: Afficher la liste 
4: Vider la liste 
5: Quitter 
👉 Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    userInput = input(MENU)

    if userInput not in MENU:
        print("Veuillez entrer un nombre entre 1 et 5")
        continue

    if userInput == "1":
        customer_choice = input(
            "Entrez le nom d'un élément à ajouter à la liste de courses: ")
        LISTE.append(customer_choice)
        print(f"L'élément {
            customer_choice} à bien été ajouté à la liste.")
    elif userInput == "2":
        customer_choice = input("Entrez le nom d'un élément à retirer: ")
        if customer_choice in LISTE:
            LISTE.remove(customer_choice)
            print(f"L'élément {
                customer_choice} à bien été retiré de la liste.")
        else:
            print(f"L'élement {
                customer_choice} ne figure pas dans votre liste.")
    elif userInput == "3":
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, element in enumerate(LISTE, 1):
                print(f"{i}/ {element}")
        else:
            print("Votre liste ne contient aucun élément.")
    elif userInput == "4":
        LISTE.clear()
        print("La liste à été vidée de son contenu.")
    elif userInput == "5":
        print("A bientôt !")
        sys.exit()

    print("-" * 50)
