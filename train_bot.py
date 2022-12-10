#Text Data Preprocessing Lib

import nltk 
from nltk.stem import PorterStemmer
Stemmer = PorterStemmer()

import json 
import pickle
import numpy as np

words = []
classes = []
word_tags_list = []
ignore_words = ['?','!',',','.','s','m']
train_data_file = open ('intents.json').read()
intents = json.loads(train_data_file)

#Function for appending stem words

def get_stem_words(words, ignore_words):
        stem_words = []
        for word in words:
                if word not in ignore_words:
                        w = Stemmer.stem(word.lower())
                        stem_words_append(w) 


        return stem_words

for intent in intents['intents']:

#Add all words of patterns to list
                for pattern in intent['pattern']:
                        pattern_word = nltk.word_tokeniser(pattern)
                        words.extend(pattern_word)
                        word_tags_list.append((pattern_word, intent['pattern']))
        
#Add all tags to the classes list
                if intent['tag'] not in classes:
                        classes.append(intent['tag'])
                        stem_words = get_stem_words(words,ignore_words)

print(stem_words)
print(word_tags_list[0])
print(classes)
