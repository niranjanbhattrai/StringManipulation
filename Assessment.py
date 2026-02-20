def char_in_string(string : str):
    my_char_list = [char for char in string]
    char_count = {}
    for char in my_char_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def non_repeat_char(string):
    string_counts = char_in_string(string)
    for ind, ch in enumerate(string):
        if string_counts[ch] == 1:
            return ind
    return -1

def compress_using_count(string):
    string_count = char_in_string(string)
    for item,val in string_count.items():
        print(item+str(val),end ='')



