# -*- coding: latin-1 -*-
import numpy as np
from numpy.linalg import inv
def ingresaClave():
    clave = np.zeros((3, 3))
    print("Ingresa la matriz clave invertible de 3x3")
    for i in range(0, 3):
        for j in range(0, 3):
            clave[i][j] = int(input("Posición [" + str(i) + "][" + str(j) + "]: "))
    if np.linalg.det(clave) == 0:
        print("La matriz no es invertible")
        clave = ingresaClave()
        return clave
    else:
        return clave
def ingresarMensaje(ABC):
    texto = input("Introduce el texto a cifrar o descifrar: ")
    if len(texto)%3 == 0:
        columns = (len(texto)//3)
    else:
        columns = (len(texto)//3)+1
    mensaje = np.zeros((3, columns))
    c=0
    for i in range(0, columns):
        try:
            mensaje[:, i] = [ABC.index(texto[c].upper()), ABC.index(texto[c+1].upper()), ABC.index(texto[c+2].upper())]
        except IndexError:
            try:
                mensaje[:, i] = [ABC.index(texto[c].upper()), ABC.index(texto[c+1].upper()), ABC.index(" ")]
            except IndexError:
                try:
                    mensaje[:, i] = [ABC.index(texto[c].upper()), ABC.index(" "), ABC.index(" ")]
                except:
                    break
        finally:
            c+=3
    return mensaje
def cifrarHill(clave, mensaje, ABC):
    resultado = np.dot(clave, mensaje)
    resultado = resultado%len(ABC)
    return resultado    
def leerMatrizC(matriz, ABC):
    resultadoT = np.transpose(matriz)
    print("Criptograma: ", end="")
    for row in range(resultadoT.shape[0]):
        for col in range(resultadoT.shape[1]):
            print(ABC[int(resultadoT[row][col])], end="")
    print("")
def leerMatrizM(matriz, ABC):
    resultadoT = np.transpose(matriz)
    print("Mensaje claro: ", end="")
    for row in range(resultadoT.shape[0]):
        for col in range(resultadoT.shape[1]):
            print(ABC[int(resultadoT[row][col])], end="")
    print("")
def HillC(ABC):
    print("")
    clave = ingresaClave()
    print("")
    print("Determinante de la matriz clave: ", np.linalg.det(clave))
    print("")
    print("Matriz inversa de la clave:")
    claveInv = inv(clave)%len(ABC)
    print(claveInv)
    print("")
    print("Matriz adjunta de K:")
    print("")
    print(np.conj(clave).T)
    mensaje = ingresarMensaje(ABC)
    print("")
    resultado = cifrarHill(clave, mensaje, ABC)
    leerMatrizC(resultado, ABC)
def HillD(ABC):
    print("")
    clave = ingresaClave()
    print("")
    mensaje = ingresarMensaje(ABC)
    resultado = cifrarHill(clave, mensaje, ABC)
    print("")
    leerMatrizM(resultado, ABC)

ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
print("--Cifrado Hill--")
HillC(ABC)
print("")
print("--Descifrado Hill--")
HillD(ABC)






