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

    if "plus" in text:
        answer = sum(nums)

    elif "minus" in text:
        answer = nums[0] - sum(nums[1:])

    return "the answer is: " + str(answer)