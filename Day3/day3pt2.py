total = 0

firstNumber = ''
secondNumber = ''

expectedChars = ['m','u','l','(','d',',','d',')']
currentExpectedCharPlace = 0
isEnabled = True
opperation = ''

def check_for_do(_chars_to_check):
    return _chars_to_check == "do()"

def check_for_dont(_chars_to_check):
    return _chars_to_check == "don't()"

def check_for_mul(_chars_to_check):
    return _chars_to_check.startswith('mul(')

def process_mul(_opperation):
    _mul_parts = _opperation[4:len(_opperation)-1].split(",")

    if(_mul_parts[0].isdigit() and _mul_parts[1].isdigit()):
        global total 
        total+=int(_mul_parts[0])*int(_mul_parts[1])


def process_opperation(_opperation,_is_enabled):
    if(_is_enabled):
        if(check_for_mul(_opperation)):
            process_mul(_opperation)
        elif(check_for_dont(_opperation)):
            _is_enabled=False
    else:
        _is_enabled = check_for_do(_opperation)
    return _is_enabled

    


with open("day3.txt","r") as file:
    for line in file:
        for char in line:
            if(char == 'm' or char == 'd'):
                opperation=''
                opperation+=char
            elif(opperation!=")"):
                opperation+=char
                if(char == ')'):
                    isEnabled=process_opperation(opperation,isEnabled)
                    opperation = ''
                
print (total)

