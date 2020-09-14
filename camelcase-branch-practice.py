# This program uses the .title(), .split(), and .join() functions to convert a sentence into camel case.

def camelcase(sentence):
    cap_sentence = sentence.title()
    split_sentence = cap_sentence.split(" ")

    split_sentence[0] = split_sentence[0].lower()   # First word must be lowercase

    join_sentence = "".join(split_sentence)
    return join_sentence

def main():
    sentence = input("Enter a sentence: ")
    output = camelcase(sentence)
    print(output)
