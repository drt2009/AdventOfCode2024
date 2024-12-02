firstList = []
secondList = []

totalDifference = 0

with open("day1.txt","r") as file:
    for line in file:
        splitLine = line.strip().split("   ")
        firstList.append(int(splitLine[0]))
        secondList.append(int(splitLine[1]))
firstList.sort()
secondList.sort()



for i in range(len(firstList)):
   totalDifference += abs(firstList[i]-secondList[i])


print(totalDifference)