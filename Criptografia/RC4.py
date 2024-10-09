def pedirClave(): #Pide una clave hexadecimal separada por espacios y la propaga en una lista de 256 elementos
    arregloClave = [] #Lista para la clave propagada que se regresará
    claveHex = [] #Lista para la clave en hexadecimal
    clave = input("Introduce la clave: ").split(" ")
    for elemento in clave:
        try:
            claveHex.append(int(elemento, 16)) #Se convierte la clave a hexadecimal y se agrega a la lista
        except:
            print("Clave inválida. Inténtalo de nuevo.")
            return pedirClave() #Si la clave no es válida, se pide de nuevo
    for i in range(256): #Se propaga la clave en una lista de 256 elementos
        arregloClave.append(claveHex[i%len(claveHex)])
    return arregloClave
def algoritmoKSA(clave, vectorS): #Algoritmo Key-Scheduling Algorithm para generar la caja S a partir de la clave
    j=0
    for i in range(256):
        j = (j + vectorS[i] + clave[i]) % 256
        vectorS[i], vectorS[j] = vectorS[j], vectorS[i]
    return vectorS
def mostrarVectorHex(vector, mode): #Función para mostrar el vector S en Hexadecimal. Mode en 0 es para textos en hexadecimal y
    if mode == 0:                   #en 1 para vector S. Así se puede reutilizar esta función
        for i in range(len(vector)):
            print(hex(vector[i]).lstrip("0x").upper(), end=" ")
    else:
        for i in range(len(vector)):
            print(hex(vector[i]).lstrip("0x").upper(), end="\t")
            if (i+1) % 16 == 0:
                print()
def pedirMensaje(): #Pide un mensaje y lo convierte a una lista de números ASCII
    mensajeNum=[]
    mensaje = list(input("\nIntroduce el mensaje: "))
    for elemento in mensaje:
        mensajeNum.append(ord(elemento))
    return mensajeNum
def pedirCriptograma(): #Pide un criptograma y lo convierte a una lista de números hexadecimales
    criptoNum=[]
    mensaje = input("\nIntroduce el criptograma: ").split(" ")
    for elemento in mensaje:
        try:
            criptoNum.append(int(elemento, 16))
        except:
            print("Criptograma inválido. Inténtalo de nuevo.")
            return pedirCriptograma()
    return criptoNum
def algoritmoPRGA(vectorS, mensaje): #Algoritmo Pseudo-Random Generation Algorithm para generar la secuencia cifrante
    i = j = 0
    secuenciaCifrante = []
    for k in range(len(mensaje)):
        i =(i + 1) % 256
        j = (j + vectorS[i]) % 256
        vectorS[i], vectorS[j] = vectorS[j], vectorS[i]
        t = (vectorS[i] + vectorS[j]) % 256
        secuenciaCifrante.append(vectorS[t])
    return secuenciaCifrante
def cifrador(mensaje, secuenciaCifrante): #Función para cifrar y descifrar el mensaje
    res = []
    for i in range(len(mensaje)):
        res.append(mensaje[i] ^ secuenciaCifrante[i])
    return res

#Main segmentado para permitir cifrar y descifrar cualquier mensaje y cualquier criptograma sin que estén relacionados
vectorS = [x for x in range(256)] 
print("\n--------- Cifrador RC4 ---------") #Esta porción se encarga de cifrar un mensaje
clave = pedirClave()
print("Vector S inicial:")
mostrarVectorHex(vectorS,1)
vectorS = algoritmoKSA(clave, vectorS)
print("\nVector S final:")
mostrarVectorHex(vectorS, 1)
mensaje = pedirMensaje()
secuenciaCifrante = algoritmoPRGA(vectorS, mensaje)
print("\n--- Mensaje cifrado ---")
mensajeCifrado=cifrador(mensaje, secuenciaCifrante)
print("Hexadecimal:", end=" ")
mostrarVectorHex(mensajeCifrado, 0)
print("\nASCII:", end=" ")
for elemento in mensajeCifrado:
    print(chr(elemento), end="")

vectorS = [x for x in range(256)] #Se reinicia el vector S para descifrar
print("\n\n--------- Descifrador RC4 ---------") #Esta porción se encarga de descifrar un mensaje
clave = pedirClave()
vectorS = algoritmoKSA(clave, vectorS)
mensajeCifrado = pedirCriptograma()
secuenciaCifrante = algoritmoPRGA(vectorS, mensajeCifrado)
print("\n--- Mensaje descifrado ---")
mensajeClaro = cifrador(mensajeCifrado, secuenciaCifrante)
print("Hexadecimal:", end=" ")
mostrarVectorHex(mensajeClaro, 0)
print("\nASCII:", end=" ")
for elemento in mensajeClaro:
    print(chr(elemento), end="")
print()