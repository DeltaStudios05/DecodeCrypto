# DecodeCrypto is an open source software. Use this to decypher many strings!
import sys
import os
import webbrowser
import code
import itertools
import time


print (""" 
---------- DecodeCrypto ----------
Use 'help' or '?' for a help menu

""")
# Start
def version ():
    print ("v.1")

def helpquestion ():
    print ("""
Commands:

version- Check the version
help(or ?)- A help menu. This is what you see now
exit- exit the program
openweb- Open a Website
openwebinfinty - forever open a website
BasicConvert(or bc)- preform a ceasez brute force
ReverseCrypto(or rc)- Read text backwords or unbackwords it
CryptoEncoder(or ce)- Encode text with a key
CryptoPassword(or cp)- Pick a format to encode/decode
print(or printr)- prints a statment 
    """)

def exit ():
     sys.exit()

def BasicConvert ():
    chars = "abcdefghijklmnopqrstuvwxyz"
    rot1 = str.maketrans(chars, chars[1:]+chars[0])

    message = input("Enter the encoded message: ")

    for i in chars:
        print(message)
        message = message.translate(rot1)



def ReverseCrypto ():
    print ("""
1) Decode reverse text (Example: olleH ---> Hello)
2) Encode reverse text (Example: Hello ---> olleH)
    """)
    ReverseOption = input("Pick a Number: ")
    if ReverseOption == "1":
        print ("Good Luck!!!!")
        CryptoText = input("Enter a String: ")
        print ("Old Cipher: " + CryptoText)
        print ("|")
        print ("|")
        print ("|")
        print ("\/")
        CryptoLast = CryptoText[::-1]
        print ("New Cipher: " + CryptoLast)

    elif ReverseOption == "2":
        print ("Enjoy Your Hideaway!!!")
        CryptoText = input("Enter a String: ")
        print ("Old Cipher: " + CryptoText)
        print ("|")
        print ("|")
        print ("|")
        print ("\/")
        CryptoLast = CryptoText[::-1]
        print ("New Cipher: " + CryptoLast)

    else:
        print ("Syntax Error: Did you enter a number?")

def OpenWeb ():
    WEBSITE = "NULL"
    WEBSITE = input("Enter URL: ")
    webbrowser.open(WEBSITE)

def OpenWebInfinty ():
    WEBSITE = "NULL"
    WEBSITE = input("Enter URL: ")
    while True:
        webbrowser.open(WEBSITE)

def CryptoEncoder ():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = input("Enter a Key: ")
    newmessage = ''

    message = input("Enter Your Message: ")
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newpostiton = (position + int(key)) % 26
            newcharacter = alphabet[newpostiton]
            print ("The New Character is: ", newcharacter)
            newmessage += newcharacter
            print(newmessage)

        else:
            newmessage += character

def CryptoPassword ():
    InputPass = input("Encode or Decode?\n")
    if InputPass.lower() == "encode":
        plaintext = input("Enter your raw text: ")
        encodingformat = input("Enter your ecoding format: ")
        try:
            encodedmessage = plaintext.encode(encodingformat, "replace")
            print (encodedmessage)
        except:
            print ("Unknown encoding format")

    elif InputPass.lower() == "decode":
        encodedtext = input("Enter your encoded message: ")
        decodingformat = input("Enter a decoding format: ")
        try:
            decodedmessage = encodedtext.decode(decodingformat, "replace")
            print (str(decodedmessage))
        except:
            print ("Unknown encoding format")
    else:
        print ("An Error Ocuured (Did you say encode or decode?))")


def printf ():
    printt = 0
    printw = input("print what: ")
    while True:
        print (printw)
        printt = printt + 1
        print (printt)
    
def printr ():
    printw = input("print what: ")
    print (printw)
# End
while True:
    User_Input = input('Crypto@Root: ')

    if User_Input.lower() == "version":
        version()
    
    if User_Input.lower() == "help" or User_Input.lower() == "?":
        helpquestion()

    elif User_Input.lower() == "exit":
        exit()

    elif User_Input.lower() == "basicconvert" or User_Input.lower() == "bc":
        BasicConvert()

    elif User_Input.lower() == "reversecrypto" or User_Input.lower() == "rc":
        ReverseCrypto()

    elif User_Input.lower() == "openweb":
        OpenWeb()

    elif User_Input.lower() == "openwebinfinty":
         OpenWebInfinty()

    elif User_Input.lower() == "cryptoencoder" or User_Input.lower() == "ce":
        CryptoEncoder()

    elif User_Input.lower() == "cryptopassword" or User_Input.lower() == "cp":
        CryptoPassword()

    elif User_Input.lower() == "print":
        printr()

    elif User_Input.lower():
        printf()

    else:
        print ("Invalid Syntax")
