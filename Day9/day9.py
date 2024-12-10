from collections import defaultdict

filesystem_blocks = defaultdict(str)
checksum = 0

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


with open("day9PreSort.txt","w") as file:
    for key,value in filesystem_blocks.items():
        file.write(str(key)+"                        "+value+"\n")


current_empty = 0
last_full = len(filesystem_blocks.keys());
while(current_empty<last_full):
    for i in range(current_empty,len(filesystem_blocks.keys())):
        if(filesystem_blocks[i]==""):
            current_empty = i
            break

    for j in reversed(range(current_empty,last_full)):
        if(filesystem_blocks[j]!=""):
            last_full = j
            break

    if(j<=i):
        break    
    
    if(current_empty<last_full):
        filesystem_blocks[current_empty]=filesystem_blocks[last_full]
        filesystem_blocks[last_full]=""

with open("day9Map.txt","w") as file:
    for key,value in filesystem_blocks.items():
        file.write(str(key)+"                        "+value+"\n")

for postion,file_id in filesystem_blocks.items():
    if(file_id==""):
        break
    checksum+=postion*int(file_id)

print(checksum)