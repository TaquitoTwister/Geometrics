#Área Paralelepipedo Rectangular
def area_base_paralelepipedo_rectangular():
    areabp=l*a
    return areabp

def area_lado_1_paralelepipedo_rectangular():
    arealp1=h*l
    return arealp1

def area_lado_2_paralelepipedo_rectangular():
    arealp2=h*a
    return arealp2

#Volumen Paralelepipedo Rectangular
def volumen_paralelepipedo_rectangular():
    vparalelepipedor=h*l*a
    return vparalelepipedor

#variables
h=float(input("Altura: "))
l=float(input("Largo: "))
a=float(input("Ancho: "))

print("El área de la base es: ",round(area_base_paralelepipedo_rectangular(),2))
print("El área lateral por largo es: ",round(area_lado_1_paralelepipedo_rectangular(),2))
print("El área lateral por ancho es: ",round(area_lado_2_paralelepipedo_rectangular(),2))
print("El volumen del Paralelepipedo Rectangular es: ",round(volumen_paralelepipedo_rectangular(),2))
