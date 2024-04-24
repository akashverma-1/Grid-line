import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter

class NLPProcessor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
        self.ps = PorterStemmer()

    def _tokenize(self, text):
        return word_tokenize(text)

    def _remove_stopwords(self, tokens):
        return [word for word in tokens if word.lower() not in self.stop_words]

    def _stemming(self, tokens):
        return [self.ps.stem(word) for word in tokens]

    def _count_words(self, tokens):
        return Counter(tokens)

    def process_files(self, folder_path):
        results = {}
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r') as file:
                    text = file.read()
                tokens = self._tokenize(text)
                tokens_without_stopwords = self._remove_stopwords(tokens)
                stemmed_tokens = self._stemming(tokens_without_stopwords)
                word_counts = self._count_words(stemmed_tokens)
                results[filename] = word_counts.most_common(5)  # Take the top 5 most common words
        return results

# Example usage:
nlp_processor = NLPProcessor()
folder_path = "/path/to/text/files"
processed_data = nlp_processor.process_files(folder_path)
print(processed_data)
