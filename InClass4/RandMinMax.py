import numpy as np

#matrix = np.random.randint(10,size=(10,10)) #Generate random numbers between 0 and 9
matrix = np.random.random((10,10)) #Generate any random numbers

print(matrix)

print("Minimum Value is ")
print(matrix.min()) #print minimum number

print("Maximum Value is ")
print(matrix.max()) #print maximum number


print("Minimum Value of each row is ")
print(matrix.min(axis=1))   #print an array containing minimum numbers in each row

print("Maximum Value of each row is ")
print(matrix.max(axis=1))   #print an array containing maximum numbers in each row