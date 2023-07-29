def encrypt(msg,a,b):
    enc = ''
    msg = msg.lower()
    for i in msg:
        if i not in 'qwertyuiopasdfghjklzxcvbnm':
                enc += i
        else:
                enc += chr((a*(ord(i)-97) + b ) % 26 +97)
                
    print('Encrypted Text: ', enc)



def decrypt(msg,a,b):
    dec = ''
    msg = msg.lower()
    invTable = [[1,1],[3,9],[5,21],[7,15],[9,3],[11,19],[15,7],[19,11],[21,5],[23,17],[25,25]]
    aInv = 0
    for i in range(11):
        if a == invTable[i][0]:
            aInv = invTable[i][1]
            break
    else:
        print('No Decryption for the given multiplication constant')
        return
    
    for i in msg:
        if i not in 'qwertyuiopasdfghjklzxcvbnm':
                dec += i
        else:
                dec += chr((aInv*((ord(i)-97) - b )) % 26 +97)
                
    print('Decrypted Text: ', dec)
        
def main():
    print('MENU')
    print('Enter:\n1 for Encryption\n2 for Decryption')
    ch = int(input())
    msg = input('Enter the text: ')
    if(ch == 1):
        a = int(input('Enter the multiplication constant:'))
        b = int(input('Enter the shift constant:'))
        encrypt(msg,a,b)
    elif ch == 2:
        a = int(input('Enter the multiplication constant:'))
        b = int(input('Enter the shift constant:'))
        decrypt(msg,a,b)
    else:
        print('Invalid Choice')
        
if __name__ == '__main__':
    main()