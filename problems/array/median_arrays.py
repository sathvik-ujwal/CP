# median of 2 sorted arrays 
# time complexity should be at worst O(log(m+n))

from typing import List
def medianOfSortedArrays(nums1: List[int] , nums2: List[int]) -> float:
    n = len(nums1)
    m = len(nums2)
    
    if n > m:
        medianOfSortedArrays(nums2, nums1)
        
    l, r= 0, n
    while l <= r:
        mid1 = (l+r)//2
        mid2 = (m+n+1)//2 -mid1
        
        l1 = (mid1 == 0) and float('inf') or nums1[mid1-1]
        r1 = (mid1 == n) and float('-inf') or nums1[mid1]
        l2 = (mid2 == 0) and float('inf') or nums2[mid2-1]
        r2 = (mid2 == m) and float('-inf') or nums2[mid2]
        
        if l1 > r2:
            r =mid1-1
        elif l2 > r1:
            l = mid1+1
        else:
            if (m+n) % 2 == 0:
                return (max(l1,l2)+ min(r1, r2)) / 2.0
            else:
                return max(l1, l2)
    return 0
        
        