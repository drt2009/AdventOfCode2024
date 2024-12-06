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
has_loop = False
previous_objects = list()
loop_count = 0


def is_movement_allowed(_x, _y, _direction):
    global previous_objects
    global has_loop

    _movement_pair = directions[_direction]
    _new_x = _x+_movement_pair[0]
    _new_y = _y+_movement_pair[1]
    if _new_x < 0 or _new_x >= len(workshop_floor):
        return True
    elif _new_y < 0 or _new_y >= len(workshop_floor[_new_x]):
        return True
    elif workshop_floor[_new_x][_new_y] == '#':
        if(((_new_x,_new_y),_direction) in previous_objects):
            has_loop = True
        previous_objects.append(((_new_x,_new_y),_direction))
        return False
    else:
        return True

def move_guard_and_check_for_extra_object(_x, _y, _direction):
    global has_left_floor
    global current_line
    global current_row
    global extra_object_places


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
            starting_line = x
            starting_row = line.index('^')
        x+=1




for x in range(len(workshop_floor)):
    for y in range(len(workshop_floor[x])):
        if workshop_floor[x][y] == '.':
            current_line = starting_line
            current_row = starting_row
            previous_objects = list()
            has_left_floor = False
            has_loop = False
            workshop_floor[x][y] = '#'
            current_direction = direction_order.index("N")
            while not has_left_floor and not has_loop:
                if is_movement_allowed(current_line,current_row, direction_order[current_direction]):
                    move_guard_and_check_for_extra_object(current_line,current_row, direction_order[current_direction])
                else:
                    current_direction = (current_direction+1) % 4
            workshop_floor[x][y] = '.'
            if has_loop:
                loop_count +=1

print(loop_count)
