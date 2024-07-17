# Login with card
import database

def accessCard(exitFunction):
  try:
    print("Introduzca 0 para salir")
    cardNumber = int(input("Introduzca su numero de tarjeta: "))
    if cardNumber == 0:
      return exitFunction()
    if cardNumber in database.cardsList:
      print("¡Tarjeta encontrada exitosamente!\n")
      return exitFunction()
      # index = database.cardsList.index(cardNumber)
      # return verifyPin(index)
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
      return exitFunction()
      # index = database.NIDList.index(nationalID)
      # return verifyPin(index)
    print("No se encontró el usuario, vuelva a intentar.")
    return accessNID(exitFunction)
  except:
    print("Ocurrió un error inesperado, vuelva a intentar.")
    return accessNID(exitFunction)