select = int(input())
lst = [int(x) for x in input().strip().split()]
def mean(lst):
    total = 0
    for n in lst:
        total += int(n)
    return total/len(lst)

def median(nums):
    nums.sort()
    length = len(nums)
    mid = int(length/2)
    if length % 2 == 0:
        return (nums[mid-1] + nums[mid])/2
    else:
        return nums[mid]

def mode(nums):
    num = None
    freq = 0
    for n in nums:
        c = nums.count(n)
        if c > freq:
            num = n
            freq = c 
    return num

def choice(choice, lst):
    if choice == 1:
        return mean(lst)
    elif choice == 2:
        return median(lst)
    elif choice == 3:
        return mode(lst)
    
print(choice(select, lst))