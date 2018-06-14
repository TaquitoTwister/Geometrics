#Área Cuadrado
def area_cuadrado():
    areacua=aristacua**2
    return areacua

#Perímetro Cuadrado
def perimetro_cuadrado():
    pericua=aristacua*4
    return pericua

aristacua=float(input("Tamaño de la arista: "))

print("El área es: ",round(area_cuadrado(),2))
print("El perímetro es: ",round(perimetro_cuadrado(),2))
