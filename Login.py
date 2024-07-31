# Login with card
import database
import userMenu

def verifyPin(index, exitFunction):
  try:
    tries = 0
    user = database.users[index]
    while tries <= 4:
      pin = int(input("Ingresa tu clave de seguridad de 4 dígitos: "))
      if pin == 0:
        return 
      if pin == user.pin:
        return userMenu.start(user, exitFunction)
      if tries == 4:
        return print("No cuenta con más intentos, operación cancelada.")
      tries = tries + 1
      print("El pin no coincide con la tarjeta. Vuelva a intentarlo o escriba 0 para salir.")
      print(f"Tiene {4 - tries} intentos restantes.")
  except:
    print("Ocurrió un error, vuelve a intentarlo.")
    return verifyPin(index, exitFunction)

def accessCard(exitFunction):
  try:
    print("Introduzca 0 para salir")
    cardNumber = int(input("Introduzca su numero de tarjeta: "))
    if cardNumber == 0:
      return exitFunction()
    if cardNumber in database.cardsList:
      print("¡Tarjeta encontrada exitosamente!\n")
      index = database.cardsList.index(cardNumber)
      return verifyPin(index, exitFunction)
    print("No se encontró la tarjeta, vuelva a intentar.")
    return accessCard(exitFunction)
  except:
    print("Ocurrió un error inesperado, vuelva a intentar.")
    return accessCard(exitFunction)

def accessNID(exitFunction):
  try:
    print("Introduzca 0 para salir")
    nationalID = int(input("Introduzca su DNI: "))
    if nationalID == 0:
      return exitFunction()
    if nationalID in database.NIDList:
      print("¡Usuario encontrado exitosamente!\n")
      index = database.NIDList.index(nationalID)
      return verifyPin(index, exitFunction)
    print("No se encontró el usuario, vuelva a intentar.")
    return accessNID(exitFunction)
  except:
    print("Ocurrió un error inesperado, vuelva a intentar.")
    return accessNID(exitFunction)