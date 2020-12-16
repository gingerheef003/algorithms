from math import ceil

def prime(n):
    for i in [2] + list(range(3, ceil(n**0.5), 2)):
        if n%i == 0:
            return False
    return True