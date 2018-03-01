import sys
import english

file = 'email3'
if len(sys.argv) > 1:
    file = sys.argv[1]


def adjugate(matrix):
    return [[matrix[1][1],(-1 * matrix[0][1]) % 26], [(-1 * matrix[1][0]) % 26,matrix[0][0]]]

def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def egcd(a,b):
    s, t, r = 0, 1, b
    o_s, o_t, o_r = 1, 0, a
    while o_r != 0:
        q = r // o_r
        r, o_r = o_r, r % o_r
        s, o_s = o_s - q * s, s
        t, o_t = o_t - q * t, t
    return r,o_t,o_s

def invertDeterminant(n, mod=26):
    gcd = egcd(n,mod)
    if gcd[0] == 1:
        return gcd[1] % mod
    else:
        return False

def inverse(matrix):
    invert_D = invertDeterminant(determinant(matrix) % 26)
    if invert_D == False:
        return invert_D

    adj = adjugate(matrix)
    for n in range(len(adj)):
        for m in range(len(adj)):
            adj[n][m] *= invert_D
            adj[n][m] %= 26
    return adj

def hillDecrypt(text, key):
    plain = ''
    for n in range(0,len(text), 2):
        first = ord(text[n]) - ord('a')
        second = ord(text[n+1]) - ord('a')
        plain += chr(((first * key[0][0] + second * key[0][1]) % 26) + ord('a'))
        plain += chr(((first * key[1][0] + second * key[1][1]) % 26) + ord('a'))
    return plain

#print(hillDecrypt('apadjtftwlfj', [[25,22],[1,23]])) #shortexample
#print(inverse([[7,8],[11,11]])) # [[25, 22], [1, 23]]
