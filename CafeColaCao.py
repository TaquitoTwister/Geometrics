#Área Lateral Cubo
def area_cubo():
    acubo=arista**2
    return acubo

#Volumen Cubo
def volumen_cubo():
    vcubo=arista**3
    return vcubo

arista = float(input("Tamaño de la arista: "))

print("Volumen de tu Cubo: ", round(volumen_cubo(),2))
print("Área lateral del Cubo: ", round(area_cubo(),2))
