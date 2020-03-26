# DecodeCrypto is an open source software. Use this to decypher many strings!
import sys
import os
import webbrowser




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
BasicConvert(or bc)- preform a ceaser brute force
ReverseCrypto(or rc)- Read text backwords or unbackwords it
CryptoEncoder(or ce)- Encode text with a key
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

    else:
        print ("Invalid Syntax")
