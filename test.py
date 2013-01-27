#!/usr/bin/python3
import sys

def sumpair(c, nums):
    """
    Accepts an integer c representing the sum value, and a list nums of
    integers which may be paired to sum to c

    Returns a set of tuples representing pairs which sum to c

    Runs in O(N) time.
    """
    cache = set()
    solutions = set()
    for num in nums:
        # Already found the other number to the pair, it's a solution!
        if (c - num) in cache:
            solutions.add((num, c - num))
        # Bookmark it in case I find (c - num) later
        else:
            cache.add(num)

    return solutions

# User input stuff
try:
    n = int(input())
    nums = []
    numlist = input().split(" ")
    for i in range(n):
        nums.append(int(numlist[i]))
    c = int(input())
except ValueError:
    print("Input must be an integer!")
    sys.exit(0)

pairs = sumpair(c, nums)
# Print results
for pair in pairs:
    print("{}, {}".format(pair[0], pair[1]))