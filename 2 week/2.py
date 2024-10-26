input_string = input().lower()
mass = [word.strip() for word in input_string.split(',')]
unique_words = set(mass)
unique_words = sorted(unique_words)
print(", ".join(unique_words))
