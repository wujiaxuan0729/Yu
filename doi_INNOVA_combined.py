# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 12:36:42 2018

@author: abe
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime,timedelta
import time

doi = pd.read_csv(r'C:\Users\wujia\Desktop\git TUT\yu date\dol.csv')
INNOVA = pd.read_csv(r'C:\Users\wujia\Desktop\git TUT\yu date\INNOVA.csv')

doi['NH3_INNOVA_avg'] = None
doi['AmT_ave'] = None
doi['C1T_ave'] = None
doi['AmRH_ave'] = None
doi['C1Airflow_ave'] = None
doi['C1RH_avg'] = None

#doi

doi_row_num = len(doi.values)

minute_pre = ''
NH3_INNOVA_avg = 0
AmT_ave = 0
C1T_ave = 0
AmRH_ave = 0
C1Airflow_ave = 0
C1RH_avg = 0

for i in range(doi_row_num):
    date = doi['Date'][i]
    time = doi['Time'][i]
    
    hour_s = str(time[0 : 2])
    minute_s = str(time[3 : 5])
    second_s = str(time[6 : 8])
    
    hour_i = int(hour_s)
    minute_i = int(minute_s)
    second_i = int(second_s)
    
    start_time = hour_s + ':' + minute_s + ':' + '00'
    if minute_i != 59:
        m_temp = str(minute_i + 1) if minute_i >= 9 else ('0' + str(minute_i + 1))  
        end_time = hour_s + ':' + m_temp + ':' + '00'
    else:
        h_temp = str(hour_i + 1) if hour_i >= 9 else ('0' + str(hour_i + 1))
        end_time = h_temp + ':' + '00:00'
    
    if minute_s != minute_pre:
        
        minute_pre = minute_s
        INNOVA_minute_avg = INNOVA.loc[(INNOVA['Date'] == date) & (INNOVA['Time'] >= start_time) & (INNOVA['Time'] < end_time)]
        
        NH3_INNOVA_avg = INNOVA_minute_avg['NH3'].mean()
        doi['NH3_INNOVA_avg'][i] = NH3_INNOVA_avg
        
        AmT_ave = INNOVA_minute_avg['Ambient T'].mean()
        doi['AmT_ave'][i] = AmT_ave
        
        C1T_ave = INNOVA_minute_avg['C1 T'].mean()
        doi['C1T_ave'][i] = C1T_ave
        
        AmRH_ave = INNOVA_minute_avg['Ambient RH'].mean()
        doi['AmRH_ave'][i] = AmRH_ave
        
        C1Airflow_ave = INNOVA_minute_avg['C1 airflow'].mean()
        doi['C1Airflow_ave'][i] = C1Airflow_ave
        
        C1RH_avg = INNOVA_minute_avg['C1 RH'].mean()
        doi['C1RH_avg'][i] = C1RH_avg
    else:
        doi['NH3_INNOVA_avg'][i] = NH3_INNOVA_avg
        
        doi['AmT_ave'][i] = AmT_ave
        
    
        
        doi['C1T_ave'][i] = C1T_ave
        
        doi['AmRH_ave'][i] = AmRH_ave
        
        doi['C1Airflow_ave'][i] = C1Airflow_ave
        
        doi['C1RH_avg'][i] = C1RH_avg
    
    print('finish', i, 'line')
    
    
columns_list_new = ['Date', 'Time', 'dol_1', 'dol_2', 'dol_3', 'dol_4', 
                    'dol_5', 'dol_6', 'dol_7', 'dol_8', 'NH3_INNOVA_avg', 'AmT_ave',
                    'C1T_ave', 'AmRH_ave', 'C1Airflow_ave', 'C1RH_avg']

doi.to_csv(r'C:\Users\wujia\Desktop\git TUT\yu date\dol_v2.csv',encoding="utf_8",index = False, columns=columns_list_new)

    
    