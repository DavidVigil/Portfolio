#Desarrollado por David Vigil 05/09/2024
def cifrarVernam():
    result = ""
    llave = []
    mensaje = []
    texto = input("Introduce el texto a cifrar: ")
    clave = input("Introduce la clave: ") 
    if len(clave) <= len(texto): #Esta estructura se encarga de propagar la clave para que cubra en su totalidad la extensión del mensaje
        for i in range(len(texto)):
            if clave[i%len(clave)] != " ":
                llave.append(clave[i%len(clave)])
            else:
                continue
        for letra in texto:
            if letra != " ": #Los espacios se omiten al cifrar
                mensaje.append(letra)
            else:
                continue
    else:
        print("La clave es más larga que el mensaje. Intenta con una clave de igual o menor tamaño")
        cifrarVernam()
    for i in range(len(mensaje)):
        result += bin(ord(mensaje[i])^(ord(llave[i])))
    return result.replace("0b"," ")
        
def descifrarVernam():
    result = ""
    llave = []
    criptograma = []
    texto = input("Introduce las cadenas de bits a descifrar separadas por espacios: ")
    clave = input("Introduce la clave: ")
    if len(clave) <= len(texto):
        for i in range(len(texto)):
            if clave[i%len(clave)] != " ":
                llave.append(clave[i%len(clave)])
            else:
                continue
        for letra in texto.split(" "):
            criptograma.append(letra)
    else:
        print("La clave es más larga que el mensaje. Intenta con una clave de igual o menor tamaño")
        descifrarVernam()
    for i in range(len(criptograma)):
        result += chr(int(criptograma[i],2)^int(ord(llave[i])))
    return result

print("Criptograma: ", cifrarVernam())
print("Mensaje: ", descifrarVernam())