# -*- coding: utf-8 -*-
"""
Created on Wed May 30 17:06:21 2018

@author: w
"""
import pandas as pd

#读取combined_05.csv文件，并把‘Temp’，‘CO2’,'RH','THI'列的值都转化为数值型，以免统计出现错误
combined_file = pd.read_csv(r'C:\Yu\THI_up to date_0729_v2.csv')
combined_file['Temp'] = pd.to_numeric(combined_file['Temp'], errors='coerce')
combined_file['CO2'] = pd.to_numeric(combined_file['CO2'], errors='coerce')
combined_file['RH'] = pd.to_numeric(combined_file['RH'], errors='coerce')
combined_file['THI'] = pd.to_numeric(combined_file['THI'], errors='coerce')


#所有方位列表
group_list_1 = ['7A', '7B']
group_list_2 = ['west', 'center', 'east']
group_list_3 = ['north', 'midpoint', 'south']
group_list_4 = ['lower', 'middle', 'upper']
group_list_1_1 = ['baffles', 'outdoor', 'plenum']


"""
get_max_min_sn是用来获取最大最小值各自对应的SN
"""
def get_max_min_sn(dateframe1, index, mm_value):
    
    if mm_value != 0:
        sn_str = ''
        query_str = "{A} == {B}".format(A = index, B = mm_value)
        mm_file = dateframe1.query(query_str)      
        for i in list(mm_file['SN']):
            sn_str += str(i) + '/'
        return sn_str
    else:
        return 'None'

"""
statisticsColumnsNames是用来统一化保存CSV的列名的
"""
def statisticsColumnsNames(tag):
    return ['DateTime','Group1', 'Group2', 'Group3', 
            'Group4', tag + '_Avg', tag + '_Std', tag + '_Max', 
            tag + '_Max_SN', tag + '_Min', tag + '_Min_SN'] 



"""
statistics_core是统计的核心功能
"""
def statistics_core(tag, new_file1, start_t, end_t, df_file_list):
    for group_temp_1 in group_list_1:
        new_file2 = new_file1.loc[new_file1['house'] == group_temp_1]
        for group_temp_2 in group_list_2:
            new_file3 = new_file2.loc[new_file2['east_west lane'] == group_temp_2]
            for group_temp_3 in group_list_3:
                new_file4 = new_file3.loc[new_file3['north_south lane'] == group_temp_3]
                for group_temp_4 in group_list_4:
                    new_file = new_file4.loc[new_file4['upper_lower lane'] == group_temp_4, ['SN', 'DateTime', tag]]
                    tag_min = new_file[tag].min() if new_file[tag].min() > -100 else -100                   
                    tag_max = new_file[tag].max() if new_file[tag].max() > -100 else -100                    
                    tag_min_sn = get_max_min_sn(new_file, tag, tag_min)
                    tag_max_sn = get_max_min_sn(new_file, tag, tag_max)
                    tag_row = {'DateTime': start_t + '-' + end_t, 'Group1': group_temp_1, 
                               'Group2': group_temp_2, 'Group3': group_temp_3, 
                               'Group4': group_temp_4, (tag + '_Avg'): new_file[tag].mean(), 
                               (tag + '_Std'): new_file[tag].std(), (tag + '_Max'): tag_max, 
                               (tag + '_Max_SN'): tag_max_sn, (tag + '_Min'): tag_min, 
                               (tag + '_Min_SN'): tag_min_sn}
                    tag_df = pd.DataFrame(tag_row, index = [0])
                    df_file_list.append(tag_df)
    for group_temp_1_1 in group_list_1_1:
        new_file = new_file1.loc[new_file1['house'] == group_temp_1_1, ['SN', 'DateTime', tag]]
        tag_min = new_file[tag].min() if new_file[tag].min() > -100 else -100
        tag_max = new_file[tag].max() if new_file[tag].max() > -100 else -100
        tag_min_sn = get_max_min_sn(new_file, tag, tag_min)
        tag_max_sn = get_max_min_sn(new_file, tag, tag_max)
        tag_row = {'DateTime': start_t + '-' + end_t, 'Group1': group_temp_1_1, 'Group2': 'ALL', 'Group3': 'ALL', 'Group4': 'ALL', (tag + '_Avg'): new_file[tag].mean(), (tag + '_Std'): new_file[tag].std(), (tag + '_Max'): tag_max, (tag + '_Max_SN'): tag_max_sn, (tag + '_Min'): tag_min, (tag + '_Min_SN'): tag_min_sn}
        tag_df = pd.DataFrame(tag_row, index = [0])
        df_file_list.append(tag_df)


#-----------------------------------按小时统计--------------------------------------------
def statistics_byhour(tag, startTime, endTime, combined_file, group_list_1, group_list_2, group_list_3, group_list_4, group_list_1_1):
    df_file_list = []
    startTime += ' 00:00:00'
    endTime += ' 00:00:00'
    if tag == 'CO2':
        new_combined_file = combined_file.loc[(combined_file['DateTime'] < endTime) & 
                                          (combined_file['DateTime'] >= startTime) &
                                          (combined_file['CO2'] != -1)]
    else:
        new_combined_file = combined_file.loc[(combined_file['DateTime'] < endTime) & 
                                          (combined_file['DateTime'] >= startTime)]
    date_set = set()
    date_list = []
    for datetime in new_combined_file['DateTime']:
        date_set.add(datetime[0: 10])
    
    for i in date_set:
        date_list.append(i)
    
    date_list.sort()
    
    for date_temp in date_list:
        print(date_temp)
        for i in range(24):
            s_t = ('0' + str(i)) if i < 10 else (str(i))
            e_t = ('0' + str(i + 1)) if (i + 1) < 10 else (str(i + 1))
            start_t = date_temp + ' ' + s_t + ':00:00'
            end_t = date_temp + ' ' + e_t + ':00:00' 
            new_file1 = new_combined_file.loc[(new_combined_file['DateTime'] < end_t) & (new_combined_file['DateTime'] >= start_t)]
            statistics_core(tag, new_file1, start_t, end_t, df_file_list)
            
    return pd.concat(df_file_list)
#-----------------------------------------------------------------------------------------------


#---------------------------------------按天统计-------------------------------------------------
def statistics_byday(tag, startTime, endTime, combined_file, group_list_1, group_list_2, group_list_3, group_list_4, group_list_1_1):
    df_file_list = []
    startTime += ' 00:00:00'
    endTime += ' 00:00:00'
    if tag == 'CO2':
        new_combined_file = combined_file.loc[(combined_file['DateTime'] < endTime) & 
                                          (combined_file['DateTime'] >= startTime) &
                                          (combined_file['CO2'] != -1)]
    else:
        new_combined_file = combined_file.loc[(combined_file['DateTime'] < endTime) & 
                                          (combined_file['DateTime'] >= startTime)]
    date_set = set()
    date_list = []
    for datetime in new_combined_file['DateTime']:
        date_set.add(datetime[0: 10])
    
    for i in date_set:
        date_list.append(i)
    
    date_list.sort()
    
    for date_temp in date_list:
        start_t = date_temp + ' 00:00:00'
        end_t = date_temp + ' 24:00:00'
        print(start_t)
        new_file1 = new_combined_file.loc[(new_combined_file['DateTime'] < end_t) & (new_combined_file['DateTime'] >= start_t)]
        statistics_core(tag, new_file1, start_t, end_t, df_file_list)
        
    return pd.concat(df_file_list)
#--------------------------------------------------------------------------------------------------------        


#-------------------------------------按6小时间隔统计-----------------------------------------------------
def statistics_by4times(tag, startTime, endTime, combined_file, group_list_1, group_list_2, group_list_3, group_list_4, group_list_1_1):
    df_file_list = []
    startTime += ' 00:00:00'
    endTime += ' 00:00:00'
    if tag == 'CO2':
        new_combined_file = combined_file.loc[(combined_file['DateTime'] < endTime) & 
                                          (combined_file['DateTime'] >= startTime) &
                                          (combined_file['CO2'] != -1)]
    else:
        new_combined_file = combined_file.loc[(combined_file['DateTime'] < endTime) & 
                                          (combined_file['DateTime'] >= startTime)]
    date_set = set()
    date_list = []
    for datetime in new_combined_file['DateTime']:
        date_set.add(datetime[0: 10])
    
    for i in date_set:
        date_list.append(i)
    
    date_list.sort()
    
    for date_temp in date_list:
        print(date_temp)
        for i in range(0, 24, 6):
            s_t = ('0' + str(i)) if i < 10 else (str(i))
            e_t = ('0' + str(i + 6)) if (i + 6) < 10 else (str(i + 6))
            start_t = date_temp + ' ' + s_t + ':00:00'
            end_t = date_temp + ' ' + e_t + ':00:00' 
            new_file1 = new_combined_file.loc[(new_combined_file['DateTime'] < end_t) & (new_combined_file['DateTime'] >= start_t)]
            statistics_core(tag, new_file1, start_t, end_t, df_file_list)
        
    return pd.concat(df_file_list)      
#------------------------------------------------------------------------------------------------------------------        

                     
'''
statistics_byXXX函数的第一个参数tag,用来表示统计参数的类别
分别有：'Temp','RH','CO2'
'''
temp_byhour = statistics_byhour('Temp', '2018-07-20', '2018-07-23',combined_file,group_list_1, group_list_2, group_list_3, group_list_4, group_list_1_1)

co2_by4times = statistics_by4times('CO2', '2018-07-20', '2018-07-25',combined_file,group_list_1, group_list_2, group_list_3, group_list_4, group_list_1_1)

thi = statistics_byday('THI', '2018-07-23', '2018-07-29',combined_file,group_list_1, group_list_2, group_list_3, group_list_4, group_list_1_1)

#保存文件
thi.to_csv(r'C:\Yu\up to date_0729_v8_statistics_byd_thi.csv',
           encoding="utf_8",index = False,columns = statisticsColumnsNames('THI'))


