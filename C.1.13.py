def reverse_list_of_integers(list):
    reversed_array=[]
    for i in range(0, len(list)):
        reversed_array.prepend(list[len(list)-i-1])
    return reversed_array


