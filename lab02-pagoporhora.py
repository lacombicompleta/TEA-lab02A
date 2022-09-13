# Tendecias e Innovacion en Tecnologias Agricola (TEA)
#
from unicodedata import numeric


horas = input("Horas trabajadas? ")
print(horas)
print(type(horas))
valorPorhora = input("valor por hora? ")
print(valorPorhora)
print(type(valorPorhora))
numeric = [int(horas)*int(valorPorhora)]
print(numeric)
