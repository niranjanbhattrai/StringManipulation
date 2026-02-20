from Assessment import non_repeat_char, compress_using_count
from module1 import reverse_string, check_anagrams, clean_string, total_sales_per_product, \
    unique_number_in_list, remove_duplicate_characters

if __name__ == "__main__":
    '''
    test_sentence  = "data engineering rocks"
    print(clean_string(test_sentence))

    sales = [
        {"product": "Pen", "amount": 10},
        {"product": "Book", "amount": 20},
        {"product": "Pen", "amount": 15},
        {"product": "Pencil", "amount": 5}
    ]

    total_sales_per_product(sales)

    input_list = [4,5,4,6,7,5,8]
    print(unique_number_in_list(input_list))

    print(reverse_string(test_sentence))

    string1 = "listen"
    string2 = "silent"
    if check_anagrams(string1, string2):
        print("True")
    else:
        print("False")

    input1 = "programming"
    print(remove_duplicate_characters(input1))
    '''
    print(non_repeat_char("sswwiibss"))
    compress_using_count("sswibbss")