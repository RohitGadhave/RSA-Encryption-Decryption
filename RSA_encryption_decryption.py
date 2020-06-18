from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP


def generate_new_keys(key_size):
    random_generator = Random.new().read
    key = RSA.generate(key_size, random_generator)
    private, public = key, key.publickey()
    print("\n" + "public key : "+str(public) + "\n" + "Private  key : " + str(private))
    return public, private


def encrypt(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    print("\n"+"Encrypted massage :- " + str(cipher.encrypt(message.encode('utf-8'))))
    return cipher.encrypt(message.encode('utf-8'))


def decrypt(cipher_text, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    print("\n"+"Decrypted massage :- " + str(cipher.decrypt(cipher_text), 'utf-8'))
    return cipher.decrypt(cipher_text)


public_key, private_key = generate_new_keys(2048)
massage = input('Enter massage :- ')
encrypt_msg = encrypt(massage, public_key)
decrypt(encrypt_msg, private_key)

