#С клавиатуры вводится строка, содержащая произвольное количество слов через запятую и пробел. 
#Слова могут повторяться. Нужно вывести 
#на экран все слова в алфавитном порядке по одному разу, также через пробел и запятую.
input_string = input().lower()
mass = [word.strip() for word in input_string.split(',')]
unique_words = set(mass)
unique_words = sorted(unique_words)
print(", ".join(unique_words))
