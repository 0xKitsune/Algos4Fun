from code.unittestSingleton import test
#Explosive Sum
#---------------------------------------------------------
# In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. 
# Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. 
# For example, 4 can be partitioned in five distinct ways.  Write a function to find the amount of ways to partition an integer.
#---------------------------------------------------------
#solution
#------------

def exp_sum(n):
    if n < 0:
        return 0
    dp = [1]+[0]*n
    #n+1 to inlcude the number itself as a soution
    for num in range(1,n+1):
        for i in range(num,n+1):
            dp[i] += dp[i-num]
    return dp[-1]

#sample tests
test.assert_equals(exp_sum(1), 1)
test.assert_equals(exp_sum(2), 2)
test.assert_equals(exp_sum(3), 3)
test.assert_equals(exp_sum(4), 5)
test.assert_equals(exp_sum(5), 7)
test.assert_equals(exp_sum(10), 42)