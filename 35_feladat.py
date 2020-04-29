def rgb():
    clr = input('Please enter the RGB(A) CSS colour: ')
    clr = clr.lower()
    if clr[:3] == 'rgb' or clr[:4] == 'rgba':
        if clr[:3] == 'rgb':
            newCol = clr[4:len(clr)-1]
            nums = newCol.split(',')
            newNum =[]
            for i in range(len(nums)):
                newNum.append(int(nums[i]))
            print(newNum)
    return False


print(rgb())