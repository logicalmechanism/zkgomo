import hashlib

def get_word_list():
    words = []
    with open("dice.txt",'r') as file:
        for line in file:
            word= line.strip().split(' ')[1]
            words.append(word)
    return words
def base10(obj):
    """
    Converts some hash into base 10.
    """
    target = int(obj, 16)
    return target


def baseQ(n, b):
    """
    Convert base 10 into base b.
    """
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def getHash(ctr):
    """
    Stringify ctr, hash it, then hexdigest.
    """
    m = hashlib.sha3_256()
    string = str(ctr).encode('utf-8')
    m.update(bytes(string))
    ctr_hash = m.hexdigest()
    return ctr_hash

def hash_to_list(data, N):
    return baseQ(base10(getHash(data)), N)

def string_to_int(string):
    return base10(getHash(string))