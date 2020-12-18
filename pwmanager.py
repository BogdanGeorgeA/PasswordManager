import sys



def return_args(flag, offset):
    i = sys.argv.index(flag) + 1 + offset
    return sys.argv[i]



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
    #addInfo(website, username, password)
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
    #updateInfo(website, username, password)

if '-remove' in sys.argv:
    checkPassword()
    try:
        website = return_args('-remove', 0)
        username = return_args('-remove', 1)
    except:
        print('Numar gresit de argumente pentru comanda remove!')
        print('pwmanager.py <master_password> -remove <website> <username>')
        sys.exit(1)
    '''if removeInfo(website, username) == 1:
        print("Datele au fost eliminate cu succes!")
    else:
        print("Datele " + website + " " + username + " nu se afla in fisier!")'''

if '-list' in sys.argv:
    checkPassword()
    #listInfo()

if '-get' in sys.argv:
    checkPassword()
    try:
        website = return_args('-get', 0)
    except:
        print('Numar gresit de argumente pentru comanda get!')
        print('pwmanager.py <master_password> -get <website>')
        sys.exit(1)
    #getByWebsite(website)

if '-help' in sys.argv:
    print('Comenzile disponibile sunt:')
    print('pwmanager.py <master_password> -add <website> <username> <password>')
    print('pwmanager.py <master_password> -update <website> <username> <new_password>')
    print('pwmanager.py <master_password> -remove <website> <username>')
    print('pwmanager.py <master_password> -get <website>')
    print('pwmanager.py <master_password> -list')