arr = [1,5,3,2,0,8]

def BubbleSort(list):
    for j in range(0,len(list)-1):  # outter for loop will help iterate and push all the larger numbers to the right.
        for i in range(0, len(list)-1-j):   # each time i push the larger number to the end of the array, 
            if list[i] > list[i+1]:         # the array should stop iterating -1 from the right as well.
                list[i], list[i+1] = list[i+1], list[i]
    return list      
    

print(BubbleSort(arr))

