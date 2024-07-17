def start(user, exitFunction):
  try:
    print(f"\nBienvenido/a {user.name}")
    print(f"Tus fondos actuales son: ${user.money}")
    print("Elija una opción:\n")
    print("1) Depositar dinero.")
    print("2) Retirar dinero.")
    print("3) Consultar información.")
    print("4) Transferir dinero.")
    print("0) Cerrar sesión.")
    option = int(input("\nEscriba el numero de su opción: "))
    if option == 0:
      print(f"¡Hasta la próxima vez, {user.name}!\n")
      return exitFunction()
    if option == 1:
      depositMoney(user)
      return start(user, exitFunction)
    if option == 2:
      withdrawMoney(user)
      return start(user, exitFunction)
    if option == 3:
      print(f"Nombre: {user.name}")
      print(f"Fondos: {user.money}")
      print(f"N° de tarjeta: {user.cardNumber}")
      print("-----------------------------------")
      return start(user, exitFunction)
    print("Opcion no valida. Vuelva a intentar")
    return start(user, exitFunction)
  except:
    print("Algo salió mal, vuelva a intentarlo")
    return start(user, exitFunction)

def depositMoney(user):
  try:
    amount = int(input("Ingrese la cantidad a agregar: "))
    if amount == 0:
      print("Operación cancelada")
      return
    if amount < 0:
      print("Acción invalida")
      return
    user.addMoney(amount)
    print(f"¡Fondos agregados exitosamente!")
    return
  except:
    print("Ocurrió un error, vuelva a intentarlo o escriba 0 para salir")

def withdrawMoney(user):
  try:
    amount = int(input("Ingrese la cantidad a retirar: "))
    if amount == 0:
      print("Operación cancelada")
      return
    if amount < 0:
      print("Acción invalida")
      return
    if amount > user.money:
      print(f"Fondos insuficientes. Fondos actuales: {user.money}")
      return
    user.removeMoney(amount)
    print(f"¡Fondos retirados exitosamente!")
    return
  except:
    print("Ocurrió un error, vuelva a intentarlo o escriba 0 para salir")