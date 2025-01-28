def lists_sum(*args, unique=False):
    if not args:  
        return 0
    
    all_numbers = [num for lst in args for num in lst]
    
    if unique:
        all_numbers = set(all_numbers)
    
    return sum(all_numbers)

#print(lists_sum([1, 1], [1], [1, 2, 3]))  # 9
#print(lists_sum([1, 1, 1], [1, 1], unique=True))  # 1
#print(lists_sum([1, 1, 1], unique=False))  # 3
