#Volumen Esfera
def volumen_esfera():
    vesfera = ((4*3.14*(r**3))/3)
    return vesfera

r = float(input("Radio: "))

print("El volumen de la Esfera es:",round(volumen_esfera(),2))
