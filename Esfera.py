#import math va en el código principal

if figura == "esfera":
    #Área Esfera
    def area_esfera():
        area=(4*math.pi*(resfera**2))
        return area

    #Volumen Esfera
    def volumen_esfera():
       vesfera = ((4*math.pi*(resfera**3))/3)
       return vesfera

    resfera = float(input("Radio: "))

    print("El área de la Esfera es: ",round(area_esfera(),2))
    print("El volumen de la Esfera es: ",round(volumen_esfera(),2))

