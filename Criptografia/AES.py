from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'00112233445566778899aabbccddeeff'
key = b'000102030405060708090a0b0c0d0e0f'
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
nonce = cipher.nonce
print('Criptograma:', ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print('Mensaje claro:',data)