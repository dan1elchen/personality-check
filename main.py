import nltk
import numpy as np


sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

print(tokens)
print(tagged[0:6])
