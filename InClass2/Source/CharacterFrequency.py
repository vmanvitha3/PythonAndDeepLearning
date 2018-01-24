# Read a file which contains one word in each line and Calculate the character frequency in each line
fName = "words.txt" #file in which words are stored

try:    #if file exists it opens
    fhandler = open(fName)
except: #if no such file exists it throws an exception and exits
    print ("File cannot be opened",fName)
    exit()

#it reads each word
for word in fhandler:
    word = word.strip()     #it strips new line characters and few others
    count_freq = dict()         #creates an empty dictionary called count_freq
    for c in word:
        if c not in count_freq:     #for each letter within the word do the following
            count_freq[c]=1         #if letter of word is not available in dictionary it adds to the dictionary
        else:
            count_freq[c] = count_freq[c] + 1   #if letter of word is available in dictionary it just increases count
    print ("Word is ",word)
    print("Frequency of word is ",count_freq)   #Prints result