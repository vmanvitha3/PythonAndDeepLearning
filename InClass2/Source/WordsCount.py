#Python Program to Count the number of words in a file and print the output
f1 = "WordFrequencyList.txt"
try:    #if file exists it opens
    fh = open(f1)   #open file
    for line in fh:  #loop each line present in file
        count = 0     #Set count to zero
        for word in line.split():   #for each word in line after splitting line with respect to spaces
            count = count + 1     #increase count by 1 for each word
        print(line.strip("\n")," ",count)        #print the line along with word count value
except: #if no such file exists it throws an exception and exits
    print ("File cannot be opened",f1)
    exit()