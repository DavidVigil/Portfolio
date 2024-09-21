# Desarrollado por David Vigil 20/09/2024
#Es necesario instalar PyCriptodome con el comando pip install pycryptodome
from Crypto.Cipher import DES

def cifrar(mensaje, llave): #Función para cifrar utilizando DES. Recibe el mensaje a cifrar y la llave.
    cifrador = DES.new(llave, DES.MODE_EAX) #Se crea un objeto cifrador con la llave
    nonce = cifrador.nonce #Se obtiene el nonce, una cadena aleatoria que se utiliza para cifrar y descifrar
    cifrado, tag = cifrador.encrypt_and_digest(mensaje.encode('ascii')) #Se cifra el mensaje y se obtiene el tag
    return cifrado, tag, nonce #Se devuelve el criptograma, el tag y el nonce

def descifrar(nonce, cifrado, tag): #Función para descifrar utilizando DES. Recibe el nonce, el criptograma y el tag.
    cifrador = DES.new(llave, DES.MODE_EAX, nonce=nonce)  #Se crea un objeto cifrador con la llave y el nonce
    mensaje = cifrador.decrypt(cifrado) #Se descifra el mensaje
    try:
        cifrador.verify(tag)
        return mensaje.decode('ascii') #Se devuelve el mensaje descifrado
    except:
        return False #Si el tag no coincide, se devuelve un False para marcar un error

def ingresaClave(): #Función para ingresar la llave de 64 bits
    llave = input("Ingresa la llave de 64 bits: ").encode('ascii')
    if len(llave) != 8:
        print("\nLa llave debe ser de 64 bits")
        return ingresaClave() #Si la llave no es de 64 bits, se vuelve a llamar a la función
    else:
        return llave #Si la llave es de 64 bits, se devuelve
    
def bytes_to_bits_binary(byte_data): #Función para convertir los bytes a una cadena de bits
    bits_data = bin(int.from_bytes(byte_data, byteorder='big'))[2:] 
    return bits_data


print("\n---------- Cifrado DES ----------")
llave = ingresaClave() #Se solicita la llave al usuario
mensaje = input("Ingresa el mensaje que deseas cifrar: ") #Se solicita el mensaje al usuario
cifrado, tag, nonce = cifrar(mensaje, llave) #Se cifra el mensaje
cifrado_bits = bytes_to_bits_binary(cifrado) #Se convierte el criptograma a una cadena de bits
print("\nCriptograma: ", cifrado_bits) #Se imprime el criptograma en bits
print("\n---------- Descifrado DES ----------")
llave = ingresaClave() #Se solicita la llave al usuario nuevamente
cifrado_bits = input("Ingresa el criptograma en bits: ") #Se solicita el criptograma al usuario
cifrado_bytes = int(cifrado_bits, 2).to_bytes((len(cifrado_bits) + 7) // 8, byteorder='big') #Se convierte el criptograma de bits a bytes
mensaje_descifrado = descifrar(nonce, cifrado_bytes, tag) #Se descifra el mensaje
if not mensaje_descifrado:
    print("Error al descifrar el mensaje") #Si el tag no coincide, se imprime un mensaje de error
else:
    print("\nMensaje descifrado: ", mensaje_descifrado, "\n") #Se imprime el mensaje descifrado
