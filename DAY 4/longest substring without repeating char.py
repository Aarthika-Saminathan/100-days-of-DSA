def length_of_longest_substring_brute(s):
    max_length = 0

    for i in range(len(s)):
        seen = set()  # To store unique characters
        for j in range(i, len(s)):
            if s[j] in seen:  # If character repeats, break
                break
            seen.add(s[j])
            max_length = max(max_length, j - i + 1)

    return max_length

# Test
print(length_of_longest_substring_brute("abcabcbb"))  # Output: 3
print(length_of_longest_substring_brute("bbbbb"))     # Output: 1
print(length_of_longest_substring_brute("pwwkew"))    # Output: 3
