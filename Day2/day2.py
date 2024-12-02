reports = []
validReports = 0

with open("day2.txt","r") as file:
    for line in file:
        linesplit = line.strip().split()
        lineSplitInt = [int(x) for x in linesplit]
        reports.append(lineSplitInt)

def is_decreasing_list(list, max_difference):
    _is_valid = True
    for i in range(len(list)-1):
        if(not (list[i] > list[i+1] and list[i] - list[i+1] < max_difference+1)):
            _is_valid = False
        if(not _is_valid):
            break
    return _is_valid

def is_increasing_list(list, max_difference):
    _is_valid = True
    for i in range(len(list)-1):
        if(not (list[i] < list[i+1] and list[i+1] - list[i] < max_difference+1)):
            _is_valid = False
        if(not _is_valid):
            break
    return _is_valid


for report in reports:
    if(is_decreasing_list(report,3) or is_increasing_list(report,3)):
        validReports+=1
            
print(validReports)
