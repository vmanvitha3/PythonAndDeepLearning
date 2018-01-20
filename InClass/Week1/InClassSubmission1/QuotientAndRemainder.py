#To Print Quotient and Remainder
import math
Fnum = input('Enter First Number: ')
Snum = input('Enter Second Number: ')

#Convert Strings to integers

num1 = int(Fnum)
num2 = int(Snum)

quotient = math.floor(num1 / num2);     #To Find Quotient and division in 3.6 version always returns float so we convert it to integer using math.floor()

rem = num1%num2;    #Find Remainder

print("Quotient is",quotient," Remainder is",rem)   #Print result