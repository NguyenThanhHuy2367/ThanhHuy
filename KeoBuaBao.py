# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:19:35 2024

@author: NGUYEN THANH HUY
"""

My=float(input("Người chơi chọn(1.Bao, 2.Búa, 3.Kéo):"))
from random import randint
com=randint(1,3)
if com==1:
    print("Robot chọn bao")
elif com==2:
    print("Robot chọn búa")
elif com==3:
    print("Robot chọn kéo")
if com==My:
    print("Kết quả hoà")
elif com==1 and My==2:
    print("My Thua, Robot thắng")
elif com==1 and My==3:
    print("My thắng, Robot thua")
elif com==2 and My==1:
    print("My thắng, Robot thua")
elif com==2 and My==3:
    print("My thua, Robot thắng")
elif com==3 and My==1:
    print("My thua, Robot thắng")
elif com==3 and My==2:
    print("My thắng, Robot thua")
else:
    print("không hợp lệ")