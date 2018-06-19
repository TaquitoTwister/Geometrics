#Área Trapecio
def area_trapecio():
    areatrape=(Btrape+btrape)*htrape/2
    return areatrape

#Perímetro Trapecio
def perimetro_trapecio():
    peritrape=atrape+Btrape+btrape+ctrape
    return peritrape

atrape=float(input("Lado Izquierdo: "))
ctrape=float(input("Lado Derecho: "))
btrape=float(input("Base menor: "))
Btrape=float(input("Base mayor: "))
htrape=float(input("Altura: "))

print("El área del Trapecio es: ",round(area_trapecio(),2))
print("El perímetro es: ",round(perimetro_trapecio(),2))
