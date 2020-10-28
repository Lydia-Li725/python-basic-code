def insertion_sort(array):
    for index in range(1,len(array)):
        position = index
        temp_value = array[index]
        while position > 0 and array[position - 1] > temp_value:
            array[position] = array[position-1]
            position -= 1
        array[position] = temp_value
    return array
a = [1,7,6,3,2,4]
print(insertion_sort(a))