from collections import defaultdict

all_antenna_locations = defaultdict(list)
antinode_locations = set()
max_line_number = 0
max_line_length = 0

def add_antinodes(_antenna_locations):
    global antinode_locations
    for i in range(len(_antenna_locations)):
        for j in range(i+1,len(_antenna_locations)):
            _x_diff = _antenna_locations[i][0] - _antenna_locations[j][0]
            _y_diff = _antenna_locations[i][1] - _antenna_locations[j][1]

            if(_antenna_locations[i][0]+_x_diff >= 0 
               and _antenna_locations[i][0]+_x_diff < max_line_number 
               and _antenna_locations[i][1]+_y_diff >=0 
               and _antenna_locations[i][1]+_y_diff < max_line_length):
                antinode_locations.add((_antenna_locations[i][0]+_x_diff,_antenna_locations[i][1]+_y_diff))

            if(_antenna_locations[j][0]-_x_diff >= 0 
               and _antenna_locations[j][0]-_x_diff < max_line_number 
               and _antenna_locations[j][1]-_y_diff >=0 
               and _antenna_locations[j][1]-_y_diff < max_line_length):
                antinode_locations.add((_antenna_locations[j][0]-_x_diff,_antenna_locations[j][1]-_y_diff))

with open("day8.txt","r") as file:
    line_number = 0
    for line in file:
        max_line_length = len(line.strip())
        for x in range(len(line.strip())):
            if line[x] != '.':
                all_antenna_locations[line[x]].append((line_number,x))
        line_number+=1
        max_line_number = line_number

for antenna_type, antenna_locations in all_antenna_locations.items():
    add_antinodes(antenna_locations)

print(antinode_locations)
print(len(antinode_locations))