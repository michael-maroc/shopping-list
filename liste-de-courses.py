import sys

liste_de_courses = []

while True:
    userInput = input("Choisissez parmis les 5 options suivantes : \n1: Ajouter un élément à la liste: \n2: Retirer un élément à la liste: \n3: Afficher la liste \n4: Vider la liste \n5: Quitter \n👉 Votre choix : ")

    if userInput.isdigit():
        if int(userInput) == 1:
            customer_choice = input(
                "Entrez le nom d'un élément à ajouter à la liste de courses: ")
            liste_de_courses.append(customer_choice)
            print(f"L'élément {customer_choice} à bien été ajouté à la liste.")
        elif int(userInput) == 2:
            customer_choice = input("Entrez le nom d'un élément à retirer: ")
            if customer_choice in liste_de_courses:
                liste_de_courses.remove(customer_choice)
                print(f"L'élément {
                      customer_choice} à bien été retiré de la liste.")
            else:
                print("Cet élément ne figure pas dans votre liste.")
        elif int(userInput) == 3:
            if len(liste_de_courses) > 0:
                print("Voici le contenu de votre liste :")
                for i, element in enumerate(liste_de_courses):
                    i += 1
                    print(i, element)
            else:
                print("Votre liste ne contient aucun élément.")
        elif int(userInput) == 4:
            liste_de_courses.clear()
            print("La liste à été vidée de son contenu.")
        elif int(userInput) == 5:
            print("A bientôt !")
            sys.exit()
        elif int(userInput) <= 0 or int(userInput) > 5:
            print("Veuillez choisir un numéro entre 1 et 5")
    else:
        print("Veuillez choisir un numéro entre 1 et 5")
