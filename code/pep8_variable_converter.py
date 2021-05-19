from code.unittestSingleton import test
#Pep8 Variable Converter
#---------------------------------------------------------
# Write simple pep8 variable converter method 
# All words must have a "_" between them.
#---------------------------------------------------------
#solution
#------------


def pep8_variable_converter(string):
    #for each word in the string, join the words by "_"
    pep8_string = '_'.join([word for word in string.split(' ')])


#sample tests
test.assert_equals(pep8_variable_converter("test case"), "test_case")
test.assert_equals(pep8_variable_converter("camel case method"), "camel_case_method")
test.assert_equals(pep8_variable_converter("say hello "), "say_hello")
test.assert_equals(pep8_variable_converter(" camel case word"), "camel_case_world")
test.assert_equals(pep8_variable_converter(""), "")