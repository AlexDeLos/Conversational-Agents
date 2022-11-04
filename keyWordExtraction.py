import nltk


def get_key_concepts(string: str):
    tokens = nltk.word_tokenize(string)
    tagged = nltk.pos_tag(tokens)
    result =[]
    for tag in tagged:
        if tag[1] == 'NN' or tag[1] == 'VBZ' or tag[1] == 'NNP' or tag[1]=='VBD' or tag[1] == 'VBP' or tag[1] == 'VB':
            result.append(tag)
    lst2 = [res[0] for res in result]
    return lst2
