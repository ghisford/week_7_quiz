#4. Write a program that accepts a sentence and calculate 
# the number of upper case letters and lower case letters. 
# Suppose the following input is supplied to the program: 
# Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

def case_counter(any_string):
    UPPER_CASE = 0
    LOWER_CASE = 0
    list_str = list(any_string)
    for letter in list_str:
        if letter.isupper() == True:
            UPPER_CASE += 1
        else:
            LOWER_CASE += 1

    print(f'UPPER CASE : {UPPER_CASE} LOWER CASE: {LOWER_CASE}')

case_counter('Hi')