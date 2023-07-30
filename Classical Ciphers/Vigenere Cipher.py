def encrypt(msg,key):
    enc = ''
    msg = msg.lower()
    key = key.lower()
    k = len(key)
    for i in range(len(msg)):
        if msg[i] not in 'qwertyuiopasdfghjklzxcvbnm':
                enc += msg[i]
        else:
                enc += chr( ( ( (ord(msg[i])-97) + (ord(key[i%k])-97) ) % 26) + 97 )
                
    print('Encrypted Text: ', enc)



def decrypt(msg,key):
    dec = ''
    msg = msg.lower()
    key = key.lower()

    k = len(key)
    for i in range(len(msg)):
        if msg[i] not in 'qwertyuiopasdfghjklzxcvbnm':
                dec += msg[i]
        else:
                dec += chr( ( ( (ord(msg[i])-97) - (ord(key[i%k])-97) ) % 26) + 97 )
                
    print('Decrypted Text: ', dec)
        
def main():
    print('MENU')
    print('Enter:\n1 for Encryption\n2 for Decryption')
    ch = int(input())
    msg = input('Enter the text: ')
    if(ch == 1):
        key = input('Enter the key(No special characters):')
        encrypt(msg,key)
    elif ch == 2:
        key = input('Enter the key(No special characters):')
        decrypt(msg,key)
    else:
        print('Invalid Choice')
        
if __name__ == '__main__':
    main()