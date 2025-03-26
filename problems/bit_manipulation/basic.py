'''
https://leetcode.com/discuss/post/6543135/all-about-bit-manipulation-by-leadingthe-qkqn/
'''
# converting number to binary

def decimal_to_binary(n):
    return bin(n)[2:]

# manual converstion

def to_binary(n):
    binary = ''
    while n > 0:
        binary += str(n % 2)
        n /= 2
    return binary[::-1]

def binary_to_decimal(binary):
    return int(binary, 2)

# manual conversion

def binary_to_decimal(binary):
    decimal = 0
    power = 1
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '1':
            decimal += power
        power += 2
    return decimal

def odd_check(num):
    if (num & 1):
        print("odd")
    else:
        print("even")
        
# swaping two numbers without extra variable
def swap(a, b):
    a = a^b
    b = a^b
    a = a^b
    
# check if a number if power of 2
def check_power(num):
    return num > 0 and (num & (num - 1)) == 0

# function to find the minimum number of bitflips to convert one number to another

def bitflip(start, goal):
    res = start ^ goal
    return bin(res).count('1')

# prime factors

def prime_factors(num):
    primes = []
    
    if num & 1 == 0:
        primes.append(num)
        while num & 1 == 0:
            num >>= 1
            
    i = 3
    while i * i <= num:
        if num % i == 0:
            primes.append(num)
        while num % i == 0:
            num //= i
        i += 2
        
    if num > 1:
        primes.append(num)
    return primes

# finding the number that appears once

def once(nums):
    res = 0
    for num in nums:
        res ^= num
    return res