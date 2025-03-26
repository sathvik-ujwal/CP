# to check if a number is power of 2

def pow2(num):
    return num > 0 and (num & (num -1)) == 0