from code.unittestSingleton import test
#Hashtag Generator
#---------------------------------------------------------
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
#---------------------------------------------------------
#solution
#------------


def generate_hashtag(s):
    hashtag='#'
    #if string is not empty and less than 140 characters
    if s!='' and len(s)<=140:
        #separate into words
        words=list(s.split(' '))
        #capitalize each word and concat it with hashtag
        for word in words:
            if word!='':
                hashtag+=word[0].upper()+word[1:].lower()
        return hashtag           
    else:
        return False

#sample tests
test.assert_equals(generate_hashtag(''), False, 'Expected an empty string to return False')
test.assert_equals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
test.assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
test.assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
test.assert_equals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
test.assert_equals(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')