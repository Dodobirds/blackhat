import re, sys

if len(sys.argv) > 1:
    file = sys.argv[1]

normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

with open('./English Score/20kWords','r') as f: #first20hours/google-10000-english
    common_words = [word.strip() for word in f]

with open('./English Score/digrams','r') as f:
    common_digrams = [re.sub(r'[^a-zA-Z]','', word).lower() for word in f]

with open ('./English Score/trigrams','r') as f:
    common_trigrams = [re.sub(r'[a-zA-Z]','', word).lower() for word in f]

def dictCheck(text):
    total = 0
    for w in common_words:
        total += text.count(w) * len(w)
    return total / len(text)

def diGram(text):
    total = 0
    for w in common_digrams:
        total += text.count(w)
    return total / len(text)

def triGram(text):
    total = 0
    for w in common_trigrams:
        total += text.count(w)
    return total / len(text)

def freqCalc(text): #closest to .065
    freq_sum = 0
    freq = {}
    for letter in normal_freqs:
        freq[letter] = float(text.count(letter)) / len(text)
        freq_sum += freq[letter] * freq[letter]
    print(freq)
    return  freq_sum

def chiSqr(text): #smaller chiSqr is closest to english text
    total = 0
    for letter in normal_freqs:
        exp = normal_freqs[letter] * len(text)
        chi = text.count(letter) - exp
        total += (chi * chi) / exp
    return total

def calcScore(text):
    text = text.lower()
    a = dictCheck(text)
    b = diGram(text)
    c = triGram(text)
    #d = chiSqr(text) / 25
    return (a + b + c)

if len(sys.argv) > 1:
    print(calcScore(file))
