
print("Введіть текст. Для завершення напишіть STOP:")

lines = []

while True:
    line = input()
    if line == "STOP":
        break
    lines.append(line)

text = " ".join(lines)

words = text.lower().split()
counts = {}

for word in words:
    word = word.strip(".,!?;:")
    if word:
        counts[word] = counts.get(word, 0) + 1

print("\nЧастота слів за алфавітом:")
for word in sorted(counts):
    print(word, "-", counts[word])

print("\nЧастота слів за спаданням:")
for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
    print(word, "-", count)

frequent_words = {word: count for word, count in counts.items() if count >= 2}

print("\nСлова, які зустрічаються не менше двох разів:")
for word in sorted(frequent_words):
    print(word, "-", frequent_words[word])

print("\nЧастота відсутнього слова:", counts.get("відсутнє", 0))
