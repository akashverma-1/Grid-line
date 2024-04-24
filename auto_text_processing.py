def tokenize_text(text):
    words = text.split()
    return words

def remove_stopwords(words):
    stopwords = set(['the', 'a', 'an', 'and', 'or', 'but', 'if', 'then', 'is', 'are', 'be', 'were'])
    filtered_words = [word for word in words if word.lower() not in stopwords]
    return filtered_words

def calculate_word_frequency(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

text = "This is a sample text for text processing. Text processing involves analyzing and manipulating textual data."

words = tokenize_text(text)

filtered_words = remove_stopwords(words)

word_freq = calculate_word_frequency(filtered_words)

# Display the results
print("Original Text:", text)
print("\nTokenized Words:", words)
print("\nFiltered Words (without stopwords):", filtered_words)
print("\nWord Frequency:", word_freq)
