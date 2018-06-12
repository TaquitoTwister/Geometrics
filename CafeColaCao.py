#Área Cuadrado
def area_cuadrado():
    acuadrado=arista**2
    return acuadrado

#Volumen Cuadrado
def volumen_cuadrado():
    vcuadrado=arista**3
    return vcuadrado

arista = int(input("Tamaño de la arista: "))

print("Volumen de tu cuadrado: ", volumen_cuadrado())
print("Área de tu cuadrado: ", area_cuadrado())
