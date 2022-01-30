#importing random library
import random
#generating 100 random numbers between 0 and 1000
randomList = random.sample(range(0, 1000), 100)
#printing the list
print(randomList)

#for i in range(len(randomList)):
    #for j in range(i + 1, len(randomList)):
       # if randomList[i] > randomList[j]:
        #    higherNumber = randomList[i]
         #   randomList[i] = randomList[j]
           # randomList[j] = higherNumber

#print the list
#print(randomList)

#defining sorted list
sortedList = []

#starting cycle until the end of the random list
while randomList:
    #defining variable value as 1st number in the list
    minimum = sortedList[0]
    #opening cycle to compare numbers one by one
    for x in randomList:
        #comparing value from random list with current minimum
        if x < minimum:
            #writing x value to minimum variable
            minimum = x
    #writing value to sorted list
    sortedList.append(minimum)
    #removing value from random list
    randomList.remove(minimum)
#printing sorted list
print(sortedList)

#defining the variables for total and count of odd numbers and index
totalOddNumbers = 0
countOddNumbers = 0
i = 0

#open the cycle from 0th index to the length of our list - 1
for i in range(len(sortedList)):

    # checking if the number from the list is odd
    if (sortedList[i] % 2) != 0:
        #adding found odd number to the sum of odd numbers
        totalOddNumbers += sortedList[i]
        #incrementing the count of found odd numbers
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
for j in range(len(sortedList)):

    # checking if the number from the list is even
    if (sortedList[j] % 2) == 0:
        # adding found odd number to the sum of even numbers
        totalEvenNumbers += sortedList[j]
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




