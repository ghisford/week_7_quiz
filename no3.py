#3. Write a function that takes a list of numbers and returns the largest number in the list.
def largest_func(num_list:list):
    largest = 0
    for num in num_list:
        if num > largest:
            largest = num

    return largest

print(largest_func([2,5,6,855]))