#---------- Desarrollado por David Vigil 05/09/2024 ----------
def cifrarVernam(): #Esta función recibe un mensaje y una clave y devuelve el criptograma en binario (No recibe los datos como parámetros, sino que los solicita al usuario)
    result = ""
    llave = [] #Aquí se almacenará la clave en forma de arreglo, así podemos propagarla de ser necesario
    mensaje = [] #Aquí se almacenará el mensaje en forma de arreglo
    texto = input("Introduce el texto a cifrar: ") #Recibimos el mensaje como string
    clave = input("Introduce la clave: ") #Recibimos la clave como string
    if len(clave) <= len(texto): #Esta estructura se encarga de propagar la clave para que cubra en su totalidad la extensión del mensaje
        for i in range(len(texto)):
            if clave[i%len(clave)] != " ": #Si el caracter no es un espacio, se añade al arreglo de la clave
                llave.append(clave[i%len(clave)])
            else:
                continue #Si el caracter es un espacio, se omite
        for letra in texto:
            if letra != " ": #Si el caracter no es un espacio, se añade al arreglo del mensaje
                mensaje.append(letra)
            else:
                continue #Si el caracter es un espacio, se omite
    else:
        print("La clave es más larga que el mensaje. Intenta con una clave de igual o menor tamaño") #Si la clave es más larga que el mensaje, se imprime un mensaje de error y se vuelve a llamar a la función
        cifrarVernam()
    for i in range(len(mensaje)): #Para cada caracter en el mensaje, se hace una XOR con el caracter correspondiente de la clave
        result += bin(ord(mensaje[i])^(ord(llave[i]))) #El resultado se almacena en la variable result en forma de binario
    return result.replace("0b"," ") #Se devuelve el resultado, pero se elimina el prefijo 0b para que se pueda visualizar mejor       
def descifrarVernam(): #Esta función recibe un criptograma y una clave y devuelve el mensaje original (No recibe los datos como parámetros, sino que los solicita al usuario)
    result = ""
    llave = [] #Aquí se almacenará la clave en forma de arreglo, así podemos propagarla de ser necesario
    criptograma = [] #Aquí se almacenará el criptograma en forma de arreglo
    texto = input("Introduce las cadenas de bits a descifrar separadas por espacios: ") #Recibimos el criptograma como string
    clave = input("Introduce la clave: ") #Recibimos la clave como string
    if len(clave) <= len(texto): #Esta estructura se encarga de propagar la clave para que cubra en su totalidad la extensión del mensaje
        for i in range(len(texto)): 
            if clave[i%len(clave)] != " ": #Si el caracter no es un espacio, se añade al arreglo de la clave
                llave.append(clave[i%len(clave)]) 
            else:
                continue #Si el caracter es un espacio, se omite
        for letra in texto.split(" "): #Se divide el criptograma en una lista de cadenas de bits
            criptograma.append(letra) #Se añade cada cadena de bits al arreglo del criptograma
    else:
        print("La clave es más larga que el mensaje. Intenta con una clave de igual o menor tamaño") #Si la clave es más larga que el mensaje, se imprime un mensaje de error y se vuelve a llamar a la función
        descifrarVernam()
    for i in range(len(criptograma)):
        result += chr(int(criptograma[i],2)^int(ord(llave[i]))) #Para cada cadena de bits en el criptograma, se hace una XOR con el caracter correspondiente de la clave
    return result
print("")
print("---------- Cifrado Vernam ----------") #Sección de cifrado
print("Criptograma: ", cifrarVernam()) #Se imprime el criptograma
print("")
print("---------- Descifrado Vernam ----------") #Sección de descifrado
print("Mensaje claro: ", descifrarVernam()) #Se imprime el mensaje claro