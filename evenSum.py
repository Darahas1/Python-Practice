# Write a Python program that takes a list of integers as input and returns the sum of all the even numbers in the list. The program should handle both positive and negative integers and should return 0 if there are no even numbers in the list.

nums = list(map(int,input().split()))
sum = 0
for n in nums:
    if n%2==0:
        sum += n

print("The Sum of even numbers in the list is:",sum)