#importing random library
import random
#Generate 100 random numbers between 0 and 1000
randomList = random.sample(range(0, 1000), 100)
#print the list
print(randomList)

for i in range(len(randomList)):
    for j in range(i + 1, len(randomList)):
        if randomList[i] > randomList[j]:
            higherNumber = randomList[i]
            randomList[i] = randomList[j]
            randomList[j] = higherNumber

print(randomList)

totalOddNumbers = 0
countOddNumbers = 0
i = 0

for i in range(len(randomList)):

    # checking condition
    if (randomList[i] % 2) != 0:
        totalOddNumbers += randomList[i]
        countOddNumbers += 1
# increment i
i += 1
avgOddNumber = totalOddNumbers/countOddNumbers
print(avgOddNumber)

totalEvenNumbers = 0
countEvenNumbers = 0
i = 0
for i in range(len(randomList)):

# checking condition
    if (randomList[i] % 2) == 0:
        totalEvenNumbers += randomList[i]
        countEvenNumbers += 1
# increment i
        i += 1
avgEvenNumber = totalEvenNumbers/countEvenNumbers
print(avgEvenNumber)



