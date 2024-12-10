path_map = list(list)



def check_for_next_number(_current_x, _current_y):
    global path_map
    if(path_map[_current_x][_current_y]== 9):
        return 1
    elif(_current_x+1<len(path_map) and _current_y+1<path_map[_current_x+1]):
        check_for_next_number(_current_x+1<len(path_map) and _current_y+1<path_map[_current_x+1])


with open("day10.txt","r") as file:
    for line in file:
        path_map.append(map(int,line.strip().split))