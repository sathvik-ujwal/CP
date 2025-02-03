# MEX Is the smallest whole number not present in the array
import time
def mex(arr):
    arr.sort()
    arr = set(arr)
    for i, num in enumerate(arr):
        if num != i:
            return i
        
    return len(arr)

def mexn(arr):
    seen = set(arr)
    for i in range(len(seen)+1):
        if i not in seen:
            return i
    
if __name__ == "__main__":
    print("Enter input array")
    input_array = list(map(int, input().split()))
    start = time.time()
    res = mex(input_array)
    end = time.time()
    print(f"Time for sorting method : {end - start}")
    start = time.time()
    res = mexn(input_array)
    end = time.time()
    print(f"Time for set set searching: {end - start}")
    print(res)