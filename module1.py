
def remove_vowels(sentence: str):
    new_sentence = ""
    for ch in sentence:
        if ch not in ("a", "e", "i", "o", "u"):
            new_sentence += ch
    return new_sentence

def replace_space_with_underscore(sentence: str):
    new_sentence = ""
    for ch in sentence:
        if ch == " ":
            new_sentence += "_"
        else:
            new_sentence += ch
    return new_sentence

def convert_to_title_case(sentence:str):
    new_sentence = ""
    for index, ch in enumerate(sentence):
        if index == 0:
            new_sentence+=str.upper(ch)
        elif sentence[index -1] == "_":
            new_sentence += str.upper(ch)
        else:
            new_sentence += ch
    return new_sentence

def clean_string(sentence: str):
    return(convert_to_title_case(
        replace_space_with_underscore(
            remove_vowels(sentence)
        )
    ))

def total_sales_per_product(products: list):
    final_list = {}
    for product in products:
        if product["product"] in final_list:
            final_list[product["product"]] += product["amount"]
        else:
            final_list[product["product"]] = product["amount"]

    for item, count in final_list.items():
        print(item, ":", count)


def unique_number_in_list(mylist: list):
    unique_num = set()
    all_element = set()
    for num in mylist:
        if num not in all_element:
            all_element.add(num)
            unique_num.add(num)
        else:
            if num in unique_num:
                unique_num.remove(num)
    return list(unique_num)


def reverse_string(mystring: str):
    reversed_string = ""
    for ch in reversed(mystring):
        reversed_string +=ch
    return reversed_string

def check_anagrams(string1, string2):
    string1_char = char_in_string(string1)
    string2_char = char_in_string(string2)

    if string1_char == string2_char:
        return True
    else:
        return False

def char_in_string(string : str):
    my_char_list = [char for char in string]
    char_count = {}
    for char in my_char_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def remove_duplicate_characters(value: str):
    char_in_input = [ch for ch in value]
    word_without_duplicate = ""
    unique_word = set()
    for ch in char_in_input:
        if ch not in unique_word:
            word_without_duplicate += ch
            unique_word.add(ch)
    return word_without_duplicate
