# class Factory:
#     a = 12
#     b = 23
#     def hello():
#         pass

# Public and Private -> Attributes and Method's

# class Fac:
#     __a = 9             #Encapsulation
#     b = 7
#     def hello():
#         print("Hello World in my Own")
#     hello()
#     print(__a)

# Fac.hello()
# Fac()

# Object in python -------------------------

# class Fac:
#     a = 89
#     b = 78
#     def hello():
#         print("Hellow World")
    
# obj = Fac

# print(obj.a)
# obj.hello()

# Constractor ----------------------------------

# class Factory:
#     def __init__(self, BT, ET, TY,):
#         self.BT = BT
#         self.ET = ET
#         self.TY = TY
#     def helo(self):
#         print(f'Details is Body {self.BT} and Enging is {self.ET} types and Tyers is {self.TY}')

# Ferari = Factory('Coverd', '5 Cycle', 9)
# Ninja = Factory('Open', '13 cycle', 2)
# Ninja.helo()
# Ferari.helo()

#   


# Inheritins in python ----------------------------


# class Fac:
#     def __init__(self,B, E, T):
#         self.B = B
#         self.E = E
#         self.T = T
#     def showDetails(self):
#         print(f'{self.B} , {self.E} , {self.T}')
    
# # Ferari = Fac('Covered', '6 cycle', '4')
# # Ferari.showDetails()

# class Honda(Fac):
#     def __init__(self, B, E, T, G):
#         super().__init__(B, E, T)
#         self.G = G

# ninja = Honda('open', '6 cycle', 4, 'plustic')

# print(ninja.G)

