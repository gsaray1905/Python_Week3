def isPalindrome(word):
     
    # Using predefined function to 
    # reverse to string print(s)
    reverseWord = ''.join(reversed(word))
 
    # Checking if both string are 
    # equal or not
    if (word == reverseWord):
        return True
    return False
 
# main function
word= input("Please enter a word to check, is it Palindrome?")
answer = isPalindrome(word)
 
if (answer):
    print("Yes")
else:
    print("No")
