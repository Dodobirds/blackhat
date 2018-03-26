import english
import operator

NORMAL_FREQ = english.normal_freqs
email = "Emails/email5"
with open(email, 'r') as f:
    cy = f.readline()

freq_order = 'zjqxkvbpgwyfmculdhrsnioate'
key = {}

def dictPrint(dic):
    for n in dic:
        print(str(n) + ' : ' + str(dic[n]))

def findFreq(text):
    freq = {}
    for l in NORMAL_FREQ:
        freq[l] = text.count(l) /len(text)
    return freq
freq = findFreq(cy)

def removeDupe(key):
    for a in key:
        if len(key[a]) == 1:
            for b in key:
                if len(key[b]) > 1:
                    if key[a][0] in key[b]:
                        key[b].remove(key[a][0])
    return key

def possibleKey(obs, exp):
    poss = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for a in alpha:
        for b in alpha:
            temp = abs(obs[a] - exp[b])
            if temp < .018:
                if a in poss:
                    poss[a].append(b)
                else:
                    poss[a] = [b]
    return poss

dictPrint(possibleKey(freq, NORMAL_FREQ))

def findBiGrams(text):
    bigram = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for a in alpha:
        for b in alpha:
            temp = text.count(a+b)
            if temp > 5:
                bigram[a+b] = temp
    return bigram

def findTriGrams(text):
    trigram = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for a in alpha:
        for b in alpha:
            for c in alpha:
                temp = text.count(a+b+c)
                if temp > 5:
                    trigram[a+b+c] = temp
    return trigram

def fillPrint(text, key):
    for c in text:
        if len(key[c]) == 1:
            print(key[c][0], end='')
        else:
            print("-", end='')
def reverseFillPrint(text,key):
    for c in text:
        if len(key[c]) == 1:
            print('*', end='')
        else:
            print(c, end='')
#i should have made some kind
key = removeDupe(possibleKey(freq, NORMAL_FREQ))
dictPrint(findBiGrams(cy))
dictPrint(findTriGrams(cy))

while(True):
    print()
    fillPrint(cy, key)
    print('\n')
    reverseFillPrint(cy, key)
    print()

    choice = input()
    key[choice[0]] = [choice[2]]
    key = removeDupe(key)
    dictPrint(key)
