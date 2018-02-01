# Read a file which contains one word in each line and Calculate the character frequency in each line
fName = "revisedWords.txt" #file in which words are stored

try:    #if file exists it opens
    fhandler = open(fName)
except: #if no such file exists it throws an exception and exits
    print ("File cannot be opened",fName)
    exit()
file = open("Output.txt", 'w')  #Open file in write mode
#it reads each word
for word in fhandler:
    word = word.strip()     #it strips new line characters and few others
    count_freq = 0         #creates an empty dictionary called count_freq
    for c in word:
        count_freq = count_freq + 1  #for each letter within the word increment count by 1 till no characters left
    data = word.strip("\n") +","+ str(count_freq)+"\n"  #Store output in a variable called data
    file.write(data)                 #write data to file
    #print (word.strip("\n"),",",count_freq)    #Prints result

file.close()        #close file