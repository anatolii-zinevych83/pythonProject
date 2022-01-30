#importing random library
import random
#Generate 100 random numbers between 0 and 1000
randomList = random.sample(range(0, 1000), 100)
#print the list
print(randomList)


#starting cycle until the end of the random list
for i in range(1, len(randomList)):
        #defining key as a list index
        key = randomList[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < randomList[j]:
            randomList[j+1] = randomList[j]
            j -= 1
        randomList[j+1] = key
#printing sorted list
print(randomList)

#defining the variables for total and count of odd numbers and index
totalOddNumbers = 0
countOddNumbers = 0
i = 0

#open the cycle from 0th index to the length of our list - 1
for i in range(len(randomList)):

    # checking if the number from the list is odd
    if (randomList[i] % 2) != 0:
        # adding found odd number to the sum of odd numbers
        totalOddNumbers += randomList[i]
        # incrementing the count of found odd numbers
        countOddNumbers += 1
# moving to next number in the list
i += 1

try:
    #calculating average odd number
    avgOddNumber = totalOddNumbers/countOddNumbers
    #printing average of odd numbers
    print(avgOddNumber)
except ZeroDivisionError:
    print("The division by zero is not allowed")

#defining the variables for total and count of even numbers and index
totalEvenNumbers = 0
countEvenNumbers = 0
j = 0

#open the cycle from 0th index to the length of our list - 1
for j in range(len(randomList)):

    # checking if the number from the list is even
    if (randomList[j] % 2) == 0:
        # adding found odd number to the sum of even numbers
        totalEvenNumbers += randomList[j]
        # incrementing the count of found even numbers
        countEvenNumbers += 1
# moving to next number in the list
        j += 1
try:
    #calculating average even number
    avgEvenNumber = totalEvenNumbers/countEvenNumbers
    #printing average of even numbers
    print(avgEvenNumber)
except ZeroDivisionError:
    print("The division by zero is not allowed")
