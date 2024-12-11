import datetime

start_time = datetime.datetime.now()

stones = list

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
        stones = list(map(int,line.strip().split()))
    
    for i in range(25):
        new_stones = []
        for stone in stones:
            new_stones.extend(change_stone(stone))
        stones = new_stones.copy()
    print(len(stones))

end_time = datetime.datetime.now()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time}")
