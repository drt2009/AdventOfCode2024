wordsearch = []

count_of_words = 0


with open("day4.txt","r") as file:
    for line in file:
        wordsearch.append(list(line))

def search_for_cross(_x,_y):
    if(_x-1 < 0 or _x+1 >=len(wordsearch)):
        return False
    elif(_y-1 <0 or _y+1 >=len(wordsearch[_x+1])):
        return False
    elif((wordsearch[_x-1][_y-1]=='M' and wordsearch[_x+1][_y+1]=='S') or (wordsearch[_x-1][_y-1]=='S' and wordsearch[_x+1][_y+1]=='M')):
        return (wordsearch[_x-1][_y+1]=='M' and wordsearch[_x+1][_y-1]=='S') or (wordsearch[_x-1][_y+1]=='S' and wordsearch[_x+1][_y-1]=='M')

        

for x in range(len(wordsearch)):
    for y in range(len(wordsearch[x])):
            if wordsearch[x][y] == 'A':
                 if(search_for_cross(x,y)):
                      count_of_words+=1

print(count_of_words)