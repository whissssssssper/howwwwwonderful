# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cmath

def quadratic_formula(a, b, c):
    # 計算判別式
    discriminant = b**2 - 4*a*c

    # 判斷是否有實根
    if discriminant >= 0:
        # 有實根
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    else:
        # 無實根，有虛根
        real_part = -b / (2*a)
        imag_part = cmath.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
        return root1, root2

# 輸入係數
a = float(input("請輸入a的值： "))
b = float(input("請輸入b的值： "))
c = float(input("請輸入c的值： "))

# 計算解
root1, root2 = quadratic_formula(a, b, c)

# 輸出解
print("解為:", root1, "和", root2)
