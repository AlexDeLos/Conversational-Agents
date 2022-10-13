import nltk


def get_key_concepts(string: str):
    tokens = nltk.word_tokenize(string)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
    for tag in tagged:
        if tag[1] == 'DT' or tag[1] == '.':
            tagged.remove(tag)

    print(tagged)

get_key_concepts("this is a test sentence. Eleni is a very sketchy girl")