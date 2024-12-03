total = 0

firstNumber = ''
secondNumber = ''

expectedChars = ['m','u','l','(','d',',','d',')']
currentExpectedCharPlace = 0


with open("day3.txt","r") as file:
    for line in file:
        for char in line:
            if(currentExpectedCharPlace==4 and char.isdigit()):
                firstNumber+=char
            elif((currentExpectedCharPlace==4 or currentExpectedCharPlace==6)  and expectedChars[currentExpectedCharPlace+1]== char):
                currentExpectedCharPlace+=2
            elif(currentExpectedCharPlace==6 and char.isdigit()):
                secondNumber+=char
            elif(expectedChars[currentExpectedCharPlace]==char):
                currentExpectedCharPlace+=1
            else:
                currentExpectedCharPlace=0
                firstNumber = ''
                secondNumber = ''
                
            
            if currentExpectedCharPlace == 8:
                currentExpectedCharPlace = 0
                print(firstNumber+'*'+secondNumber)
                total += int(firstNumber)*int(secondNumber)
                firstNumber = ''
                secondNumber = ''

print(total)
