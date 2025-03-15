from collections import Counter
def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    cnt = Counter(a)
    k = len(cnt)
    for num in sorted(cnt.values()):
        if m < num:
            break
        m -= num
        k -=1
    print(max(1,k))
    return
        
    
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
    

    
    