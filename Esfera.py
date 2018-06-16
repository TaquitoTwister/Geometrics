import math
#Área Esfera
def area_esfera(r):
    area=(4*math.pi*(r**2))
    return area

#Volumen Esfera
def volumen_esfera():
   vesfera = ((4*math.pi*(r**3))/3)
   return vesfera

r = float(input("Radio: "))

print("El volumen de la Esfera es:",round(volumen_esfera(r),2))
print("El área es: ",round(area_esfera(r),2))
