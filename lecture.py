# PART 1
import math
def is_palindrome(s):
    # Check if a string is a palindrome or not.
    # To make it simple, let's assume that an empty string is a palindrome.

    if len(s) <= 1:
        return True  # base case 1
    elif s[0] != s[-1]:
        return False  # base case 2
    else:
        # recursive case
        # -1 and then half it to get the index of the middle element in an odd one.
        # 101           len=3
        # 1001          len=4

        stack = []
        # Pushing phase
        for x in range(len(s) // 2):
            stack.append(s[x])
        for x in range(math.ceil(len(s) / 2), len(s)):
            if(stack[-1] == s[x]):
                stack.pop()

        return stack == []

# PART 2
def is_small(a):
    if a < 5:
        return True
    else:
        return False

def randomised_function():
    from random import randint
    a = randint(0, 10)

    if is_small(a):
        return 'software'
    else:
        return 'engineering'


# PART 3 (Advanced Topic)
def difficult_function(x, y):
    if complex_math(x, y) < 0.000001:
        return 'solved!'  ## TODO: How can we cover this line? In other words, how to find (x, y) that makes this line executed?
    else:
        return 'not yet'


def complex_math(x, y):
    import numpy as np
    a = 20
    b = 0.2
    c = 2 * np.pi
    t1 = -a * np.exp(-b * np.sqrt(0.5 * ((x-10) ** 2 + y ** 2)))
    t2 = -np.exp(0.5 * (np.cos(c * (x-10)) + np.cos(c * y)))
    return t1 + t2 + a + np.e

if __name__ == '__main__':
    print(difficult_function(10, 0))