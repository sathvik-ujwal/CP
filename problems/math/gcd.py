import time
import math

# Euclidean algo

def EGCD(a,b):
    if a == 0:
        return b
    if b== 0:
        return a
    if a ==b:
        return a
    if (a >b):
        return EGCD(a-b,b)
    return EGCD(a, b-a)

# Recursion
def RGCD(a, b):
    if (b == 0):
        return a 
    else:
        return RGCD(b, a % b)
    

if __name__ == "__main__":
    a, b = 8728, 3380
    curr = time.time()
    Egcd = EGCD(a,b)
    print(time.time() - curr)
    cur = time.time()
    Rgcd = RGCD(a,b)
    print(time.time() - cur)
    cu = time.time()
    Mgcd = math.gcd(a,b)
    print(time.time() - cu)
    print(Rgcd)
    print(Egcd)