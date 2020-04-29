def rgb():
    clr = input('Please enter the RGB(A) CSS colour: ')
    clr = clr.lower()
    if clr[:3] == 'rgb' or clr[:4] == 'rgba':
        if clr[:4] =='rgba':
            newCol = clr[5:len(clr)-1]
            nums = newCol.split(',')
            if len(nums) == 4:
                for i in range(len(nums)-1):
                    if 0 > int(nums[i]) or 255 < int(nums[i]):
                        return False
                if float(nums[3]) >= 1 or float(nums[3]) <= 0:
                    return False
                return True
        elif clr[:3] == 'rgb':
            newCol = clr[4:len(clr)-1]
            nums = newCol.split(',')
            if len(nums) == 3:
                for i in nums:
                    if 0 > int(i) or int(i) > 255:
                        return False
                return True
    return False


print(rgb())