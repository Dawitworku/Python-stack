# Insertion Sort
# Objectives:
# Execute insertion sort
# Build an algorithm for insertion sort. Basically, this sort works by starting at index 1, shifting that value to the left until it is sorted relative to all values to the left, and then moving on to the next index position and performing the same shifts until the end of the list is reached.

my_arr = [9,3,78,12,76,0,-2]

for idx in range(1, len(my_arr)): 
    temp = my_arr[idx] 
    prev_idx = idx-1
    while prev_idx >= 0 and temp < my_arr[prev_idx]: 
        my_arr[prev_idx + 1] = my_arr[prev_idx] 
        prev_idx -= 1
    my_arr[prev_idx + 1] = temp 

print(my_arr)

