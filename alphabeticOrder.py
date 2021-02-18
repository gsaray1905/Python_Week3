'''Write a function that takes an input of different words with hyphen (-)
 in between them and then: sorts the words in alphabetical order, adds 
 hyphen icon (-) between them, gives the output of the sorted words.'''

def words():# defining words function
    words=[n for n in input("Please enter the words with hyphen(-)"
                            "between words:").split('-')] #for loop for input
    words.sort()# to sort the words for alphabetic order
    print('-'.join(words)) #adding "-" between words

words() # running the function