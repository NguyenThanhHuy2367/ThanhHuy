# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:46:04 2024

@author: NGUYEN THANH HUY
"""

N=int(input("Nhập số nguyên dương N có 2 chữ số: "))
if 10<=N<=99:
    hangdonvi = N//10
    hangchuc= N%10
    tongchuso= hangdonvi + hangchuc
    print(" Tổng các số của N là:", tongchuso)
