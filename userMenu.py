def start(user, exitFunction):
  try:
    print(f"\nBienvenido/a {user.name}")
    print("Elija una opción:\n")
    print("1) Depositar dinero.")
    print("2) Retirar dinero.")
    print("3) Consultar saldo.")
    print("4) Transferir dinero.")
    print("0) Cerrar sesión.")
    option = int(input("Escriba el numero de su opción: "))
    if option == 0:
      print(f"Hasta la próxima vez, {user.name}")
      exitFunction()
    if option == 1:
      depositMoney(user)
      return start(user, exitFunction)
    if option == 2:
      withdrawMoney(user)
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
    print(f"¡Fondos agregados exitosamente! Nuevos fondos: {user.money}")
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
    user.removeMoney(amount)
    print(f"¡Fondos retirados exitosamente! Nuevos fondos: {user.money}")
    return
  except:
    print("Ocurrió un error, vuelva a intentarlo o escriba 0 para salir")