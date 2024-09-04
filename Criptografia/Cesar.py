# -*- coding: latin-1 -*-
# ---------- Cifrado y descifrado César con K = 3 ----------
def cesarCifrar(texto): #Esta función recibe el texto claro y realiza una sustitución desplazando 3 veces cada letra en el abecedario
    result = ""
    for letra in texto:
        if letra in ABC: #Revisamos si la letra se encuentra en el abecedario que contiene mayúsculas, números y el espacio
            result += ABC[(ABC.index(letra)+3)%len(ABC)] #Se suma un 3 para obtener la letra cifrada
        elif letra in abc: #Revisamos si la letra se encuentra en el abecedario que contiene minúsculas
            result += abc[(abc.index(letra)+3)%len(abc)] #Se suma un 3 para obtener la letra cifrada
        else:
            result += letra #En caso de haber colocado comillas, puntos u otros signos de puntuación, se incluyen directamente en el texto cifrado
    return result

def cesarDescifrar(texto): #Esta función descifra un mensaje cifrado con el algoritmo César simple. 
    result = ""
    for letra in texto:
        if letra in ABC: #Revisamos si la letra se encuentra en el abecedario que contiene mayúsculas, números y el espacio
            result += ABC[(ABC.index(letra)-3)%len(ABC)] #Se resta un 3 para obtener la letra original
        elif letra in abc: #Revisamos si la letra se encuentra en el abecedario que contiene minúsculas
            result += abc[(abc.index(letra)-3)%len(abc)] #Se resta un 3 para obtener la letra original
        else:
            result += letra #En caso de haber colocado comillas, puntos u otros signos de puntuación, se incluyen directamente en el texto cifrado
    return result

# ---------- Cifrado y descifrado César con clave ----------

def cesarClaveCifrar(texto, clave): #Esta función cifra a partir de un abecedario que se construye con una clave
    result = ""
    for i in clave:
        if i.upper() not in Abc: #Revisa si la letra en la clave se encuentra en el abecedario que comienza con la clave
            if i==" ": #Si la letra en cuestión es un espacio, no lo agrega a la clave. Esto es opcional si se incluye el espacio como elemento del abecedario
                continue #Sale de esta iteración del ciclo for y empieza la siguiente
            Abc.append(i.upper()) #Agrega la letra a el abecedario clave
    for i in ABC: #Este ciclo for agrega el resto de las letras del abecedario a el abecedario clave. De esta forma el abecedario comienza con las letras de la clave (sin repetirse)
        if i.upper() not in Abc:
            Abc.append(i.upper())
    print("Abecedario con clave: ", Abc) #Mostramos el abecedario con el que se hará el cifrado
    #print(len(Abc)) Esta instrucción nos sirve para saber con qué módulo se trabaja
    for letra in texto: #Este ciclo crea el mensaje con el desplazamiento k = 3. Esto se puede mejorar si llamamos a la función cesarCifrar. Para fines de esta tarea se realizó por separado
        if letra in ABC or letra in abc:
            result += Abc[((Abc.index(letra.upper())+3)%len(ABC))]
        else:
            result += letra
    return result

def cesarClaveDescifrar(texto): #Esta función descifra un texto que se cifró utilizando un corrimiento de k = 3 y una clave. Puede ser reemplazada por cesarDescifrar si se agrega un abecedario como parámetro de la función
    result = ""
    for letra in texto:
        if letra in ABC or letra in abc:
            result += Abc[((Abc.index(letra.upper())-3)%len(ABC))]
        else:
            result += letra
    return result

# ---------- Cifrado y descifrado utilizando algoritmo César isométrico ----------
#Este algoritmo utiliza una clave, suma los números de las posiciones que ocupa la letra original y la de la clave, y realiza el módulo para obtener la letra nueva
#De ser necesario, la clave se debe repetir hasta cubrir en su totalidad la extensión del mensaje en claro

def cesarIsometricoCifrar(): #Esta función cifra un texto claro pidiendo una clave y un texto
    result = ""
    llave = []
    mensaje = []
    texto = input("Introduce el texto a cifrar: ")
    clave = input("Introduce la clave: ") 
    if len(clave) < len(texto): #Esta estructura se encarga de propagar la clave para que cubra en su totalidad la extensión del mensaje
        for i in range(len(texto)):
            if clave[i%len(clave)] != " ":
                llave.append(clave[i%len(clave)].upper())
            else:
                continue
        for letra in texto:
            if letra != " ": #Los espacios se omiten al cifrar
                mensaje.append(letra.upper())
            else:
                continue
        for i in range(len(mensaje)):  #realiza la suma de posiciones del mensaje claro y de la clave, y realiza el módulo para obtener el nuevo caracter
            result += ABC[(ABC.index(mensaje[i])+ABC.index(llave[i]))%len(ABC)]
        print("Criptograma: ", result)
        print("Clave: ", llave)
    elif len(clave) > len(texto): #No se admite una clave más grande que el texto
        print("La clave es más larga que el mensaje. Intenta con una clave de igual o menor tamaño")
        cesarIsometricoCifrar() #Solicitamos la clave nuevamente utilizando recursividad
    else:
        for letra in texto:
            mensaje.append(letra.upper())
        for letra in clave:
            llave.append(letra.upper())
        for i in range(len(mensaje)):
            result += ABC[(ABC.index(mensaje[i])+ABC.index(llave[i]))%len(ABC)] #Realiza el cifrado
        print("Criptograma: ", result)
        print("Clave: ", llave)
    return clave

def cesarIsometricoDescifrar(clave):
    result = ""
    llave = []
    mensaje = []
    texto = input("Introduce el texto a descifrar: ") #Recibimos el criptograma
    if len(texto) < len(clave):
        print("El mensaje es más corto que la clave. Intenta con un mensaje de igual o mayor tamaño") #No se admiten criptogramas más cortos que la clave
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
            result += ABC[(ABC.index(mensaje[i])-ABC.index(llave[i]))%len(ABC)] #Descifra el criptograma sumando las posiciones y realizando el módulo
    print("Mensaje claro: ", result)

Abc = [] # Abecedario en el que se pone la clave
ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"," "] #Abecedario con números y espacio
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"] #Abecedario de minúsculas. Puede omitirse si los resultados se entregan solo en mayúsculas

#----- MAIN -----
#Se solicitan los datos y se muestra al momento el resultado
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
