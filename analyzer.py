import re
text = open("input.txt", "r").read()

def most_common_words(arr):
    first = ""
    second = ""
    third = ""
    first_freq = 0
    second_freq = 0
    third_freq = 0

    dict = {}
    
    # create dict
    for i in range(len(arr)):
        if arr[i] not in dict.keys():
            dict.update({arr[i] : 1})
        else:
            dict.update({arr[i] : dict.get(arr[i]) + 1})
    
    # find top three most frequent words
    for key in dict.keys():
        freq = dict.get(key)
        if freq > first_freq:
            first = key
            first_freq = freq
        elif freq > second_freq:
            second = key
            second_freq = freq
        elif freq > third_freq:
            third = key
            third_freq = freq
    return [first, second, third, first_freq, second_freq, third_freq]

# characters
num_chars = len(text)

# characters no spaces
num_chars_no_spaces = len(text.replace(" ", ""))

# sentences
sentences = text.split(".")
while (sentences.count("")):
    sentences.remove("")
num_sentences = len(sentences)

# words
words = re.sub("[^a-zA-Z| ]", "", text).lower().split()
num_words = len(words)

# word frequency
freq_arr = most_common_words(words)


print("Number of Characters:", num_chars, 
      "\nNumber of Characters (No Spaces):", num_chars_no_spaces,
      "\nNumber of Words:", num_words,
      "\nNumber of Sentences:", num_sentences,
      "\nMost Frequent Words:\n1.", freq_arr[0], "(", freq_arr[3],"occurrences )\n2.",
      freq_arr[1], "(", freq_arr[4],"occurrences )\n3.",
      freq_arr[2], "(", freq_arr[5],"occurrences )\n",)


