from code.unittestSingleton import test
#Digital Root
#---------------------------------------------------------
# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.
#---------------------------------------------------------
#solution
#------------

def digital_root(n):
    #parse the number into individual digits and sum them
    digital_sum=sum([int(num) for num in str(n)])
    #recursively call digital_root() until the sum is one digit
    while digital_sum>9:
        digital_sum=digital_root(digital_sum)
    return digital_sum
    

#sample tests
test.assert_equals(digital_root(16), 7)
test.assert_equals(digital_root(942), 6)
test.assert_equals(digital_root(132189), 6)
test.assert_equals(digital_root(493193), 2)