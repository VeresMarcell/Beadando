# 34. Készítsen programot, amely eldönti egy bemeneti string-ről, hogy az helyes RGB(A) CSS
# szín-e.
# A feltételek a következők: a string úgy kezdődik, hogy rgb vagy rgba. Ha rgb akkor 3 szám
# szerepel a zárójelek között, vesszővel elválasztva [0,255] intervallumon. Ha rgba akkor 4
# szám, az első 3 a [0,255] intervallumon a negyedik pedig [0,1] intervallumon.

def rgb():
    clr = input('Please enter the RGB(A) CSS colour: ')
    clr = clr.lower()
    if clr[:3] == 'rgb' or clr[:4] == 'rgba':       #betűk vizsgálata
        if clr[:4] =='rgba':
            newCol = clr[5:len(clr)-1]      #számok leválasztása
            nums = newCol.split(',')
            if len(nums) == 4:      #elég szám van?
                for i in range(len(nums)-1):        #számok tartománya
                    if 0 > int(nums[i]) or 255 < int(nums[i]):
                        return False
                if float(nums[3]) >= 1 or float(nums[3]) <= 0:
                    return False
                return True
        elif clr[:3] == 'rgb':      #betűk
            newCol = clr[4:len(clr)-1]
            nums = newCol.split(',')
            if len(nums) == 3:  #szám
                for i in nums:      #tartomány
                    if 0 > int(i) or int(i) > 255:
                        return False
                return True
    return False


print(rgb())