import re
from collections import defaultdict

pages_before=defaultdict(set)
middle_number_sum = 0

order_expression = r"\d+\|\d+"

def validate_print_queue_line(_print_queue):
    global middle_number_sum
    _is_valid_order = True
    _split_page_queue = _print_queue.strip().split(',')
    for x in range(len(_split_page_queue)-1):
        if _split_page_queue[x] in pages_before.keys():
            _is_valid_order = not any(_page in pages_before[_split_page_queue[x]] for _page in _split_page_queue[x:])
        if(not _is_valid_order):
            break
    if _is_valid_order:
        middle_number_sum += int(_split_page_queue[int(len(_split_page_queue)/2)])


with open("day5.txt","r") as file:
    for line in file:
        if re.search(order_expression,line):
            page_before, page_after = map(str, line.strip().split("|"))
            pages_before[page_after].add(page_before)
        elif line == '\n':
            continue
        else:
            validate_print_queue_line(line)


print(middle_number_sum)