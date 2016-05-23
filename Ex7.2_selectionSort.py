'''
    selection sort
'''

def findMin(nums, start):
    if start == len(nums)-1:
        return start
    else:
        temp = findMin(nums, start+1)
        return start if nums[start] < nums[temp] else temp


def selectionSort(nums):
    for i in range(len(nums)):
        temp = findMin(nums, i)
        if temp != i:
            nums[temp], nums[i] = nums[i], nums[temp]

    return nums

print selectionSort([1,3,4,2,5,0,-123])