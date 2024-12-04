wordsearch = []
lookup_word = list('XMAS')

directions = {
     "N": (-1,0),
     "NE": (-1,1),
     "E": (0,1),
     "SE": (1,1),
     "S": (1,0),
     "SW": (1,-1),
     "W": (0,-1),
     "NW": (-1,-1)
     }

count_of_words = 0


with open("day4.txt","r") as file:
    for line in file:
        wordsearch.append(list(line))

def search_in_direction(_x,_y,_current_letter_search_index,_direction):
    _new_x = _x+_direction[0]
    _new_y = _y+_direction[1]
    

    if(_current_letter_search_index<4):
        if(_new_x < 0 or _new_x >=len(wordsearch)):
            return False
        elif(_new_y <0 or _new_y>=len(wordsearch[_new_x])):
            return False
        elif(wordsearch[_new_x][_new_y]==lookup_word[_current_letter_search_index]):
            return search_in_direction(_new_x,_new_y,_current_letter_search_index+1,_direction)
    elif(_current_letter_search_index == 4):
        return True 
    else:
        return False
          

def search_for_word(_x,_y,_current_letter_search_index):
    global count_of_words
    for direction in directions:
         if(search_in_direction(_x,_y,_current_letter_search_index,directions[direction])):
              print("found: " +str(_x) + " " + str(_y) + " " + direction)
              count_of_words+=1




for x in range(len(wordsearch)):
    for y in range(len(wordsearch[x])):
            if wordsearch[x][y] == 'X':
                 search_for_word(x,y,1)

print(count_of_words)