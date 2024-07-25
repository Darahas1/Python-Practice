'''
Program to find the target element in a list using Binary Search!
Also find the first and last position of the element if it exists more than once.
'''

#binary search function
def binary_search(low, high, condi):
    while low <= high:
        mid = (low + high)//2
        result = condi(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        else:
            low = mid + 1
    return -1

#function to find the first position of the target element
def first_pos(nums, tar):
    def condi(mid):
        if nums[mid] == tar:
            if mid > 0 and nums[mid-1] == tar:
                return 'left'
            return 'found'
        elif nums[mid] < tar:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condi)

#function to find the last position of the target element
def last_pos(nums, tar):
    def condi(mid):
        if nums[mid] == tar:
            if mid < len(nums)-1 and nums[mid+1] == tar:
                return 'right'
            return 'found'
        elif nums[mid] < tar:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condi)

#main function to ease the handling of multiple functions for output. 
def main():
    nums = list(map(int,input('Enter the numbers into the list to check:').split()))
    tar = int(input('Enter the target number to find:'))
    gen_search = first_pos(nums, tar)
    f_p_search, l_p_search = first_pos(nums, tar), last_pos(nums, tar)
    print("General search:",gen_search) 
    print("First position of the element:", f_p_search)
    print("Last position of the element:", l_p_search)

#execute the main function directly
if __name__ == "__main__":
    main()
