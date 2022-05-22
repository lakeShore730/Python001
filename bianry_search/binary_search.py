import random
import time

def naive_serrch(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    # print(f"Low value : {low}")
    # print(f"High value: {high}")
    
    if high < low:
        return -1    
    
    mid_point = (low + high) // 2
    # print(l[mid_point: high])
    
    
    if l[mid_point] == target:
        return mid_point

    elif target < l[mid_point]:
        return binary_search(l, target, low, mid_point-1)
    
    else:
        return binary_search(l, target, mid_point + 1, high)


if __name__ == "__main__":
    # num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # target = 7
    # print(binary_search(num_list, target))
    
    list_length = 30000
    sorted_list = set()
    
    while len(sorted_list) < list_length:
        sorted_list.add(random.randint(-3*list_length, 3*list_length))

    # print(sorted_list)
    # print(f"min value : {min(sorted_list)}")
    # print(f"max value : {max(sorted_list)}")
    
    # let' s sort the list 
    sorted_list = sorted(list(sorted_list))
    
    # Now, let's search all number in list 

    start_time = time.time()
    
    for target in sorted_list:
        naive_serrch(sorted_list, target)
    
    end_time = time.time()
    
    print(f"Naive search  time : {end_time - start_time}")    
     

    # time calculation for the binary search
    start_time = time.time()
    
    for target in sorted_list:
        binary_search(sorted_list, target)
        
    end_time = time.time()
    
    print(f"Binary search time : {end_time - start_time}")
        
    
    
    
