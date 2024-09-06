#               array
# [0 .. .. .. .. mid .. .. .. .. high-1] `high`
def binary_search(ordered_list, item_to_find):
    low_index = 0
    high_index = len(ordered_list) - 1

    while low_index <= high_index: # check the range of the array is more than one
        mid_index = (low_index + high_index) // 2 # new mid of the array
        guess_item = ordered_list[mid_index]
        if guess_item == item_to_find:
            return mid_index # return position of the item_to_find
        if guess_item > item_to_find:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return None # item_to_find doesn't exist


my_list = [1,3,5,7,9,11,13]
print(f"Ordered list introduced: [1,3,5,7,9,11,13]")
result = binary_search(my_list, 3)
if result is not None:
    print(f"Index of item 3 is {result}")
else:
    print("Item not found")


result = binary_search(my_list, -1)
if result is not None:
    print(f"Index of item is {result}")
else:
    print("Item -1 not found")


result = binary_search(my_list, 9)
if result is not None:
    print(f"Index of item 9 is {result}")
else:
    print("Item not found")
