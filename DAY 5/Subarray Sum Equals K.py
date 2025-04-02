def subarraySum(nums, k):
    prefix_sum_count = {0: 1}  # To handle cases where prefixSum itself is k
    prefixSum = 0
    count = 0

    for num in nums:
        prefixSum += num  # Update running sum

        # Check if (prefixSum - k) exists in map
        if prefixSum - k in prefix_sum_count:
            count += prefix_sum_count[prefixSum - k]

        # Store prefixSum in the HashMap
        prefix_sum_count[prefixSum] = prefix_sum_count.get(prefixSum, 0) + 1

    return count
