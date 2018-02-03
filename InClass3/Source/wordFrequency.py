#Python program to count the frequency of each word in it using dictionary
#The words as keys should be in sorted manner in dictionary and Display it

#Take input from user
sentence = input("Enter a sentence: ")
countWord = dict()  #used built-in function to create an empty dictionary
for word in sentence.split(' '):    #Split input entered by user based on space and Loop through each word
    if word not in countWord:       #If word doesn't exist in dictionary add it and increase the count to 1
        countWord[word] = 1
    else:                           #If word exist in dictionary add increase count 1 to existing value
        countWord[word] = countWord[word]+1
#To print sorted dictionary based on keys using sorted method
print(dict(sorted(countWord.items())))