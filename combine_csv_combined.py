# -*- coding: utf-8 -*-
"""
Created on Wed May 30 14:32:27 2018

@author: wujia
"""

import pandas as pd
import numpy as np
import os


dir_name = r'D:\Yu data_0719\wjx\wjx_1'
frame = []
#获取dir_now目录下的所有csv文件名，保存在files列表中
for root, dirs, files in os.walk(dir_name):  
   pass

for combined_csv_name in files:
    full_combined_csv_dir = dir_name + '\\' + str(combined_csv_name)
    wjx = pd.read_csv(full_combined_csv_dir)
    frame.append(wjx)

new_result = pd.concat(frame)
#new_result

new_result = new_result.sort_index(axis = 0,ascending = True,by = ['SN', 'DateTime'])

new_result = new_result.drop_duplicates(['SN','DateTime'], keep = 'first')
#new_result

columns_list_new = ['SN','DateTime','Temp','RH', 'CO2', 'DewPt', 'house', 'east_west lane', 'north_south lane', 'upper_lower lane']
new_result.to_csv(r'D:\Yu data_0719\wjx\wjx_1\combined_0719_v2.csv',encoding="utf_8",index = False, columns=columns_list_new)
