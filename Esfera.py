import math
#Área Esfera
def area_esfera():
    area=(4*math.pi*(r**2))
    return area

#Volumen Esfera
def volumen_esfera():
   vesfera = ((4*math.pi*(r**3))/3)
   return vesfera

r = float(input("Radio: "))

print("El volumen de la Esfera es:",round(volumen_esfera(),2))
print("El área de la Esfera es:",round(area_esfera(),2))
