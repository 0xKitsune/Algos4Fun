from code.unittestSingleton import test
#Count bits
#---------------------------------------------------------
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
# You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
#---------------------------------------------------------
#solution
#------------

def count_bits(n):
    #convert the number to binary with bin() and use count(substring) to find how many '1's in the binary conversion
    return bin(n).count('1')


#not using bin()
def manual_count_bits(n):
    #init binary and quotient values
    binary=''
    quotient=n
    #while the quotient is greater than 0, get the binary value
    while quotient>0:
        remainder=str(quotient%2)
        quotient=int(quotient/2)
        binary+=remainder
    #return the number of '1's in the final binary value
    return binary.count('1')

#sample tests
test.assert_equals(count_bits(0), 0)
test.assert_equals(count_bits(4), 1)
test.assert_equals(count_bits(7), 3)
test.assert_equals(count_bits(9), 2)
test.assert_equals(count_bits(10), 2)