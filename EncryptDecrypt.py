def encrypt():
    print("Enter any string to Encrypt")
    var = input()
    encrypt = ""
    for letter in var:
        if letter == " ":
            encrypt += " "
        elif letter == 'Z' or letter == 'z':
            encrypt += chr(ord(letter)-25)
        else:
            encrypt += chr(ord(letter) + 1)
    print("Cipher text is : \n", encrypt)

def decrypt():
    print("Enter any string to Decrypt:")
    var = input()
    decrypt = ""
    for letter in var:
        if letter == " ":
            decrypt += " "
        elif letter == 'A' or letter == 'a':
            decrypt += chr(ord(letter)+25)
        else:
            decrypt += chr(ord(letter) - 1)

    print("Decrypted text is : \n", decrypt)





print("\nChoose the following Details")
print("Press 1 to Encrypt a Plain text to Cipher text")
print("Press 2 to Decrypt a Cipher text to Plain text")
press = int(input())
if press == 1:
    encrypte()
elif press == 2:
    decrypt()
else:
    print("Press only given choices number")
