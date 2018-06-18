if figura == "cono":
    radcono =  float(input("Radio: "))
    hcono =   float(input("Altura: "))
    gene = math.sqrt(hcono**2 + radcono**2)

    #Volumen Cono
    def volumen_cono():
        vcono = ((math.pi * radcono**2)  * hcono) / 3
        return  vcono

    #Área Total Cono
    def area_total_cono():
        acono = (math.pi  * radcono  * gene) + math.pi * radcono**2
        return acono

    #Área Lateral Cono
    def area_lateral_cono():
        alcono = math.pi  * radcono  * gene
        return alcono

    print("El área lateral del Cono es: ",round(area_lateral_cono(),2))
    print("El área total del Cono es: ",round(area_total_cono(),2))
    print("El volumen del Cono es: ",round(volumen_cono(),2))
