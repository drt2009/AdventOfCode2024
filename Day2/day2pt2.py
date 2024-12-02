reports = []
validReports = 0

with open("day2.txt","r") as file:
    for line in file:
        linesplit = line.strip().split()
        lineSplitInt = [int(x) for x in linesplit]
        reports.append(lineSplitInt)

def is_decreasing_list(list, max_difference,retry_allowed):
    _is_valid = True
    for i in range(len(list)-1):
        if(not (list[i] > list[i+1] and list[i] - list[i+1] < max_difference+1)):
            _is_valid = False
        if(not _is_valid and retry_allowed):
            list1 = list.copy()
            list2 = list.copy()
            del list1[i]
            del list2[i+1]
            _is_valid = is_decreasing_list(list1, max_difference, False) or is_decreasing_list(list2, max_difference, False)
        if(not _is_valid):
            break
    return _is_valid

def is_increasing_list(list, max_difference, retry_allowed):
    _is_valid = True
    for i in range(len(list)-1):
        if(not (list[i] < list[i+1] and list[i+1] - list[i] < max_difference+1)):
            _is_valid = False
        if(not _is_valid and retry_allowed):
            list1 = list.copy()
            list2 = list.copy()
            del list1[i]
            del list2[i+1]
            _is_valid = is_increasing_list(list1, max_difference, False) or is_increasing_list(list2, max_difference, False)
        if(not _is_valid):
            break
    return _is_valid


for report in reports:
    if(is_decreasing_list(report,3,True) or is_increasing_list(report,3,True)):
        validReports+=1
            
print(validReports)