#This function takes in an input and determines if the string has unique characters
#Additionally, this solution take O(1), or constant, space complexity O(n) time complexity

def isUnique(word):
    if len(word) > 128:
        return False

    #Initialize empty character dictionary
    booleanList = [False] * 128

    #Iterate once through word, O(n)
    for char in word:
        val = ord(char) #Find ASCII equivalent to char
        if booleanList[val]:
            return False
        else:
            booleanList[val] = True

    return True

#Take user input
word = input("Please input a string to determine if each character is unique:")

#Determine based on flag
if isUnique(word):
    print "Your word has unique characters"
else:
    print "Your word does not have unique characters"
