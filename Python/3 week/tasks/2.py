'''
Вам нужно написать функцию lists_sum, которая принимает произвольное количество списков чисел, и 
возвращает сумму всех этих чисел. Предусмотрите дополнительный аргумент unique, который по умолчанию 
равен False, но если в функцию подается unique=True, то функция должна вернуть сумму всех уникальных чисел 
из всех списков. Если поданы только пустые списки или списки 
чисел вообще не поданы в функцию, то считать сумму чисел нулём.
'''
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
