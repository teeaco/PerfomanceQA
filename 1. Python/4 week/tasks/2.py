from collections import Counter
#Напишите функцию get_popular_name_from_file(filename), которая считывает файл, 
#в котором в каждой строке записаны имя и фамилия через пробел. filename - это имя файла, 
#в котором записаны эти имена. Вам нужно вернуть строку - самое популярное имя в файле. 
##Если таких имен несколько, они должны быть 
#перечислены через запятую внутри строки в алфавитном порядке.
def get_popular_name_from_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        names = [line.split()[0] for line in file if line.strip()]
    name_counts = Counter(names)
    max_count = max(name_counts.values())
    popular_names = sorted([name for name, count in name_counts.items() if count == max_count])
    return ', '.join(popular_names)
