import re
# First time regexing in python HHHHHH
def tokenize(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-z0-9\s]', ' ', sentence)
    tokens = []
    for word in sentence.split():
        if word:
            tokens.append(word)
    return tokens
# I think all the regexes are the same except the bash (grep)