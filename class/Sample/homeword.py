import math
a = input('Chiều dài đáy hình hộp chữ nhật là:')
b = input('Chiều rộng đáy hình hộp chữ nhât là :')
c = input('Chiều cao hình hộp chữ nhât là :')
length = float(a)
width = float(b)
height = float(c)
if (length < width):
    print("Chiều dài không thể nhỏ hơn chiều rộng!!!")
else:
    Sxq = str(round(2*height*(length+width), 4))
    Volume = str(round(height*width*length, 4))
    Stp = str(round((2*height*(length+width) + 2*length*width), 4))
    Maxdiagonalline = str(
        round(math.sqrt(length**2 + width**2 + height**2), 4))
    pi = math.pi
    array = [length, width, height]
    array.sort()
    Vmax = str(round((4/3) * pi * (array[0]/2)**3, 4))

    print('Diện tích xung quanh của hình hộp chữ nhật là :', Sxq + '\n')
    print('Thể tích của hình hộp chữ nhật là : ', Volume + '\n')
    print('Diện tích toàn phần của hình hộp chữ nhật là :', Stp + '\n')
    print('Độ dài đường chéo lớn nhất của hình hộp chữ nhật là : ',
          Maxdiagonalline + '\n')
    print('Thể tích hình cầu lớn nhất nằm trong hình hộp chữ nhật là : ', Vmax + '\n')
    print('HELLO WORLD!!!!!')
