if figura == "paralelepipedo" or figura == "paralelepípedo":
    #Perímetro Paralelepipedo Rectangular
    def per_paralelepipedo_rectangular():
        arealp1=4* (l + a + h)
        return arealp1

    #Diagonal Paralelepipedo Rectangular
    def diag_paralelepipedo_rectangular():
        arealp1=math.sqrt(a**2 + l**2 + h**2)
        return arealp1

    #Área Base Paralelepipedo Rectangular
    def area_base_paralelepipedo_rectangular():
        areabp=l*a
        return areabp

    #Área Lateral Paralelepipedo Rectangular
    def area_lateral_paralelepipedo_rectangular():
        arealp1=2* (h*l + h*a)
        return arealp1

    #Área Total Paralelepipedo Rectangular
    def area_total_paralelepipedo_rectangular():
        arealp2=2*(l*a + l*h * a*h)
     return arealp2

    #Volumen Paralelepipedo Rectangular
    def volumen_paralelepipedo_rectangular():
        vparalelepipedor=h*l*a
        return vparalelepipedor

    #variables
    h=float(input("Altura: "))
    l=float(input("Largo: "))
    a=float(input("Ancho: "))

    print("El perímetro es: ",round(per_paralelepipedo_rectangular(),2))
    print("La diagonal es: ",round(diag_paralelepipedo_rectangular(),2))
    print("El área de la base es: ",round(area_base_paralelepipedo_rectangular(),2))
    print("El área lateral es: ",round(area_lateral_paralelepipedo_rectangular(),2))
    print("El área total es: ",round(area_total_paralelepipedo_rectangular(),2))
    print("El volumen del Paralelepípedo Rectangular es: ",round(volumen_paralelepipedo_rectangular(),2))
