# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 17:13:37 2018

@author: abe
"""

import pandas as pd

old_file = pd.read_csv(r'C:\Yu\csv_0820\combined_0820.csv')

# 选择DateTime小于‘2018-08-09 00:00:00’的数据
old_file = old_file.loc[(old_file['DateTime'] < '2018-08-09 00:00:00')]

columns_list_new = ['SN','DateTime','Temp','RH', 'CO2', 'DewPt', 'house', 'east_west lane', 'north_south lane', 'upper_lower lane']
old_file.to_csv(r"C:\Yu\csv_0820\combined_0808.csv",encoding="utf_8",index = False, columns=columns_list_new)

old_file = pd.read_csv(r'C:\Yu\csv_0820\combined_0820.csv')

old_file = old_file.loc[(old_file['DateTime'] >= '2018-08-10 20:00:00') & (old_file['DateTime'] <= '2018-08-12 20:00:00')]

old_file['DateTime']

columns_list_new = ['SN','DateTime','Temp','RH', 'CO2', 'DewPt', 'house', 'east_west lane', 'north_south lane', 'upper_lower lane']
old_file.to_csv(r"C:\Yu\csv_0820\combined_0810-12.csv",encoding="utf_8",index = False, columns=columns_list_new)


