#!/usr/bin/python

# Function definition is here

numbers = [1, 2, 3, 4]

# start numbersSum
numbersSum = sum(numbers)
print (numbersSum)

# start numbersmultSum
def multiplyList(myList) : 
    result = 1
    for x in myList: 
        result = result * x  
    return result  
print(multiplyList(numbers))
