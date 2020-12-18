import sys
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad


def ecrypt(plaintext):
    plaintext = plaintext.encode('utf-8')
    cipher = AES.new(AESkey, AES.MODE_CBC, iv)
    return b64encode(cipher.encrypt(pad(plaintext, AES.block_size))).decode('utf-8')


def decrypt(ciphertext, iv):
    ciphertext = ciphertext.encode('utf-8')
    cipher = AES.new(AESkey, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(b64decode(ciphertext)), AES.block_size).decode('utf-8')


def return_args(flag, offset):
    i = sys.argv.index(flag) + 1 + offset
    return sys.argv[i]


def addInfo(website, username, password):
    encrypted_password = ecrypt(password)
    try:
        fp = open('parole_criptate', 'a')
    except:
        print('Eroare la deschiderea fisierului sau fisierul nu a fost creat inca!')
        sys.exit(1)
    fp.write(website + ' ' + username + ' ' + encrypted_password + ' ' + b64encode(iv).decode('utf-8') + '\n')
    fp.close()


def updateInfo(website, username, password):
    if removeInfo(website, username) == 1:
        addInfo(website, username, password)
        print("Datele au fost actualizate cu succes!")
    else:
        print("Datele " + website + " " + username + " nu se afla in fisier!")
    


def listInfo():
    try:
        fp = open('parole_criptate', 'r')
    except:
        print('Eroare la deschiderea fisierului sau fisierul nu a fost creat inca!')
        sys.exit(1)
    Lines = fp.readlines()
    for line in Lines:
        listOfWords = line.split()
        print(listOfWords[0]+ ' ' + listOfWords[1] + ' ' + decrypt(listOfWords[2], b64decode(listOfWords[3].encode('utf-8'))))
    fp.close()


def getByWebsite(website):
    try:
        fp = open('parole_criptate', 'r')
    except:
        print('Eroare la deschiderea fisierului sau fisierul nu a fost creat inca!')
        sys.exit(1)
    Lines = fp.readlines()
    ok = 0
    for line in Lines:
        listOfWords = line.split()
        if(listOfWords[0] == website):
            print(listOfWords[0]+ ' ' + listOfWords[1] + ' ' + decrypt(listOfWords[2], b64decode(listOfWords[3].encode('utf-8'))))
            ok = 1
    if ok == 0:
        print("Date despre " + website + " nu exista in fisier!")
    fp.close()


def removeInfo(website, username):
    try:
        fp = open('parole_criptate', 'r')
    except:
        print('Eroare la deschiderea fisierului sau fisierul nu a fost creat inca!')
        sys.exit(1)
    Lines = fp.readlines()
    data = ''
    ok = 0
    for line in Lines:
        listOfWords = line.split()
        if listOfWords[0] != website or listOfWords[1] != username:
            data = data + line
        else:
            ok = 1
    fp.close()
    fp = open('parole_criptate', 'w')
    fp.write(data)
    fp.close()
    return ok


master_password = 'parolasecreta123'
AESkey = master_password.encode('utf-8')
iv = Random.new().read(AES.block_size)
def checkPassword():
    i_password = sys.argv[1]
    if master_password != i_password:
        print('Parola introdusa este gresita')
        sys.exit(1)


if '-add' in sys.argv:
    checkPassword()
    try:
        website = return_args('-add', 0)
        username = return_args('-add', 1)
        password = return_args('-add', 2)
    except:
        print('Numar gresit de argumente pentru comanda add!')
        print('pwmanager.py <master_password> -add <website> <username> <password>')
        sys.exit(1)
    addInfo(website, username, password)
    print("Datele au fost adaugate cu succes!")

if '-update' in sys.argv:
    checkPassword()
    try:
        website = return_args('-update', 0)
        username = return_args('-update', 1)
        password = return_args('-update', 2)
    except:
        print('Numar gresit de argumente pentru comanda update!')
        print('pwmanager.py <master_password> -update <website> <username> <new_password>')
        sys.exit(1)
    updateInfo(website, username, password)

if '-remove' in sys.argv:
    checkPassword()
    try:
        website = return_args('-remove', 0)
        username = return_args('-remove', 1)
    except:
        print('Numar gresit de argumente pentru comanda remove!')
        print('pwmanager.py <master_password> -remove <website> <username>')
        sys.exit(1)
    if removeInfo(website, username) == 1:
        print("Datele au fost eliminate cu succes!")
    else:
        print("Datele " + website + " " + username + " nu se afla in fisier!")

if '-list' in sys.argv:
    checkPassword()
    listInfo()

if '-get' in sys.argv:
    checkPassword()
    try:
        website = return_args('-get', 0)
    except:
        print('Numar gresit de argumente pentru comanda get!')
        print('pwmanager.py <master_password> -get <website>')
        sys.exit(1)
    getByWebsite(website)

if '-help' in sys.argv:
    print('Comenzile disponibile sunt:')
    print('pwmanager.py <master_password> -add <website> <username> <password>')
    print('pwmanager.py <master_password> -update <website> <username> <new_password>')
    print('pwmanager.py <master_password> -remove <website> <username>')
    print('pwmanager.py <master_password> -get <website>')
    print('pwmanager.py <master_password> -list')