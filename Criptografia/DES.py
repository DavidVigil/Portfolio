# Desarrollado por David Vigil 20/09/2024
#Es necesario instalar PyCriptodome con el comando pip install pycryptodome
from Crypto.Cipher import DES
from secrets import token_bytes
from textwrap import wrap

def cifrar(mensaje, llave):
    cifrador = DES.new(llave, DES.MODE_EAX)
    nonce = cifrador.nonce
    cifrado, tag = cifrador.encrypt_and_digest(mensaje.encode('ascii'))
    return cifrado, tag, nonce

def descifrar(nonce, cifrado, tag):
    cifrador = DES.new(llave, DES.MODE_EAX, nonce=nonce) 
    mensaje = cifrador.decrypt(cifrado)
    try:
        cifrador.verify(tag)
        return mensaje.decode('ascii')
    except:
        return False

def ingresaClave():
    llave = input("Ingresa la llave de 64 bits: ").encode('ascii')
    if len(llave) != 8:
        print("\nLa llave debe ser de 64 bits")
        return ingresaClave()
    else:
        return llave
    
def bytes_to_bits_binary(byte_data):
    bits_data = bin(int.from_bytes(byte_data, byteorder='big'))[2:]
    return bits_data


print("\n---------- Cifrado DES ----------")
llave = ingresaClave()
mensaje = input("Ingresa el mensaje que deseas cifrar: ")
cifrado, tag, nonce = cifrar(mensaje, llave)
cifrado_bits = bytes_to_bits_binary(cifrado)
print("\nCriptograma: ", cifrado_bits)
print("\n---------- Descifrado DES ----------")
llave = ingresaClave()
cifrado_bits = input("Ingresa el criptograma en bits: ")
cifrado_bytes = int(cifrado_bits, 2).to_bytes((len(cifrado_bits) + 7) // 8, byteorder='big')
mensaje_descifrado = descifrar(nonce, cifrado_bytes, tag)
if not mensaje_descifrado:
    print("Error al descifrar el mensaje")
else:
    print("\nMensaje descifrado: ", mensaje_descifrado, "\n")
