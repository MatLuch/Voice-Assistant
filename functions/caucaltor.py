def cauc(text):
    if "plus" in text or "minus" in text:
        nums = []
        i = 0
        while i < len(text):
            if text[i].isdigit():
                count = 0
                hold = ""
                while(i + count < len(text) and text[i + count].isdigit()):
                    hold += text[i + count]
                    count += 1
                nums.append(hold)
                i += count
                count = 0
            else: 
                i += 1
        end = 0

        if "plus" in text and len(nums) >= 1:
            for i in range(len(nums)):
                end += int(nums[i])
        elif "minus" in text and len(nums) >= 1:
            end += int(nums[0])
            for i in range(len(nums)):
                if i > 0:
                    end -= int(nums[i])

        return "The answer is: " + str(end)