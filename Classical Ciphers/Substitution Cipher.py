def encrypt(msg,key):
    enc = ''
    msg = msg.lower()
    keys = {}
    for i in range(26):
        keys[chr(97+i)] = key[i]
    for i in msg:
        if i not in 'qwertyuiopasdfghjklzxcvbnm':
                enc += i
        else:
                enc += keys[i]
                
    print('Encrypted Text: ', enc)


def decrypt(msg,key):
    dec = ''
    msg = msg.lower()
    keys = {}
    for i in range(26):
        keys[key[i]] = chr(97+i)
    for i in msg:
        if i not in 'qwertyuiopasdfghjklzxcvbnm':
                dec += i
        else:
                dec += keys[i]
                
    print('Decrypted Text: ', dec)
        
def main():
    print('MENU')
    print('Enter:\n1 for Encryption\n2 for Decryption')
    ch = int(input())
    msg = input('Enter the text: ')
    if(ch == 1):
        key = input('Enter the key as a continous string starting from the corresponding subsitution for a:') 
        encrypt(msg,key)
    elif ch == 2:
        key = input('Enter the key as a continous string starting from the corresponding subsitution for a:')
        decrypt(msg,key)
    else:
        print('Invalid Choice')
        
if __name__ == '__main__':
    main()