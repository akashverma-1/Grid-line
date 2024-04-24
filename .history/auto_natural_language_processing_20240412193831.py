import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.probability import FreqDist
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = "Natural language processing (NLP) is a subfield of linguistics, computer science, " \
       "and artificial intelligence concerned with the interactions between computers and human " \
       "natural languages, in particular how to program computers to process and analyze large " \
       "amounts of natural language data."

tokens = word_tokenize(text)
sentences = sent_tokenize(text)

stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)
filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words and word not in punctuation]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

freq_dist = FreqDist(filtered_tokens)

print("Original Text:", text)
print("\nTokenized Words:", tokens)
print("\nSentences:", sentences)
print("\nFiltered Tokens:", filtered_tokens)
print("\nStemmed Tokens:", stemmed_tokens)
print("\nLemmatized Tokens:", lemmatized_tokens)
print("\nMost Common Words:", freq_dist.most_common(5))
