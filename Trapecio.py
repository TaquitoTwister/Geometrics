#Área Trapecio
def area_trapecio(B,b,h):
    area=(B+b)*h/2
    return area

#Perímetro Trapecio
def perimetro_trapecio(B,b,a,c):
    peri=a+B+b+c
    return peri

a=float(input("Primer lado: "))
c=float(input("Segundo lado: "))
b=float(input("Base menor: "))
B=float(input("Base mayor: "))
h=float(input("Altura: "))

print("El área es: ",round(area_trapecio(B,b,h),2))
print("El perímetro es: ",round(perimetro_trapecio(B,b,a,c,2))
