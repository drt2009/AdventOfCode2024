firstList = []
secondList = []

similarityScore = 0

with open("day1.txt","r") as file:
    for line in file:
        splitLine = line.strip().split("   ")
        firstList.append(int(splitLine[0]))
        secondList.append(int(splitLine[1]))
firstList.sort()
secondList.sort()


for firstValue in firstList:
    sameNumberCount = 0
    for value in secondList:
        if value < firstValue:
            continue
        elif value == firstValue:
            sameNumberCount+=1
        else:
            break
    similarityScore+=firstValue*sameNumberCount
        


print(similarityScore)