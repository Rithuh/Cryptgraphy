def cryptanalysis(msg):
    decrypt=['' for i in range(26)]
    msg = msg.lower()
    print(msg)
    for i in range(26):
        for j in msg:
            if j not in 'qwertyuiopasdfghjklzxcvbnm':
                decrypt[i] += j
            else:
                decrypt[i] += chr(((ord(j)-97-i) % 26) + 97)
    
    for i in range(26):
        print(f'Key: {i}, Decrypted Text: {decrypt[i]}')

def encrypt(msg,key):
    enc = ''
    msg = msg.lower()
    for i in msg:
        if i not in 'qwertyuiopasdfghjklzxcvbnm':
                enc += i
        else:
                enc += chr(((ord(i)-97+key) % 26) + 97)
                
    print('Encrypted Text: ', enc)


def decrypt(msg,key):
    dec = ''
    msg = msg.lower()
    for i in msg:
        if i not in 'qwertyuiopasdfghjklzxcvbnm':
                dec += i
        else:
                dec += chr(((ord(i)-97-key) % 26) + 97)
                
    print('Decrypted Text: ', dec)
        
def main():
    print('MENU')
    print('Enter:\n1 for Encryption\n2 for Decryption\n3 for Cryptanalysis')
    ch = int(input())
    msg = input('Enter the text: ')
    if(ch == 1):
        key = int(input('Enter the key(Press 3 for Caeser Cipher):')) % 26
        encrypt(msg,key)
    elif ch == 2:
        key = int(input('Enter the key(Press 3 for Caeser Cipher):')) % 26
        decrypt(msg,key)
    elif ch == 3:
        cryptanalysis(msg)
    else:
        print('Invalid Choice')
        
if __name__ == '__main__':
    main()