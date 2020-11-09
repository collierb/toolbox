# -*- coding: UTF-8 -*-

import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def clean_text(x):
    for punctuation in string.punctuation:
        x = x.replace(punctuation, '')
    x = x.lower()
    x = ''.join(word for word in x if not word.isdigit())
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(x)
    x = [w for w in word_tokens if not w in stop_words]
    lemmatizer = WordNetLemmatizer()
    x = [lemmatizer.lemmatize(word) for word in x]

    return x
