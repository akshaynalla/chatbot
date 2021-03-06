import nltk
#nltk.download("punkt")
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
import numpy as np

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return  stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    tokenized_sentence = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag

"""sentence = ["hello", "how", "are", "you"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
bag = bag_of_words(sentence, words)
print(bag)

a = "How long does shipping take?"
print(a)
a_token= tokenize(a)
print(a_token)
words = ["Organize", "Organizes", "Organizer"]
stemmed_words = [stem(w) for w in words]
print(stemmed_words)"""