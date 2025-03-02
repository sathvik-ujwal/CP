'''
given 3 binary strings s1, s2, s3 make of size n. make then contain either all 0s or 1s.
By swapping with other string. return the minimum number of swaps. if not possible return -1
sample input:
   100
   000
   011
output:
   1
   
explanation: swap char 0 of 1 and char 0 if s3
'''

def solve():
    n = int(input())
    s1 = input()
    s2 = input()
    s3 = input()
    s1c = s1.count('1')
    s2c = s2.count('1')
    s3c = s3.count('1')
    
    su = s1c + s2c + s3c
    if su % n != 0:
        print(-1)
    elif su == n:
        print(n - max(s1c, s2c, s3c))
    elif su == 2*n:
        print(min(s1c, s2c, s3c))
    else:
        print(0)
    return
        
    
    
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
