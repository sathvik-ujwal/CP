def toRoman(num):
    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    i = 12
    res = ""
    while num > 1:
        if num // nums[i] > 0:
            res += roman[i] * (num // nums[i])
            num = num % nums[i]
        i-=1
    return res

if __name__ == "__main__":
    num = 1012
    roman = toRoman(num)
    print(roman)
                