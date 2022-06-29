from speck import SpeckCipher

tiny_cipher = SpeckCipher(0x123456789ABCDEFF, key_size=64, block_size=32)

#speck cipher encryption

a = [128, 129, 254, 255, 148, 192, 0, 1, 213]

int_val = int.from_bytes(a, "little")

print(int_val)

enc = tiny_cipher.encrypt(int_val)

print("Encrypted: ", enc)

to_bytes = enc.to_bytes(9, byteorder ='little')
print(list(to_bytes))

dec = tiny_cipher.decrypt(enc)

print("Decrypted: ", enc)

to_bytes = dec.to_bytes(9, byteorder ='little')
print(list(to_bytes))
