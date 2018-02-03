#Use sets to count the number of vowels in a string
#Print vowels count even if they are duplicated
def countVowels(string,vowels): #function definition
    count = 0                   #set vowel count to 0
    for char in string:         #for each character within the user entered string we do the following
        if char in vowels:      #if character is in the set created for vowels
            count = count+1     #increase the count
    print("Count of vowels is ",count)  #Display vowel count

text = input("Enter String: ")  #Take input string from user

vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'} #vowels are stored in a a set

countVowels(text,vowels)    #call function by passing user text and vowel set that is defined above as arguments