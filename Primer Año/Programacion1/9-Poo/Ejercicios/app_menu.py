from contactos import App
def menuOptions():
    print("Options:")
    print("1 - Contact Add")
    print("2 - Contact List")
    print("3 - Contact Search")
    print("4 - Contact Edit")
    usuarios=App()
    option=int(input("Enter option number: "))
    validado=False
    try:
        while not validado:
            if option == 1:
                usuarios.AddContact()
                validado=True
            elif option == 2:
                usuarios.showList()
                validado=True
            elif option == 3:
                usuarios.contactSearch()
                validado=True
            elif option == 4:
                usuarios.modifyContact()
                validado=True
            else:
                print("Numero fuera de rango")
    except:
        print("Ingresar solo Numeros enteros")

def returnSearch():
    print("Options:")
    print("1 - Return")
    print("2 - Exit")
    try:
        option = int(input("Enter option number: "))
        validado = False
        while not validado:
            if option == 1:
                menuOptions()
                validado = True
            elif option == 2:
                validado = True
            else:
                print("Numero fuera de rango")
                option = int(input("Enter option number: "))
    except ValueError:
        print("Ingresar solo números enteros")