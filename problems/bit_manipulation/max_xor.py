# find the maximum xor of an subsequence of an array

def max_subset_xor(arr):
    n = len(arr)
    index = 0
    MAX_BITS = max(arr).bit_length()  # highest bit needed

    # Step 1: Build the basis
    for bit in range(MAX_BITS - 1, -1, -1):  # from MSB to LSB
        # Find a number with current bit set
        max_idx = index
        for i in range(index, n):
            if arr[i] & (1 << bit):
                max_idx = i
                break

        # If no number has this bit, continue
        if not (arr[max_idx] & (1 << bit)):
            continue

        # Swap to current index
        arr[index], arr[max_idx] = arr[max_idx], arr[index]

        # Eliminate this bit from all others
        for i in range(n):
            if i != index and (arr[i] & (1 << bit)):
                arr[i] ^= arr[index]

        index += 1

    # Step 2: Find max XOR
    max_xor = 0
    for i in range(index):
        max_xor = max(max_xor, max_xor ^ arr[i])

    return max_xor


# Example
arr = [1, 2, 3, 4]
print(max_subset_xor(arr))  # Output: 7
