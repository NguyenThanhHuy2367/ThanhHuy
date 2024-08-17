# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:51:29 2024

@author: NGUYEN THANH HUY
"""

import calendar

year = int(input("Nhập năm: "))
is_leap = calendar.isleap(year)
print(f"{year} là năm nhuận" if is_leap else f"{year} không phải là năm nhuận")