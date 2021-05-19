from code.unittestSingleton import test
#Hamming Numbers
#---------------------------------------------------------
# A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.
# Write a function that computes the nth smallest Hamming number.
#---------------------------------------------------------
#solution
#------------

#faster version
def hamming(num):
  #Make a list of size n, n-1 is the value we want to return.
    h = [1] * num
  #variables to represent 2^i, 3^j, 5^k
    x2, x3, x5 = 2,3,5
    i=0
    j=0
    k= 0
    for n in range(1, num):
    #Get the smallest number, multiply it buy 2, 3 or 5
        h[n] = min(x2, x3, x5)        
        if x2 == h[n]:
            i += 1
            x2 = 2 * h[i]
        if x3 == h[n]:
            j += 1
            x3 = 3 * h[j]
        if x5 == h[n]:
            k += 1
            x5 = 5 * h[k]
    return h[-1]

#compact version
def hamming(n):
    #initialize bases and exponents
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    #list to keep track of the lowest value through each iteration
    next_hamms = [2, 3, 5]
    for _ in range(1, n):
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            if next_hamms[i] == next_hamm:
                expos[i] += 1
                next_hamms[i] = bases[i] * hamms[expos[i]]
    return hamms[-1]

#sample tests
test.expect(hamming(1) == 1, "hamming(1) should be 1");
test.expect(hamming(2) == 2, "hamming(2) should be 2");
test.expect(hamming(3) == 3, "hamming(3) should be 3");
test.expect(hamming(4) == 4, "hamming(4) should be 4");
test.expect(hamming(5) == 5, "hamming(5) should be 5");
test.expect(hamming(6) == 6, "hamming(6) should be 6");
test.expect(hamming(7) == 8, "hamming(7) should be 8");
test.expect(hamming(8) == 9, "hamming(8) should be 9");
test.expect(hamming(9) == 10, "hamming(9) should be 10");
test.expect(hamming(10) == 12, "hamming(10) should be 12");
test.expect(hamming(11) == 15, "hamming(11) should be 15");
test.expect(hamming(12) == 16, "hamming(12) should be 16");
test.expect(hamming(13) == 18, "hamming(13) should be 18");
test.expect(hamming(14) == 20, "hamming(14) should be 20");
test.expect(hamming(15) == 24, "hamming(15) should be 24");
test.expect(hamming(16) == 25, "hamming(16) should be 25");
test.expect(hamming(17) == 27, "hamming(17) should be 27");
test.expect(hamming(18) == 30, "hamming(18) should be 30");
test.expect(hamming(19) == 32, "hamming(19) should be 32");