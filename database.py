# Array of Cards Numbers
cardsList = []

#Array of DNI's
NIDList = []

#Array of Users
users = []

#Class users
class User:

  def __init__(self, name, nationalID, pin ):
    self.name = name
    self.nationalID = nationalID
    self.money = 0
    self.pin = pin
    if len(cardsList) > 0:
      self.cardNumber = cardsList[-1] + 1
    else:
      self.cardNumber = 1234567891123456
    cardsList.append(self.cardNumber)
    NIDList.append(self.nationalID)

  def addMoney(self, amount):
    self.money = self.money + amount

  def removeMoney(self, amount):
    self.money = self.money - amount

def getUser(NIDNumber):
  if NIDNumber in NIDList:
    index = NIDList.index(NIDNumber)
    user = users[index]
    return user
  return False

def accessInfo():
  for user in users:
    print(f"Nombre: {user.name} \nNID: {user.nationalID} \nPIN: {user.pin} \nNúmero de tarjeta: {user.cardNumber}")
    print("-----------------------------------")
