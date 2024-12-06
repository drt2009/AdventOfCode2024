directions = {
     "N": (-1,0),
     "E": (0,1),
     "S": (1,0),
     "W": (0,-1)
     }
direction_order = list(directions.keys())
current_direction = direction_order.index("N")


workshop_floor = []

current_line = 0
current_row = 0

has_left_floor = False
floor_tiles_through = set()

def is_movement_allowed(_x, _y, _direction):
    _movement_pair = directions[_direction]
    _new_x = _x+_movement_pair[0]
    _new_y = _y+_movement_pair[1]
    if _new_x < 0 or _new_x >= len(workshop_floor):
        return True
    elif _new_y < 0 or _new_y >= len(workshop_floor[_new_x]):
        return True
    elif workshop_floor[_new_x][_new_y] == '#':
        return False
    else:
        return True

def move_guard(_x, _y, _direction):
    global has_left_floor
    global current_line
    global current_row


    _movement_pair = directions[_direction]
    _new_x = _x+_movement_pair[0]
    _new_y = _y+_movement_pair[1]
    if _new_x < 0 or _new_x >= len(workshop_floor):
        has_left_floor = True
    elif _new_y < 0 or _new_y >= len(workshop_floor[_new_x]):
        has_left_floor = True
    else:
        current_line = _new_x
        current_row = _new_y


with open("day6.txt","r") as file:
    x = 0
    for line in file:
        workshop_floor.append(list(line.strip()))
        if '^' in line:
            current_line = x
            current_row = line.index('^')
            floor_tiles_through.add((current_line,current_row))
        x+=1

while not has_left_floor:
    if is_movement_allowed(current_line,current_row, direction_order[current_direction]):
        move_guard(current_line,current_row, direction_order[current_direction])
        floor_tiles_through.add((current_line,current_row))
    else:
        current_direction = (current_direction+1) % 4

print(len(floor_tiles_through))
# print(workshop_floor)


