arr = [50, 32, 2, 77, 25]
#      0   1   2   3   4
#      [2, 32,50,77,25]----1st iteration
def SelectionSort(list):


    for j in range(len(list)):
        min = list[j]
        min_idx = j             #<---Since we are swapping outside of the for loop, putting just list[i] will 
        for i in range(j,len(list)):    # not work. Thus, we need a variable to replace that i position as we 
            if list[i] < min:               #iterate through the array. list[min_index]
                min = list[i]#<----minimim value
                min_idx = i

        list[j], list[min_idx] = min, list[j]
            

    print(min)
    print(list)

SelectionSort(arr)


#list[0], list[i] = list[i], list[0]
