from code.unittestSingleton import test
#Counting car mileage
#---------------------------------------------------------
# Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).
# It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

# "Interesting" Numbers
# Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

# Any digit followed by all zeros: 100, 90000
# Every digit is the same number: 1111
# The digits are sequential, incementing†: 1234
# The digits are sequential, decrementing‡: 4321
# The digits are a palindrome: 1221 or 73837
# The digits match one of the values in the awesome_phrases array
#---------------------------------------------------------
#solution
#------------
import re
def check_patterns(number,awesome_phrases):
    match=False
    number=str(number)
    if len(number)>2:
        #init patterns and add awesome phrases to regex patterns
        patterns= ['^\d0+$', '^(\d)\1+$']
        [patterns.append(str(pattern)) for pattern in awesome_phrases]
        #check regex patterns
        if any(re.match(regex, number) for regex in patterns):
            match=True
        #check increment
        if number in '1234567890':
            match=True
        #check decrement
        elif number in '9876543210':
            match=True
        #check palindrome
        elif number==number[::-1]:
            match=True
    return match

def is_interesting(number, awesome_phrases):
    match=0   
    #check if 2
    if check_patterns(number=number, awesome_phrases=awesome_phrases) ==True:
        match=2
    #check if 1
    else:
        for i in range(number+1, number+3):
            if check_patterns(number=i, awesome_phrases=awesome_phrases):
                match=1 
    return match

        

#sample tests
tests = [
	{'n': 3, 'interesting': [1337, 256], 'expected': 0},
	{'n': 1336, 'interesting': [1337, 256], 'expected': 1},
	{'n': 1337, 'interesting': [1337, 256], 'expected': 2},
	{'n': 11208, 'interesting': [1337, 256], 'expected': 0},
	{'n': 11209, 'interesting': [1337, 256], 'expected': 1},
	{'n': 11211, 'interesting': [1337, 256], 'expected': 2},
]
for t in tests:
	test.assert_equals(is_interesting(t['n'], t['interesting']), t['expected'])