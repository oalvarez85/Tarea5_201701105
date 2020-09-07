cadena1 = "__servidor1"
cadena2 = "3servidor"


def validarAFD(cadena):
    print()
    print("Cadena a evaluar: ",cadena)
    print("Resultado:")
    estado = 0

    for caracter in cadena:        
        if estado == 0:
            if caracter == "_":
                estado = 1
            elif caracter.isalpha():
                estado = 2
            else:
                print("Cadena incorrecta")
                return        
        elif estado == 1:            
            if caracter == "_":
                estado = 1
            elif caracter.isalpha():
                estado = 3
            else:
                print("Cadena incorrecta")
                return
        elif estado == 2:
            if caracter.isalpha():
                estado = 2
            elif caracter.isdigit():
                estado = 4
            else:
                print("Cadena incorrecta")
                return
        elif estado == 3:
            if caracter.isdigit():
                estado = 4
            else:
                print("Cadena incorrecta")
                return  
        elif estado == 4:
            print("Cadena incorrecta")
            return       
    print("¡Cadena aceptada!")

        

validarAFD(cadena1)
validarAFD(cadena2)