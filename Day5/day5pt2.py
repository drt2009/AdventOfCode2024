import re
from collections import defaultdict

pages_before=defaultdict(set)
rules= []
middle_number_sum = 0


order_expression = r"\d+\|\d+"

def resortList(_list):
    _has_been_changed = True
    while _has_been_changed:
        _has_been_changed = False
        for rule in rules:
            if rule[0] in _list and  rule[1] in _list:
                if _list.index(rule[0]) > _list.index(rule[1]):
                    _list.remove(rule[0])
                    _list.insert(_list.index(rule[1]), rule[0])
                    _has_been_changed = True
    return _list        

def validate_print_queue_line(_print_queue):
    global middle_number_sum
    _is_valid_order = True
    _split_page_queue = _print_queue.strip().split(',')
    for x in range(len(_split_page_queue)-1):
        if _split_page_queue[x] in pages_before.keys():
            _is_valid_order = not any(_page in pages_before[_split_page_queue[x]] for _page in _split_page_queue[x:])
        if(not _is_valid_order):
            _resorted_list = resortList(_split_page_queue)
            middle_number_sum += int(_resorted_list[int(len(_resorted_list)/2)])


with open("day5.txt","r") as file:
    for line in file:
        if re.search(order_expression,line):
            page_before, page_after = map(str, line.strip().split("|"))
            pages_before[page_after].add(page_before)
            rules.append((page_before,page_after))
        elif line == '\n':
            continue
        else:
            validate_print_queue_line(line)

print(middle_number_sum)