def cifrarAfin(mensaje, a, b):
    ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    result = ""
    for letra in mensaje:
        if letra.upper() in ABC:
            letraCifrada = ABC[(ABC.index(letra.upper())*a+b)%len(ABC)]
            result += str(letraCifrada)
        else:    
            result += letra
    return result

def descifrarAfin(criptograma, a, b):
    ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    INV = [1,19,25,28,15,31,16,14,33,26,27,34,20,8,5,7,24,35,2,13,30,32,29,17,3,10,11,4,23,21,6,22,9,12,18,0]
    result = ""
    for letra in criptograma:
        if letra.upper() in ABC:
            letraDescifrada = ABC[((ABC.index(letra.upper())-b)*INV[a-1])%len(ABC)]
            result += str(letraDescifrada)
        else:
            result += letra
    return result

mensaje = input("Introduce el mensaje a cifrar: ")
print(cifrarAfin(mensaje, 1, 7))
criptograma = input("Introduce el criptograma a descifrar: ")
print(descifrarAfin(criptograma, 1, 7))