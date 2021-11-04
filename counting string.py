# python counting occurrences of characters, words and numbers
#count spaces
string1 = 'hello world hope you are having a great day'.count(' ') # < how to count spaces within a string. space between
# the quotation marks allows python to count the amount of spaces there are within a string
print (string1) # to see your coding within the terminal you would need to print the variables that you have asssigned the value to
print ( 'count of spaces in string1 is {}'.format(string1.count(' '))) # this method allows you to create a string as
#as well as designate the answer within the string .count(' ') allows you to count spaces

#count letters
string2 = 'aaaabbbccccc' # once you have created the variable you are able to place the '.count()' function and place a letter within the
#brackets to allow python to count how many letters there are within the string
print(string2.count('b'))
#count numbers
list1 = [1,2,34,5,5,6,6,8,7,7,7,7]
print (list1.count('7'))
#count words
 string3 = 'hello world what a beautiful day day just just imagine'
 print (string3.count('day'))
