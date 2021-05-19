from code.unittestSingleton import test
#Counting Duplicates
#---------------------------------------------------------
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
#---------------------------------------------------------
#solution
#------------

def duplicate_count(text):
    #init count of duplicate characters and set text to lowercase
    duplicate_chars=0
    text=text.lower()
    for char in text:
        #if there is more than one occurence of the character
        if text.count(char)>1:
            duplicate_chars+=1
        #remove the character from the string
        text=text.replace(char,'')
    return duplicate_chars
    

#sample tests
test.assert_equals(duplicate_count(""), 0)
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdeaa"), 1)
test.assert_equals(duplicate_count("abcdeaB"), 2)
test.assert_equals(duplicate_count("Indivisibilities"), 2)