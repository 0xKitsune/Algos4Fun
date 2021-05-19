from code.unittestSingleton import test

#Find The Missing Letter
#---------------------------------------------------------
# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.
# Example:
# ['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
#---------------------------------------------------------
#solution
#------------
import string

def find_missing_letter(chars):
    starting_position=0
    #find the position of the first letter in chars
    for i, val in enumerate(string.ascii_letters):
        if chars[0]==val: starting_position=i
    #get the correct slice with the missing letter
    slice_with_missing_letter=string.ascii_letters[starting_position:starting_position+len(chars)+1]
    #check to see which letter is missing and return it
    for char in slice_with_missing_letter:
        if char not in chars:
            return char


#sample tests
test.describe("kata tests")
test.it("example tests")
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')

