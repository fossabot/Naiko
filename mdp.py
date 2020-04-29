id = "Mathieu"
print("l'indentifiant est: " + id)
password = "Asvel2019"
print("le mot de passe est: " + password)

new_account = input('voulez vous faire un nouveau compte? ')

if new_account != 'oui':
    id2 = input("Veuillez entrer votre identifiant: ")

    if id2 != id:
        print("L'identifient n'est pas le bon!")

    elif id2 == id:
        print("L'identifient est juste!")
    
        inputpassword2 = input("Veuiller rentrer votre Mots De Passe: ")
    
        if inputpassword2 == password:
            print("Bonjour " + id)
    
        elif inputpassword2 != password:
            print("Le mots de passe n'est pas le bon!")

else:
    new_id = input("Veuillez rentrez un nom d'utilisateur ")
    if new_id == id:
        print("Cette identifient est déja utilisé!")
    
    elif new_id != id:
        new_password = input("Veuillez rentrez un Mots De Passe ")
        check = input("Etes vous sure de vote chois? ")
        if check == oui:
            print("Veuillez patienter!")
        elif check != oui:
            check2 = input