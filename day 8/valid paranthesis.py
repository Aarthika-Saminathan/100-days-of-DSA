def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False  # Invalid character

    return not stack  # If stack is empty, it's valid

# Example usage:
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))      # Output: False
