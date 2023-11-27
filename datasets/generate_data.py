import json
import string
import random

def lowercase_true_uppercase_false(nsamples, is_example=False):
    # whenever the sentence contains only lower case classify as True
    # if contains any uppercase classify as False
    # the input space only contains letters with lower and uppercase
    res = []
    for _ in range(nsamples):
        size = random.randint(1, 5)
        label = random.choices([True, False], [0.5, 0.5])
        if label[0]:
            text = ''.join(random.choice(string.ascii_lowercase) for _ in range(size))
        else:
            is_contain_upper = False
            while not is_contain_upper:
                text = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(size))
                is_contain_upper = any(ele.isupper() for ele in text)
            assert is_contain_upper == True
        res.append({'text': text, 'label': label[0]})
    if is_example:
        with open("lowercase_true_uppercase_false_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("lowercase_true_uppercase_false.json", "w") as final:
            json.dump(res, final, indent=2)

def odd_even(nsamples, is_example=False):
    s  = [random.randint(0,100) for _ in range(nsamples) ]
    l = [str( (v/2)==int(v/2) ) for v in s]
    res = []
    for text, label in zip(s, l):
        res.append({'text': text, 'label': label})
    if is_example:
        with open("odd_even_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("odd_even.json", "w") as final:
            json.dump(res, final, indent=2)


def algorithmicSentences1():
    t = ['I', 'You', 'We', 'They']
    w0 = ['love', 'don’t care about', 'see', 'want to see']
    w1 = ['the', 'our', 'their', 'your']
    w2 = ['apple', 'orange', 'fig', 'peach', 'mango', 'walnut']
    w3 = ['tree', 'desert', 'slices']
    w4 = ['today', 'yesterday', 'tomorrow']
    t__ = random.choice(t)
    t0 = random.choice(w0)
    t1 = random.choice(w1)
    t2 = random.choice(w2)
    t3 = random.choice(w3)
    t4 = random.choice(w4)
    t = ' '.join([t__,t0, t1, t2, t3, t4])
    return t


def Apple(nsamples, is_example=False):
    s = [algorithmicSentences1() for k in range(nsamples)]
    l = [('apple' in j) for j in s]
    res = []
    for text, label in zip(s, l):
        res.append({'text': text, 'label': label})
    if is_example:
        with open("Apple_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("Apple.json", "w") as final:
            json.dump(res, final, indent=2)

def Walnut(nsamples, is_example=False):
    s = [algorithmicSentences1() for k in range(nsamples)]
    l = [('walnut' in j) for j in s]
    res = []
    for text, label in zip(s, l):
        res.append({'text': text, 'label': label})
    if is_example:
        with open("Walnut_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("Walnut.json", "w") as final:
            json.dump(res, final, indent=2)


def Love(nsamples, is_example=False):
    s = [algorithmicSentences1() for k in range(nsamples)]
    l = [('love' in j) for j in s]
    res = []
    for text, label in zip(s, l):
        res.append({'text': text, 'label': label})
    if is_example:
        with open("Love_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("Love.json", "w") as final:
            json.dump(res, final, indent=2)


def Sums(nsamples, is_example=False):
    i1 = [random.randint(0, 10) for j in range(nsamples)]
    i2 = [random.randint(0, 10) for j in range(nsamples)]
    r = [random.randint(0, 20) for j in range(nsamples)]
    a__ = [(str(i1[j] + i2[j]) if random.choice([True, False]) else str(r[j])) for j in range(nsamples)]
    s = [str(i1[j]) + ' ' + str(i2[j]) + ' ... ' + a__[j] for j in range(nsamples)]
    l = [a__[j] == str(i1[j] + i2[j]) for j in range(nsamples)]
    res = []
    for text, label in zip(s, l):
        res.append({'text': text, 'label': label})
    if is_example:
        with open("Sums_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("Sums.json", "w") as final:
            json.dump(res, final, indent=2)
def GetCommonWords():
    lines = open('../CommonWords.txt').read().splitlines()
    return lines

def Longer(nsamples, is_example=False):
    words = GetCommonWords()
    s_1 = [random.choice(words) for j in range(nsamples)]
    s_2 = [random.choice(words) for j in range(nsamples)]
    s = ['Word 1: ' + s_1[j] + ' | Word 2:' + s_2[j]  for j in range(nsamples)]
    l = [len(s_1[j])>len(s_2[j]) for j in range(nsamples)]
    res = []
    for text, label in zip(s, l):
        res.append({'text': text, 'label': label})
    if is_example:
        with open("Longer_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("Longer.json", "w") as final:
            json.dump(res, final, indent=2)




def Noun(nsamples, is_example=False):
    from nltk import pos_tag
    words = GetCommonWords()
    s_1 = [random.choice(words) for j in range(nsamples)]
    s = [pos_tag([s_1[j]], tagset='universal')[0][0] for j in range(nsamples)]
    l = [pos_tag([s_1[j]], tagset='universal')[0][1]=='NOUN' for j in range(nsamples)]
    res = []
    for text, label in zip(s, l):
        res.append({'text': text, 'label': label})
    if is_example:
        with open("Noun_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("Noun.json", "w") as final:
            json.dump(res, final, indent=2)



def Verb(nsamples, is_example=False):
    from nltk import pos_tag
    words = GetCommonWords()
    s_1 = [random.choice(words) for j in range(nsamples)]
    s = [pos_tag([s_1[j]], tagset='universal')[0][0] for j in range(nsamples)]
    l = [pos_tag([s_1[j]], tagset='universal')[0][1]=='VERB' for j in range(nsamples)]
    res = []
    for text, label in zip(s, l):
        res.append({'text': text, 'label': label})
    if is_example:
        with open("Verb_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("Verb.json", "w") as final:
            json.dump(res, final, indent=2)



def endsWithExclamation(samples, is_example=False):
    from english_words import get_english_words_set
    web2lowerset = get_english_words_set(['web2'], lower=True)
    res = []
    for _ in range(samples):
        word = random.choice(list(web2lowerset))
        if random.choice([True, False]):
            text = word
            label = 'True'
        else:
            text = word + '!'
            label = 'False'
        res.append({'text': text, 'label': label})

    if is_example:
        with open("endsWithExclamation_example.json.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("endsWithExclamation.json.json", "w") as final:
            json.dump(res, final, indent=2)


def LoadSentences():
    from urllib import request
    url = "http://www.gutenberg.org/files/2554/2554-0.txt"
    response = request.urlopen(url)
    raw = response.read().decode('utf8')

    from nltk import sent_tokenize
    sentences = sent_tokenize(raw)
    return sentences

def SentenceLength(nsamples, is_example=False):
    snt = LoadSentences()
    s = [random.choice(snt) for i in range(nsamples)]
    l   = [len(q.split(' ')) >=8 for q in s]
    res = []
    for text, label in zip(s, l):
        res.append({'text': text, 'label': label})
    if is_example:
        with open("SentenceLength_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("SentenceLength.json", "w") as final:
            json.dump(res, final, indent=2)


def Questions(nsamples, is_example=False):
    from nltk import sent_tokenize, word_tokenize
    snt = LoadSentences()
    s = [random.choice(snt) for i in range(nsamples)]
    l   = ['?' in q for q in s]
    res = []
    for text, label in zip(s, l):
        res.append({'text': text, 'label': label})
    if is_example:
        with open("Question_example.json", "w") as final:
            json.dump(res, final, indent=2)
    else:
        with open("Question.json", "w") as final:
            json.dump(res, final, indent=2)

# lowercase_true_uppercase_false(50)
# lowercase_true_uppercase_false(20, is_example=True)
# odd_even(50)
# odd_even(20, is_example=True)
#endsWithExclamation(50)
#endsWithExclamation(20, is_example=True)
# res = odd_even(100)
# print(res)
Sums(50)
Sums(50, is_example=True)
#Longer(50)
#Longer(50, is_example=True)
#Note: 20 in-context examples are not enough for Noun and Verb, it needs 50.
# Noun(50)
# Noun(50, is_example=True)
# Verb(50)
# Verb(50, is_example=True)
# Love(50)
# Love(50, is_example=True)
# Apple(50)
# Apple(50, is_example=True)
# Walnut(50)
# Walnut(50, is_example=True)
#SentenceLength(50)
#SentenceLength(50, is_example=True)
# Questions(25)
# Questions(25,is_example=True)