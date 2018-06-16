#Área Triángulo
def area_triangulo(b,h):
    area=b*h/2
    return area

#Perímetro Triángulo
def perimetro_triangulo(a,b,c):
    peri=a+b+c
    return peri

a=float(input("Primer lado: "))
b=float(input("Segundo lado: "))
c=float(input("Tercer lado: "))
h=float(input("Altura: "))

print("El área es: ",round(area_triangulo(b,h),2))
print("El perímetro es: ",round(perimetro_triangulo(a,b,c),2))
