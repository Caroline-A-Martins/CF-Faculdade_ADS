def sort(array):
    for index in range(0, len(array)):
        
        min_index = index  
       
        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]: 
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]

array1 = [40,16,8,4,12]
array2 = [20, 50, 5, 4,2,90]
array3 = [21,10,11,5,30,50,54]
sort(array1)
print(array1)

sort(array2)
print(array2)

sort(array3)
print(array3)