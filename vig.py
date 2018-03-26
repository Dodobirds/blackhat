import sys
import english

file_name = './Emails/email2'
with open(file_name, 'r') as f:
    cy = f.readline()

NORMAL_FREQ = english.normal_freqs
FREQ_SQR = 0
for n in NORMAL_FREQ:
    FREQ_SQR += NORMAL_FREQ[n] ** 2

def shiftBy(a, n):
    return chr(((ord(a) - ord('a') + n) % 26) + ord('a'))

def findFreq(text):
    freq = {}
    freq_sum = 0
    for letter in NORMAL_FREQ:
        freq[letter]= float(text.count(letter)) / len(text)
        freq_sum += freq[letter] ** 2
    return freq, freq_sum

def findKeyLength(text):
    big = 0
    lenght = 0
    for n in range(10,21):
        prev = {}
        total = 0
        for a in range(n, len(text), n):
            seg = text[a-2:a+1]
            if seg in prev:
                prev[seg] += 1
            else:
                prev[seg] = 0
        for key in prev:
            total += prev[key]
        #print(total)
        if total > big:
            big = total
            length = n
    return length

key_length = findKeyLength(cy)

freq = findFreq(cy[::key_length])[0]
big = 0
save = 0

#print(cy.upper())

def findShift( freq):
    s = 0
    big = 1
    val = 0
    for key in range(26):
        temp = 0
        for letter in NORMAL_FREQ:
            guess = shiftBy(letter, key)
            temp += NORMAL_FREQ[letter] * freq[guess]
        if abs(temp - .065) < big:
            big = abs(temp - .065)
            val = key
    return val
#print(findShift(freq))
k = ''
for n in range(key_length):
    k += chr(ord('a') +findShift(findFreq(cy[n::key_length])[0]))


def decodeVigenere(key, code):
    message = ''
    for n in range(len(code)):
        m = n % len(key)
        message = message + shiftBy(code[n], 26 - (ord(key[m]) - ord('a')))
    return message

#print(decodeVigenere(k,cy))

#i just manually fixed the 2nd index
k = k[:1] + 'u' + k[2:]
print(k)
print(decodeVigenere(k, cy))
