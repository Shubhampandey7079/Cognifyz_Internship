def count_words(filename):
    word_count = {}

    with open(filename, "r") as file:
        text = file.read().lower()
        words = text.split()

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


result = count_words("D:\Cognifyz_Internship\Level2_Task5_FileManipulation\sample.txt")

print("Word Frequency:\n")

for word in sorted(result):
    print(word, ":", result[word])