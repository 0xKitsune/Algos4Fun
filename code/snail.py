from code.unittestSingleton import test
#Snail
#---------------------------------------------------------
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.  
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
#---------------------------------------------------------
#solution
#------------

#using numpy
import numpy as np
def snail(array):
    res = []
    array = np.array(array)
    #add the top row to res, then drop the top row, rotate the array 90 degrees and create new array
    while len(array) > 0:
        res += array[0].tolist()
        array = np.rot90(array[1:])
    return res


#manual version
def snail(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        #get all of the items in the first row
        for i in range(col_begin, col_end+1):
            res.append(matrix[row_begin][i])
        row_begin += 1
        #get all of the items in the last column
        for i in range(row_begin, row_end+1):
            res.append(matrix[i][col_end])
        col_end -= 1
        #get all of the items in the last row if row_begin is not the last row
        if row_begin <= row_end:
            for i in range(col_end, col_begin-1, -1):
                res.append(matrix[row_end][i])
        row_end -= 1
        #get all of the items in the first column if col_begin is not the last column
        if col_begin <= col_end:
            for i in range(row_end, row_begin-1, -1):
                res.append(matrix[i][col_begin])
        col_begin += 1

    return res

#sample tests
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
test.assert_equals(snail(array), expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
test.assert_equals(snail(array), expected)