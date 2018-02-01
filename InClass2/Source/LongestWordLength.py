#Takes a list of words and returns the length of longest one
words_list = ["PHP","Exercises","Backend","Web Development"]  #List of words

#
word_len = []   #List to keep count of letters in each word
word_freq = []  #List which contains both the word and len of the word

#Iterates through each word in the list of words
for words in words_list:
    word_len.append(len(words))
    word_freq.extend([(len(words),words)])

print("List of words: ",words_list)
print("Length of words in the list: ",word_len)

sorted_list = sorted(word_freq)     #Sorted the list based on number of letters

print("Sorted list is ",sorted_list)


#Returns the last tuple
print("Last tuple in the list is ",sorted_list[-1:])