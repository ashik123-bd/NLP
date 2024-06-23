import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

example = "Hello Mr. Smith , how are doing today? The weather is great, and Python is awesome.The sky is pinkish-blue.You don't eat cardboard "

print(sent_tokenize(example))
print("\n")
print(word_tokenize(example))