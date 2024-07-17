#Imports

import Login
import SignIn
import database

#Option Selector:

def welcomeScreen():
  #Welcome panel:
  print("\n--------------------")
  print("¡Bienvenido/a a ATM!")
  print("--------------------\n")
  try:
    option = int(input("¿Qué acción desea realizar?:\n1) Crear cuenta \n2) Acceder con tarjeta \n3) Acceder sin tarjeta\n0) Salir\n\nIndique el numero de su opción: "))
    if option == 0:
      print("¡Hasta pronto!")
      return
    if option == 1:
      return SignIn.start(welcomeScreen)
    if option == 2:
      return Login.accessCard(welcomeScreen)
    if option == 3:
      return Login.accessNID(welcomeScreen)
    if option == 4:
      database.accessInfo()
      return welcomeScreen()
    raise TypeError("Solo se aceptan los numeros del 0 al 3.")
    return welcomeScreen()
  except:
    print("\n---------------------------------------------------------")
    print("Ha ocurrido un error, ingrese una opción numérica válida")
    print("---------------------------------------------------------\n")
    return welcomeScreen()

admin = database.User("Admin",12345678, 1234)
database.users.append(admin)
welcomeScreen()