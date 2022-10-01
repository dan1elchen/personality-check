import numpy as np
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

print(tokens)
print(tagged[0:6])
