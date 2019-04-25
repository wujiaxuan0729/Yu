# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 00:55:47 2018

@author: wujia
"""
#引入pandas包
import pandas as pd
import numpy as np
#打开指定的CSV文件
old_file = pd.read_csv(r'C:\Users\wujia\Desktop\git TUT\yu date\combined_0622.csv')

#这两行功能是将Temp和dewPt列转化为数值型，防止万一是字符串型会影响计算
old_file['Temp'] = pd.to_numeric(old_file['Temp'], errors='coerce')
old_file['DewPt'] = pd.to_numeric(old_file['DewPt'], errors='coerce')

#添加新的THI列，该列每行的值为Temp、DewPt列对应行值的运算。因为是矩阵运算，直接写成这样就行，会依次将每一行的新值赋给THI列上
old_file['THI'] = 0.6 * old_file['Temp'] + 0.4 * 0.5 * (old_file['Temp'] + old_file['DewPt'])

#以columns_list_new标明的列顺序进行CSV保存
columns_list_new = ['SN', 'DateTime','Temp','RH','CO2', 'DewPt', 'house', 
                    'east_west lane', 'north_south lane', 'upper_lower lane', 'THI']
old_file.to_csv(r"C:\Users\wujia\Desktop\git TUT\yu date\THI_combined_0622.csv",encoding="utf_8",index = False, columns=columns_list_new)
