
#Python tasks using function and list;

#1. Given an array of numbers, return true if 6 appears as either the first or last element in the array. The array will be length 1 or more.
def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else: return False
    
print(first_last6([1, 2, 5]))

#2. Given an array of numbers, return true if the array is length 1 or more, and the first element and the last element are equal.
def first_lastequal(nums):
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else: return False

print(first_lastequal([1, 2, 1]))

#3. Return a number array length 3 containing the first 3 digits of pi, [3, 1, 4].
def make_pi():
    return [3, 1, 4]

print(make_pi())

#4. Given 2 arrays of numbers, a and b, return true if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
def same_first_last(a, b):
    if len(a) >= 1 and len(b) >= 1:
        if a[0] == b[0] or a[-1] == b[-1]:
            return True
    return False

print(same_first_last([1, 2, 3], [7, 3]))

#5. Given an array of numbers length 3, return the sum of all the elements.
def sum3(nums):
    return sum(nums)

print(sum3([1, 2, 3]))

#6. Given an array of numbers length 3, return an array with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
def rotate_left3(nums):
    for i in range(len(nums) - 1):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

print(rotate_left3([1, 2, 3]))

#7. Given an array of numbers length 3, return a new array with the elements in reverse order, so [1, 2, 3] becomes [3, 2, 1].
def reverse3(nums):
    return nums[::-1]

print(reverse3([1, 2, 3]))

#8. Given an array of numbers length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
    max_value = max(nums[0], nums[-1])
    return [max_value] * 3

print(max_end3([10, 2, 3]))

#9. Given an array of numbers, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
    if len(nums) >= 2:
        return nums[0] + nums[1]
    elif len(nums) == 1:
        return nums[0]
    else:
        return 0
    
print(sum2([8, 2, 3]))

#10. Given 2 number arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
    return [a[1], b[1]]

print(middle_way([1, 2, 3], [4, 5, 6]))

#11. Given an array of numbers, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
def make_ends(nums):
    return [nums[0], nums[-1]]

print(make_ends([1, 2, 3, 4]))

#12. Given a number array length 2, return true if it contains a 2 or a 3.
def has23(nums):
    for i in nums:
        if i == 2 or i == 3:
            return True
    return False

print(has23([2, 5]))

#13. Given a number array length 2, return true if it does not contain a 2 or 3.
def no23(nums):
    for i in nums:
        if i == 2 or i == 3:
            return False
    return True 
 
print(no23([1, 4]))

#14. Given a number array, return a new array with double the length where its last element is the same as the original array, and all the other elements are 0. The original array will be length 1 or more.
def make_last(nums):
    new_array = [0] * (len(nums) * 2)
    new_array[-1] = nums[-1]
    return new_array

print(make_last([4, 5, 6])) 

#15. Given a number array, return true if the array contains 2 twice, or 3 twice. The array will be length 0, 1, or 2.
def double23(nums):
    for i in nums:
        if nums.count(i) == 2 and (i == 2 or i == 3):
            return True
    return False

print(double23([3, 3]))

#16. Given a number array length 3, if there is a 2 in the array immediately followed by a 3, set the 3 element to 0. Return the changed array. 
def fix23(nums):
    for i in nums:
        if nums[i] == 2 and nums[i + 1] == 3:
            nums[i + 1] = 0
    return nums

print(fix23([1, 2, 3]))

#17. Start with 2 number arrays, a and b, of any length. Return how many of the arrays have 1 as their first element.
def start1(a, b):
    count = 0
    if len(a) > 0 and a[0] == 1:
        count += 1
    if len(b) > 0 and b[0] == 1:
        count += 1
    return count

print (start1([1, 2, 3], [1, 3]))

#18.  Start with 2 number arrays, a and b, each length 2. Consider the sum of the values in each array. Return the array which has the largest sum. In event of a tie, return a.
def biggerTwo(a, b):
    sum1 = 0
    sum2 = 0
    for i in a:
        sum1 += i
    for i in b:
        sum2 += i
    if sum1 > sum2:
        return a
    elif sum2 > sum1:
        return b
    else: 
        return a
    
print(biggerTwo([4, 3], [3, 4]))

#19. Given an array of numbers of even length, return a new array length 2 containing the middle two elements from the original array. The original array will be length 2 or more.
def makeMiddle(nums):
    
