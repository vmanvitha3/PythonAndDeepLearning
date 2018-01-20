#Print FirstName and LastName in Reverse Order

FirstName = input('Enter First Name: ')
LastName = input('Enter Last Name: ')

fullName = FirstName+" "+LastName #Append last name to first name with a space in between
print(fullName)
reverseName = ""
j = len(fullName)
while j>0:  #iterate through the length of the name
    reverseName+=fullName[j-1]  #store name in reverse order
    j-=1

print ("Reversed Name is ",reverseName)