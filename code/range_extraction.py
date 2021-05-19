from code.unittestSingleton import test
#Range Extraction
#---------------------------------------------------------
# A format for expressing an ordered list of integers is to use a comma separated list of either individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
# The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. 
# For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
#---------------------------------------------------------
#solution
#------------

def range_extraction(args):
    # init extraction list
    extraction_list = []
    # init temporary holder list to store consecutive values
    holder = [args[0]]

    # for each number in args after the 0 position, check if the previous number is in the holder variable and if not, add the range to the extraction list
    for i in args[1:]:
        if i-1 in holder:
            holder.append(i)
        else:
            if len(holder) > 2:
                extraction_list.append(str(holder[0])+'-'+str(holder[-1]))
            else:
                [extraction_list.append(str(item)) for item in holder]
            holder = []
            holder.append(i)

    # after looping through args, if there are items in holder, get range and add them to extraction
    if len(holder) > 2:
        extraction_list.append(str(holder[0])+'-'+str(holder[-1]))
    else:
        [extraction_list.append(str(item)) for item in holder]

    return ','.join(extraction_list)

#sample tests
test.assert_equals(range_extraction([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
test.assert_equals(range_extraction([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')