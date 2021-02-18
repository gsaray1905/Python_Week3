'''Write a function that controls the given inputs whether 
they are equal to their reversed order or not.'''

def isPalindrome(word): # defining isPalindrome function
    reverseWord = ''.join(reversed(word))# getting reverse the word 
    if (word == reverseWord): # if word is equal to reverseWord
        return True # Return to True
    return False # Return False
 

word= input("Please enter a word" 
            "to check, is it Palindrome?")# to get an input from user
answer = isPalindrome(word) # to run word in isPalindrome function 
 
if (answer):
    print("Yes") # if it is True, Print-->Yes
else:
    print("No")# if not, print-->No
