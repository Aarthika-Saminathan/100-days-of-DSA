def maxSubArrayLen(nums, k):
    prefix_sum_index = {}  # Stores prefix sum and its first occurrence index
    prefixSum = 0
    max_length = 0

    for i, num in enumerate(nums):
        prefixSum += num  # Update prefix sum

        # If prefixSum itself is k, update max_length
        if prefixSum == k:
            max_length = i + 1

        # If (prefixSum - k) exists in map, update max_length
        if (prefixSum - k) in prefix_sum_index:
            max_length = max(max_length, i - prefix_sum_index[prefixSum - k])

        # Store the first occurrence of prefixSum
        if prefixSum not in prefix_sum_index:
            prefix_sum_index[prefixSum] = i

    return max_length

# Example test cases
nums1 = [1, -1, 5, -2, 3]
k1 = 3
print(maxSubArrayLen(nums1, k1))  # Output: 4

nums2 = [-2, -1, 2, 1]
k2 = 1
print(maxSubArrayLen(nums2, k2))  # Output: 2
