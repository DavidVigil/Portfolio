# -*- coding: latin-1 -*-

def cesarCifrar(texto):
    result = ""
    for letra in texto:
        if letra in ABC:
            result += ABC[(ABC.index(letra)+3)%len(ABC)]
        elif letra in abc:
            result += abc[(abc.index(letra)+3)%len(abc)]
        else:
            result += letra
    return result

def cesarDescifrar(texto):
    result = ""
    for letra in texto:
        if letra in ABC:
            result += ABC[(ABC.index(letra)-3)%len(ABC)]
        elif letra in abc:
            result += abc[(abc.index(letra)-3)%len(abc)]
        else:
            result += letra
    return result

def cesarClaveCifrar(texto, clave):
    result = ""
    for i in clave:
        if i.upper() not in Abc:
            if i==" ":
                continue
            Abc.append(i.upper())
    for i in ABC:
        if i.upper() not in Abc:
            Abc.append(i.upper())
    print("Abecedario con clave: ", Abc)
    print(len(Abc))
    for letra in texto:
        if letra in ABC or letra in abc:
            result += Abc[((Abc.index(letra.upper())+3)%len(ABC))]
        else:
            result += letra
    return result

def cesarClaveDescifrar(texto):
    result = ""
    for letra in texto:
        if letra in ABC or letra in abc:
            result += Abc[((Abc.index(letra.upper())-3)%len(ABC))]
        else:
            result += letra
    return result

def cesarIsometricoCifrar():
    result = ""
    llave = []
    mensaje = []
    texto = input("Introduce el texto a cifrar: ")
    clave = input("Introduce la clave: ") 
    if len(clave) < len(texto):
        for i in range(len(texto)):
            if clave[i%len(clave)] != " ":
                llave.append(clave[i%len(clave)].upper())
            else:
                continue
        for letra in texto:
            if letra != " ":
                mensaje.append(letra.upper())
            else:
                continue
        for i in range(len(mensaje)):
            result += ABC[(ABC.index(mensaje[i])+ABC.index(llave[i]))%len(ABC)]
        print("Criptograma: ", result)
        print("Clave: ", llave)
    elif len(clave) > len(texto):
        print("La clave es más larga que el mensaje. Intenta con una clave de igual o menor tamaño")
        cesarIsometricoCifrar()
    else:
        for letra in texto:
            mensaje.append(letra.upper())
        for letra in clave:
            llave.append(letra.upper())
        for i in range(len(mensaje)):
            result += ABC[(ABC.index(mensaje[i])+ABC.index(llave[i]))%len(ABC)]
        print("Criptograma: ", result)
        print("Clave: ", llave)
    return clave

def cesarIsometricoDescifrar(clave):
    result = ""
    llave = []
    mensaje = []
    texto = input("Introduce el texto a descifrar: ")
    if len(texto) < len(clave):
        print("El mensaje es más corto que la clave. Intenta con un mensaje de igual o mayor tamaño")
        cesarIsometricoDescifrar(clave)
    else:
        for i in range(len(texto)):
            llave.append(clave[i%len(clave)].upper())
        for letra in texto:
            if letra != " ":
                mensaje.append(letra.upper())
            else:
                continue
        for i in range(len(mensaje)):
            result += ABC[(ABC.index(mensaje[i])-ABC.index(llave[i]))%len(ABC)]
    print("Mensaje claro: ", result)

Abc = [] # Abecedario en el que se pone la clave
ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"," "]
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

print("Cifrado y descifrado César")
texto = input("Introduce el texto a cifrar: ")
print("Criptograma: ", cesarCifrar(texto))
texto = input("Introduce el texto a descifrar: ")
print("Mensaje claro: ", cesarDescifrar(texto))
print("")
print("Cifrado César con clave, completando el abecedario")
clave = input("Introduce la clave: ")
texto = input("Introduce el texto a cifrar: ")
print("Criptograma: ", cesarClaveCifrar(texto, clave))
texto = input("Introduce el texto a descifrar: ")
print("Mensaje claro: ", cesarClaveDescifrar(texto))
print("")
print("Cifrado César con clave isométrica")
clave = cesarIsometricoCifrar()
print("Clave: ", clave)
cesarIsometricoDescifrar(clave)
