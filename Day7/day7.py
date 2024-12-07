from collections import defaultdict

callabration_outcomes = defaultdict(bool)
total_of_valid = 0

def try_opperations(_list_of_opperands,_target_total,_iteration,_current_total=0, _index=0):
    global callabration_outcomes

    if _index == (len(_list_of_opperands)):
        callabration_outcomes[( _target_total,_iteration)] = callabration_outcomes[( _target_total,_iteration)] or _current_total == _target_total
    elif _current_total > _target_total:
        return
    elif _index == 0 :
        try_opperations(_list_of_opperands, _target_total,_iteration,_current_total+_list_of_opperands[_index], _index+1)
    else:
        try_opperations(_list_of_opperands, _target_total,_iteration,_current_total* _list_of_opperands[_index], _index+1)
        try_opperations(_list_of_opperands, _target_total,_iteration,_current_total+ _list_of_opperands[_index], _index+1)

with open("day7.txt","r") as file:
    iteration = 0
    for line in file:
       callabration_value, callabration_opperands = line.strip().split(":")
       callabration_value = int(callabration_value)
       callabration_opperands = list(map(int,callabration_opperands.strip().split()))
       try_opperations(callabration_opperands,callabration_value,iteration)
       iteration+=1
count=0

for outcome, is_valid in callabration_outcomes.items():
    if is_valid:
        total_of_valid += outcome[0]
        count+=1

print(total_of_valid)
