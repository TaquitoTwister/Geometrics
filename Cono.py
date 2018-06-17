import math

r =  float(input("Radio: "))
h =   float(input("Altura: "))
g =  float(input("Generatriz: "))


def volumen_cono():
    vcono = ((math.pi * r**2)  * h) / 3
    return  vcono



def area_total_cono():
    acono = (math.pi  * r  * g) + math.pi * r**2
    return acono


def area_lateral_cono():
    alcono = math.pi  * r  * g
    return alcono




print("El área lateral del Cono es:",round(area_lateral_cono(),2))
print("El área total del Cono es:",round(area_total_cono(),2))
print("El volumen del Cono es:",round(volumen_cono(),2))
