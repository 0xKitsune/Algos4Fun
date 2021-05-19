from code.unittestSingleton import test
#Rail Fence Cipher
#---------------------------------------------------------
# Create two functions to encode and then decode a string using the Rail Fence Cipher. 
# This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". 
# First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. 
# Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.
#---------------------------------------------------------
#solution
#------------

def encode_rail_fence_cipher(string, n, get_rails=False):
    #init the amount of rails
    rails = [[] for i in range(n)]
    #separate string into rails
    sequence=[i for i in range(n)]+[i for i in range(1,n-1)][::-1]
    while len(string)>0:
        for i in sequence:
            if string!='':
                rails[i].append(string[0])
                string=string[1:]
    #join encoded rails
    encoded_rails=''
    for rail in rails:
        encoded_rails+=''.join(rail)  
    #return rails
    if get_rails:
        return rails
    else:
        return encoded_rails

def decode_rail_fence_cipher(string, n):
    #encode the string to get the necessary length of each rail
    rail_lengths=[len(result)for result in encode_rail_fence_cipher(string,n,get_rails=True)]
    #init rails for decoding
    rails=[]
    anchor=0
    for rail_length in rail_lengths:
        rails.append(string[anchor:rail_length+anchor])
        anchor+=rail_length
    #create decoded string
    sequence=[i for i in range(n)]+[i for i in range(1,n-1)][::-1]
    decoded_string=''
    while len(string)>0:
        for i in sequence:
            if rails[i]!='':
                decoded_string+=rails[i][0]
                rails[i]=rails[i][1:]
                string=string[1:]
    return decoded_string
        

    
    

#sample tests 
test.assert_equals(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3), "WECRLTEERDSOEEFEAOCAIVDEN");
test.assert_equals(encode_rail_fence_cipher("Hello, World!", 3), "Hoo!el,Wrdl l");
test.assert_equals(encode_rail_fence_cipher("WADCEDETCOEFROIREESVELANE", 3), "WECREEEACDTOFOREVLNDEEISA");
test.assert_equals(encode_rail_fence_cipher("", 3), "");


test.assert_equals(decode_rail_fence_cipher("H !e,Wdloollr", 4), "Hello, World!");
test.assert_equals(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3), "WEAREDISCOVEREDFLEEATONCE");
test.assert_equals(decode_rail_fence_cipher("", 3), "");

