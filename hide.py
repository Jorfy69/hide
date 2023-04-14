from cryptography.fernet import Fernet
import sys
import time

filename = sys.argv[2]
filebytes = filenamebytes = len(filename).to_bytes(len(filename), 'big')
key = '' #print(Fernet.generate_key()) to get new key for this projects
fernet = Fernet(key)

if sys.argv[1] == 'encrypt' or sys.argv[1] == 'Encrypt':
    with open(filename, 'rb') as file:
        og = file.read()
    encrypted = fernet.encrypt(og)
    with open(filename, 'wb') as encryptedFile:
        encryptedFile.write(encrypted)
    time.sleep(.25)
    print(f'The file {filename} has been encrypted.')
elif sys.argv[1] == 'decrypt' or sys.argv[1] == 'decrypt':
    print('*Note the file must have been encrypted')
    time.sleep(.25)
    with open(filename, 'rb') as encryptedfile:
        encrypted = encryptedfile.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filename, 'wb') as decryptedfile:
        decryptedfile.write(decrypted) 
    time.sleep(.25)
    print(f'The file {filename} has been decrypted.')    
else:
    print('error')
