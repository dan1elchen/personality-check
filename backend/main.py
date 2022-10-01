import numpy as np
import nltk
import csv
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def read_csv(csv_file_path):
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            tokens = nltk.word_tokenize(row)
            tagged = nltk.pos_tag(tokens)
            print(tagged)


def main():
    read_csv("mbti_1.csv")


if __name__ == "__main_":
    main()

# sentence = """At eight o'clock on Thursday morning
# ... Arthur didn't feel very good."""
# tokens = nltk.word_tokenize(sentence)
# tagged = nltk.pos_tag(tokens)

# print(tokens)
# print(tagged[0:6])
