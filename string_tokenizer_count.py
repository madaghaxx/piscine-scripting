import string
# There is a similar one in rust pool and it was better written using rust
# This is the regexsless version because regex in python is default and boring
def tokenizer_counter(text):
    translator = str.maketrans('', '', string.punctuation)
    clean = text.translate(translator).lower()
    
    words = clean.split()
    
    map = {}
    for word in words:
        if word in map:
            map[word] += 1
        else:
            map[word] = 1
    
    return dict(sorted(map.items()))