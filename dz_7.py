"""**18**"""

def is_subsequence(S, S_prime):
    i = 0
    for x in S:
        if i < len(S_prime) and x == S_prime[i]:
            i += 1
    return i == len(S_prime)

S = ["Amazon", "Yahoo", "eBay", "Yahoo", "Yahoo", "Oracle"]
S_prime = ["Yahoo", "eBay", "Yahoo", "Oracle"]

print(is_subsequence(S, S_prime))
