cadena1 = "__servidor1"
cadena2 = "3servidor"
cadena3 = "__s1"
cadena4 = "_jsn2"

def validarAFD(cadena):
    estado = 0

    for i in range(len(cadena)):
        print(estado)
        if estado == 0:
            if cadena[i] == "_":
                estado = 1
            elif cadena[i].isalpha():
                estado = 2
            else:
                print("Cadena incorrecta")
                return        
        if estado == 1:
            if cadena[i] == "_":
                estado = 1
            elif cadena[i].isalpha():
                estado = 3
            else :
                print("Cadena incorrecta")
                return
        if estado == 2:
            if cadena[i].isalpha:
                estado = 2
            elif cadena[i].isdigit():
                estado = 4
            else:
                print("Cadena incorrecta")
                return
        if estado == 3:
            if cadena[i].isdigit():
                estado = 4
            else:
                print("Cadena incorrecta")
                return
        if estado == 4:
            print("Cadena incorrecta")
            return
    print("¡Cadena aceptada!")

        

validarAFD(cadena1)
validarAFD(cadena2)
validarAFD(cadena3)
validarAFD(cadena4)