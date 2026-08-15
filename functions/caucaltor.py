import math
import operator
def cauc(text):
    nums = []
    hold = ""

    for char in text:
        if char.isdigit():
            hold += char
        elif hold: # checks if the last one is false and hold contains something
            nums.append(int(hold))
            hold = ""

    if hold: 
        nums.append(int(hold))

    if "+" in text:
        answer = sum(nums)

    elif "-" in text:
        answer = nums[0] - sum(nums[1:])

    elif "*" in text:
        answer = math.prod(nums)

    elif "/" in text:
        answer = nums[0]
        for num in nums[1:]:
            answer /= nums 
    
    return "the answer is: " + str(answer)