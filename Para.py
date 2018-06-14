#Área Paralelepipedo Rectangular
def area_base_paralelepipedo_rectangular():
    areabp=l*a
    return areabp

def area_lado_1_paralelepipedo_rectangular():
    arealp1=h*a
    return arealp1

def area_lado_2_paralelepipedo_rectangular():
    arealp2=h*l
    return arealp2

#Volumen Paralelepipedo Rectangular
def volumen_paralelepipedo_rectangular():
    vparalelepipedor=h*l*a
    return vparalelepipedor

#variables
h=int(input("Altura: "))
l=int(input("Largo: "))
a=int(input("Ancho: "))

print("El área de la base es: ",area_base_paralelepipedo_rectangular())
print("El área lateral por largo es: ",area_lado_1_paralelepipedo_rectangular())
print("El área lateral por ancho es: ",area_lado_2_paralelepipedo_rectangular())
print("El volumen del Paralelepipedo Rectangular es: ",volumen_paralelepipedo_rectangular())