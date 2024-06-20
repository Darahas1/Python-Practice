# Write a Python program that takes a list of integers as input and returns the maximum number in the list. The program should handle both positive and negative integers.

nums = list(map(int,input().split()))
print("The Maximum number in the list is:",max(nums))