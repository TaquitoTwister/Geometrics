import math

#Perímetro Cubo
def per_cubo():
    acubo=arista**2
    return acubo

#Diagonal Cubo
def diag_cubo():
    dcubo= math.sqrt(3) * arista
    return dcubo

#Área Base Cubo
def areab_cubo():
    acubo=arista**2
    return acubo

#Área Lateral Cubo
def areal_cubo():
    acubo=arista**2 * 4
    return acubo

#Área Total Cubo
def areat_cubo():
    acubo=arista**2 * 6
    return acubo

#Volumen Cubo
def volumen_cubo():
    vcubo=arista**3
    return vcubo

arista = float(input("Tamaño de la arista: "))

print("Perímetro del Cubo: ", round(per_cubo(),2))
print("Diagonal del Cubo: ", round(diag_cubo(),2))
print("Área de la base del Cubo: ", round(areab_cubo(),2))
print("Área lateral del Cubo: ", round(areal_cubo(),2))
print("Área total del Cubo: ", round(areat_cubo(),2))
print("Volumen de tu Cubo: ", round(volumen_cubo(),2))
