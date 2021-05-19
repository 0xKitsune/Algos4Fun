from code.unittestSingleton import test
#Rotate by 13 places
#---------------------------------------------------------
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
# ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, they should be returned as they are. 
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
#---------------------------------------------------------
#solution
#------------

import string

def rot13(message):
    ciphered = ''
    alphabet=[char for char in string.ascii_lowercase]
    for char in message:
        try:
            rot13_position=alphabet.index(char.lower())+13
            #if the adjusted position is outside the length of alphabet, go back to the beginning
            if rot13_position>25:
                rot13_position=rot13_position-26
            #if char is uppercase, return rot13 in uppercase
            if char.isupper():
                ciphered+=alphabet[rot13_position].upper()
            else:
                #if the character is not in the alphabet, add it to ciphered as it is
                ciphered+=alphabet[rot13_position]
        except:
            ciphered+=char
    return ciphered

#sample tests
test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")