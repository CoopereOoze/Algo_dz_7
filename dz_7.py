# В порядке убывания, если ra > rb, то выгоднее купить a раньше b
def fall(r):
    return [i for _, i in sorted(enumerate(r), key=lambda x: -x[1])]

r = [1, 3, 5]
print(fall(r))

"""**17(2)**"""

# В порядке возрастания, чем быстрее падает цена,
# тем раньше нужно продавать чтобы не потерять стоимость
def height(r):
    return [i for _, i in sorted(enumerate(r), key=lambda x: x[1])]

r = [1, 3, 5]
print(height(r))

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
