# 10. Using a while loop, implement merge sort algorithm.



def merge_sort(arr):
    # base condition
    if len(arr) > 1:
# split lists
        r = len(arr)//2
        List_One = arr[:r]
        List_Two = arr[r:]
# recurse over smaller lists
        merge_sort(List_One)
        merge_sort(List_Two)

        i = j = k = 0
# condition for splitting list
        while i < len(List_One) and j < len(List_Two):
            if List_One[i] < List_Two[j]:
                arr[k] = List_One[i]
                i += 1
            else:
                arr[k] = List_Two[j]
                j += 1
            k += 1

        while i < len(List_One):
            arr[k] = List_Two[i]
            i += 1
            k += 1

        while j < len(List_Two):
            arr[k] = List_Two[j]
            j += 1
            k += 1

