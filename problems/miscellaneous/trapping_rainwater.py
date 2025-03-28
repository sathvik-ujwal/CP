# given an array of heights find the amount of water 
# that can be stored

def trapping_rainwater(array):
    l, r= 1, len(array)-2
    left_max, right_max = array[0], array[len(array)-1]
    water = 0
    
    while l <= r:
        if left_max <= right_max:
            left_max = max(left_max, array[l])
            water += left_max - array[l]
            l += 1
        else:
            right_max= max(right_max, array[r])
            water += right_max - array[r]
            r -= 1 
        print(water)
    return water

if __name__ == "__main__":
    array = [6, 2, 4, 8, 3, 8]
    res = trapping_rainwater(array)
    print(res)
            
            