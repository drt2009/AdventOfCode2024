from collections import defaultdict

filesystem_blocks = defaultdict(str)
checksum = 0
max_file_num = 0

def find_next_file_to_move(_search_start_location,_file_id):
    _is_counting = False
    for i in reversed(range(_search_start_location)):
        if not _is_counting and filesystem_blocks[i] == str(_file_id):
            _is_counting = True
            _ending_location_of_file = i
        elif _is_counting and filesystem_blocks[i] == str(_file_id):
            continue
        elif _is_counting and filesystem_blocks[i] != str(_file_id):
            _starting_location_of_file = i+1
            _is_counting = False
            break
    return (_starting_location_of_file,_ending_location_of_file)

def find_first_space_to_move_to(_end_search_location,_size_of_file):
    _is_counting = False
    _can_move = False
    _number_of_free_space = 0
    _starting_location_of_empty = 0
    for i in (range(_end_search_location)):
        if not _is_counting and filesystem_blocks[i] == '':
            _number_of_free_space = 0
            _is_counting = True
            _starting_location_of_empty = i
            _number_of_free_space+=1
        elif _is_counting and _number_of_free_space == _size_of_file:
            _can_move = True
            _is_counting = False
            break
        elif _is_counting and filesystem_blocks[i] == '':
            _number_of_free_space+=1
        elif _is_counting and filesystem_blocks[i] != '':
            _is_counting = False
        
    return (_can_move,_starting_location_of_empty)


def move_file(_file_to_move_starting,_free_space_starting,_file_size):
    global filesystem_blocks
    for i in range(_file_size):
        filesystem_blocks[_free_space_starting+i] = filesystem_blocks[_file_to_move_starting+i]
        filesystem_blocks[_file_to_move_starting+i] = ''


with open("day9.txt","r") as file:
    for line in file:
        file_number = 0
        block_location = 0
        is_file = True
        for i in range(len(line)):
            if is_file:
                for j in range(int(line[i])):
                    filesystem_blocks[block_location]=str(file_number)
                    block_location+=1
                is_file = False
                if(int(line[i])>0):
                    file_number+=1
            else:
                for j in range(int(line[i])):
                    filesystem_blocks[block_location]=""
                    block_location+=1
                is_file = True 
        max_file_num = file_number

last_checked_memory_location = len(filesystem_blocks.keys())
number_of_blocks_to_find = 0

for i in reversed(range(1,max_file_num)):
    file_to_move_starting,file_to_move_ending = find_next_file_to_move(last_checked_memory_location,i)
    file_to_move_size = file_to_move_ending - file_to_move_starting + 1
    can_move, free_space_starting = find_first_space_to_move_to(file_to_move_ending,file_to_move_size)
    if can_move:
        move_file(file_to_move_starting,free_space_starting,file_to_move_size)

for postion,file_id in filesystem_blocks.items():
    if(file_id.isdigit()):
        checksum+=postion*int(file_id)


print(checksum)