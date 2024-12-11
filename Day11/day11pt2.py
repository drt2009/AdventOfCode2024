from collections import defaultdict

import datetime

start_time = datetime.datetime.now()


stones = defaultdict(int)

def change_stone(_stone):
    if _stone == 0:
        return [1]
    elif len(str(_stone))%2==0:
        _string_stone = str(_stone)
        _half_length = len(_string_stone)//2
        _stone_1 = _string_stone[:_half_length]
        _stone_2 = _string_stone[_half_length:]
        return [int(_stone_1),int(_stone_2)]
    else:
        return [_stone*2024]

with open("day11.txt","r") as file:
    for line in file:
        for stone in list(map(int,line.strip().split())):
            stones[stone]+=1
    
        for i in range(9999):
            new_stones = defaultdict(int)
            for stone, frequency in stones.items():
                for new_stone in change_stone(stone):
                    new_stones[new_stone]+=frequency
            stones = new_stones.copy()
        total_stones = 0
        for stone, frequency in stones.items():
            total_stones+=frequency
        print(total_stones)

end_time = datetime.datetime.now()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time}")

