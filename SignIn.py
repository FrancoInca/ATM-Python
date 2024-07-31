#Imports
import database

# Creating the function:

def start(exitFunction):
  try:
    name = input("Introduzca su nombre completo: ")
    nationalID = int(input("Introduzca su DNI: "))
    if database.getUser(nationalID) != False:
      print("Usuario creado con anterioriad. Verifique sus datos e intentelo de nuevo.")
      return start(exitFunction)
    pin = validatePin()
    newUser = database.User(name, nationalID, pin)
    database.users.append(newUser)
    print(f"\nUsuario creado con éxito: Bienvenido/a {name}\nSu tarjeta es: {newUser.cardNumber}\nVuelva a iniciar sesión por favor.\n")
    exitFunction()
  except:
    print("Hubo un error inesperado.")
    return start(exitFunction)

def validatePin():
  try:
    pin = int(input("Introduzca su clave de 4 dígitos de seguridad:"))
    if pin < 1000 or pin > 9999:
      print("Debe ser de 4 dígitos")
      return validatePin()
    
    pinTest = int(input("Vuelva a introducir su pin de seguridad: "))
    if pin == pinTest:
      print("¡Clave de seguridad añadida exitosamente!")
      return pin
    print("Las claves no coinciden.\nInténtelo nuevamente")
    return validatePin()
  except:
    print("Ha ocurrido un error, introduzca correctamente su pin.")
    return validatePin()