from code.unittestSingleton import test
#Twice Linear
#---------------------------------------------------------
# Consider a sequence u where u is defined as follows:

# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Example:
# u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

# Task:
# Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered sequence u (ordered with < so there are no duplicates).


#---------------------------------------------------------
#solution
#------------


def dbl_linear(n):
    num_list = [1]
    for i in num_list:
        num_list.append((i * 2) + 1)
        num_list.append((i * 3) + 1)
        if len(num_list) > n *10:
            break
    return sorted(list(set(num_list)))[n]