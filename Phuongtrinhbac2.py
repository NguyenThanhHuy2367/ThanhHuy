# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:36:15 2024

@author: NGUYEN THANH HUY
"""
import math 
a=float(input("nhap he so a="))
b=float(input("nhap he so b="))
c=float(input("nhap he so c="))
delta=b**2 - 4*a*c
if delta < 0:
    print("phuong trinh vo nghiem")
elif delta ==0:
    x= -b/(2*a)
    print("phuong trinh co nghiem kep x1= x2=",x)
elif delta > 0:
    x1 = (-b + math.sqrt(delta)/2*a)
    x2 = (-b - math.sqrt(delta)/2*a)
    print("phuong trinh co hai nghiem phan biet x1= x2=", x1,x2)