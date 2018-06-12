#Área Cubo
def area_cubo():
    acubo=arista**2
    return acubo

#Volumen Cubo
def volumen_cubo():
    vcubo=arista**3
    return vcubo

arista = int(input("Tamaño de la arista: "))

print("Volumen de tu Cubo: ", volumen_cubo())
print("Área lateral del Cubo: ", area_cubo())
