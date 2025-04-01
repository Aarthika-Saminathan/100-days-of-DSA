def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0  # If k <= 1, no valid subarray can exist with a product < k
    
    product = 1  # Product of elements in the current window
    left = 0  # Left pointer of the sliding window
    result = 0  # To store the number of valid subarrays
    
    # Iterate through the array with the right pointer
    for right in range(len(nums)):
        product *= nums[right]  # Expand the window by including nums[right]
        
        # Shrink the window from the left if the product >= k
        while product >= k and left <= right:
            product //= nums[left]
            left += 1
        
        # All subarrays ending at `right` and starting from any index from `left` to `right` are valid
        result += right - left + 1
    
    return result
