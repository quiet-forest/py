nombre = input("Indique su nombre y apellido: ")
diasWorked = int(input("Indique los dias trabajados: "))
horasPerDay = int(input("Indique las horas trabajadas al dia: "))

calSueldo = horasPerDay * 9500
sueldo = calSueldo

while True:
    print("1. Isapre")
    print("2. Fonasa")
    IsaOFon = int(input("Seleccione una opcion: "))
    if IsaOFon == 1 or IsaOFon == 2:
        break

if IsaOFon == 1:
    while True:
        print('1. Mas Vida') # 2
        print('2. Consalud') # 2
        print('3. Colmena') # 2.11
        print('4. Banmedica') # 2.34
        print('5. Cruz Blanca') # 2.76
        print('6. Vida Tres') # 2.78
        NumIsa = int(input("Seleccione su Isapre: "))
        if NumIsa > 0 and NumIsa <= 6:
            break
    if NumIsa == 1:
      DescuentoIsa = 32500 * 2
      sueldo = sueldo - DescuentoIsa
      Isapre = 'Mas vida'

    if NumIsa == 2:
        DescuentoIsa = 32500 * 2
        sueldo = sueldo - DescuentoIsa
        Isapre = 'Consalud'

    if NumIsa == 3:
        DescuentoIsa = 32500 * 2.11
        sueldo = sueldo - DescuentoIsa
        Isapre = 'Colmena'

    if NumIsa == 4:
        DescuentoIsa = 32500 * 2.34
        sueldo = sueldo - DescuentoIsa
        Isapre = 'Banmedica'

    if NumIsa == 5:
        DescuentoIsa = 32500 * 2.76
        sueldo = sueldo - DescuentoIsa
        Isapre = 'Cruz Blanca'

    if NumIsa == 6:
        DescuentoIsa = 32500 * 2.78
        sueldo = sueldo - DescuentoIsa
        Isapre = 'Vida Tres'

if IsaOFon == 2:
    fonasa = sueldo * (7 / 100)
    calSueldo -= fonasa


DescuentoAFP = sueldo * 0.12
calSueldo -= DescuentoAFP
DescuentoAFC = sueldo * (3 / 100)
calSueldo -= DescuentoAFC

print("El Sueldo del Sr/a",nombre," Es: ")
print("Sueldo Bruto: ",sueldo)
print("Sueldo Liquido: ", calSueldo)
print("Descuento AFP: ", DescuentoAFP)
print("Descuento AFC: ", DescuentoAFC)





if IsaOFon == 1:
    print('El descuento de isapre es: ',DescuentoIsa)

else:
    import math
    fonasa = math.trunc(fonasa)
    print('El descuento de fonasa es: ',fonasa)