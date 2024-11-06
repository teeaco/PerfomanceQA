input_string = input().lower()
words = [word.strip() for word in input_string.split(', ')]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:3]:
    print(f"{word}: {count}")
