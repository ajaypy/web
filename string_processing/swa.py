nums = [1,3,2,4,5,8,7,10,14,11,12]

def find_swapped(nums):
    n = len(nums)
    x = y = -1

    for i in range(n - 1):
        print (x,y)
        if nums[i+1] < nums[i]:
            y = nums[i+1]

            if x == -1:
                x = nums[i]
            #else:
            #    break

    return x,y

print (find_swapped(nums))


