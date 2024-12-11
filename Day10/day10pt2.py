path_map = []
total_counts = 0 

def check_for_next_number(_current_x, _current_y):
    global path_map
    _current_number = path_map[_current_x][_current_y]
    _full_path = 0
    if _current_number == 9:
        return 1
    
    if _current_x-1 >= 0 and path_map[_current_x-1][_current_y] == _current_number+1:
        _full_path+=check_for_next_number(_current_x-1, _current_y)
    if _current_x+1 < len(path_map) and path_map[_current_x+1][_current_y] == _current_number+1:
        _full_path+=check_for_next_number(_current_x+1, _current_y)
    if _current_y-1 >= 0 and path_map[_current_x][_current_y-1] == _current_number+1:
        _full_path+=check_for_next_number(_current_x, _current_y-1)
    if _current_y+1 < len(path_map[_current_x]) and path_map[_current_x][_current_y+1] == _current_number+1:
        _full_path+=check_for_next_number(_current_x, _current_y+1)

    return _full_path


with open("day10.txt","r") as file:
    for line in file:
        path_map.append(list(map(int,list(line.strip()))))

for i in range(len(path_map)):
    for j in range (len(path_map[i])):
        if path_map[i][j] == 0:
            total_counts+=check_for_next_number(i,j)

print(total_counts)