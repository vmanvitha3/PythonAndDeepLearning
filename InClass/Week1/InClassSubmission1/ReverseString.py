#Print FirstName and LastName in Reverse Order

FirstName = input('Enter First Name: ')
LastName = input('Enter Last Name: ')

fullName = FirstName+" "+LastName
print(fullName)
reverseName = ""
i = len(fullName)
while i>0:
    reverseName+=fullName[i-1]
    i-=1

print ("Reversed Name is ",reverseName)