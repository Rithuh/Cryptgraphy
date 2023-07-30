import math
def keylessEncrypt(msg,key):
    enc = ''
    msg = msg.lower()
    for i in range(key):
        enc += msg[i::key]
                
    print('Encrypted Text: ', enc)
    keylessDecrypt(enc,key)



def keylessDecrypt(msg,key):
    ##Incorrect
    dec = ''
    msg = msg.lower()
    l = [['' for j in range(key)] for i in range(math.ceil(len(msg)/key))]
    for i in range(key):
        dec += msg[i::key]
                
    print('Decrypted Text: ', dec)
    
def keyedEncrypt(msg,key):
    #To be completed
    pass
    
def keyedDecrypt(msg,key):
    #To be completed
    pass
    
def main():
    print('MENU')
    print('Enter:\n1 for Keyless Transposition Cipher\n2 for Keyed Transposition Cipher')
    cph = int(input())
    msg = input('Enter the text: ')
    if(cph == 1):
        ch = int(input('Enter:\n1 for Encryption\n2 for Decryption: '))
        if(ch == 1):
            key = int(input('Enter the number of Columns:'))
            keylessEncrypt(msg,key)
        elif ch == 2:
            key = int(input('Enter the number of Columns:'))
            keylessDecrypt(msg,key)
        else:
            print('Invalid Choice')

    elif cph == 2:
        ch = int(input('Enter:\n1 for Encryption\n2 for Decryption: '))
        if(ch == 1):
            key = [int(i) for i in input('Enter the permutation sequence separated by a space:').split()]
            keyedEncrypt(msg,key)
        elif ch == 2:
            key = [int(i) for i in input('Enter the permutation sequence separated by a space:').split()]
            keyedDecrypt(msg,key)
        else:
            print('Invalid Choice')

    else:
        print('Invalid Choice')
        
if __name__ == '__main__':
    main()