# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:46:02 2024

@author: NGUYEN THANH HUY
"""

a=float(input(" Nhập vào a="))
b=float(input(" Nhập vào b="))
c=float(input(" Nhập vào c="))
if a+b > c or a+c>b or c+b>a:
    print("ba cạnh này toạ thành tam giác")
else:
    print("Ba cạnh này không tạo thành một tam giác")
if a==b==c:
        print("Ba cạnh thành tam giác đều")
elif a**2+b**2==c**2:
        print("Ba cạnh này tạo thành  tam giác vuông")
elif a==b or a==c or a==b:
      print("Ba cạnh thành tâm giác cân")
else:
    print("Ba cạnh toạ thành tam giác thường")