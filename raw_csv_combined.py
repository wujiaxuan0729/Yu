import pandas as pd
import numpy as np
import os


#house
house_7A = ['20299495', '20299494', '20311776',
            '20318222', '20313845', '20318225',
            '20299504', '20311783', '20311778',
            '20311780', '20299500', '20311789',
            '20313847', '20313849', '20318230',
            '20299496', '20299493', '20299505',
            '20311787', '20299497', '20311791',
            '20318227', '20318224', '20313846',
            '20311788', '20311774', '20311786','20299502']

house_7B = ['20299491', '20311784',	'20311781',
            '20318237', '20318223',	'20318234',
            '20299499', '20311769',	'20299501',
            '20299490', '20311777',	'20299503',
            '20318229', '20318233',	'20318235',
            '20311792', '20311790',	'20311785',
            '20299492', '20311782',	'20311779',
            '20318231', '20318232',	'20313848',
            '20311773', '20299498',	'20311775']

house_baffles = ['20315101',	'20315104', '20315109', '20315103', '20315111', '20315113']

house_outdoor = ['20315107', '20315114']

house_plenum = ['20318236', '20315112', '20315110', '20318228', '20315115', '20315102', '20315106', '20318226', '20315108']

def locationHouse(x):
    x = str(x)
    if x in house_7A:
        return '7A'
    elif x in house_7B:
        return '7B'
    elif x in house_baffles:
        return 'baffles'
    elif x in house_outdoor:
        return 'outdoor'
    elif x in house_plenum:
        return 'plenum'

#east_west lane
east_west_east = ['20311776', '20318225', '20311778', 
                  '20311789', '20318230', '20299505', 
                  '20311791', '20313846',	'20311786', 
                  '20311781', '20318234', '20299501', 
                  '20299503', '20318235', '20311785', 
                  '20311779',	'20313848', '20311775']

east_west_center = ['20299494', '20313845', '20311783', 
                    '20299500', '20313849', '20299493', 
                    '20299497', '20318224', '20311774', 
                    '20311784', '20318223', '20311769', 
                    '20311777', '20318233', '20311790', 
                    '20311782', '20318232', '20299498']

east_west_west = ['20299495', '20318222', '20299504', 
                  '20311780', '20313847', '20299496', 
                  '20311787', '20318227', '20311788', 
                  '20299491', '20318237', '20299499', 
                  '20299490', '20318229', '20311792', 
                  '20299492', '20318231', '20311773', '20299502']

def locationEastwest(x):
    x = str(x)
    if x in east_west_east:
        return 'east'
    elif x in east_west_center:
        return 'center'
    elif x in east_west_west:
        return 'west'
    

#north_south lane
north_south_north = ['20299495', '20299494', '20311776',
                     '20318222', '20313845', '20318225',
                     '20299504', '20311783', '20311778',
                     '20299491', '20311784', '20311781',
                     '20318237', '20318223', '20318234',
                     '20299499', '20311769', '20299501', '20299502']

north_south_midpoint = ['20311780', '20299500', '20311789',
                        '20313847', '20313849', '20318230',
                        '20299496', '20299493', '20299505',
                        '20299490', '20311777', '20299503',
                        '20318229', '20318233', '20318235',
                        '20311792', '20311790', '20311785']

north_south_south = ['20311787', '20299497', '20311791',
                     '20318227', '20318224', '20313846',
                     '20311788', '20311774', '20311786',
                     '20299492', '20311782', '20311779',
                     '20318231', '20318232', '20313848',
                     '20311773', '20299498', '20311775']


def locationNorthsouth(x):
    x = str(x)
    if x in north_south_north:
        return 'north'
    elif x in north_south_midpoint:
        return 'midpoint'
    elif x in north_south_south:
        return 'south'
    
    
#upper_lower lane
upper_lower_upper = ['20311776', '20311789', '20311791', '20311781', '20299503', '20311779',
                     '20299494', '20299500', '20299497', '20311784', '20311777', '20311782',
                     '20299495', '20311780', '20311787', '20299491', '20299490', '20299492']

upper_lower_middle = ['20318225', '20318230', '20313846', '20318234', '20318235', '20313848',
                      '20313845', '20313849', '20318224', '20318223', '20318233', '20318232',
                      '20318222', '20313847', '20318227', '20318237', '20318229', '20318231']

upper_lower_lower = ['20311778', '20299505', '20311786', '20299501', '20311785', '20311775',
                     '20311783', '20299493', '20311774', '20311769', '20311790', '20299498',
                     '20299504', '20299496', '20311788', '20299499', '20311792', '20311773', '20299502']

def locationUpperower(x):
    x = str(x)
    if x in upper_lower_upper:
        return 'upper'
    elif x in upper_lower_middle:
        return 'middle'
    elif x in upper_lower_lower:
        return 'lower'


dir_now = r'D:\yu data\wjx\CO2_csv\top_middle'
new_file_list = []
#获取dir_now目录下的所有csv文件名，保存在files列表中
for root, dirs, files in os.walk(dir_now):  
   pass

k = 0
for temp_file_name in files:
    #截取传感器标识‘sn’
    sn = temp_file_name[3:11]
    new_index = 0
    new_file = pd.DataFrame({'SN': [], 'DateTime': [], 'Temp': [], 'RH': [], 'CO2': [], 'DewPt': [], 'Auto': []})
    old_file = pd.read_csv((dir_now + '\\' + temp_file_name), skiprows = 2)
    rows_num = len(old_file.values)
    columns_name = old_file.columns
    
    for i in range(rows_num):
        if 'CO2, (ppm)' in columns_name:
            
            
            temp = {'SN': sn, 'DateTime': old_file['Date Time, GMT -0500'][i], 'Temp': old_file['Temp, (*C)'][i], 'RH': old_file['RH, (%)'][i], 'CO2': old_file['CO2, (ppm)'][i], 'DewPt': old_file['DewPt, (*C)'][i], 'Auto': old_file['Auto Calibration, (ppm)'][i]}
        else:
            temp = {'SN': sn, 'DateTime': old_file['Date Time, GMT -0500'][i], 'Temp': old_file['Temp, (*C)'][i], 'RH': old_file['RH, (%)'][i], 'CO2': '-1', 'DewPt': old_file['DewPt, (*C)'][i], 'Auto': old_file['Auto Calibration, (ppm)'][i]}
        new_file.loc[new_index] = temp
        new_index += 1
    new_file_list.append(new_file)
    print('finish', k)
    k += 1

print(len(new_file_list))

new_result = pd.concat(new_file_list)
new_result






new_result = new_result.sort_index(axis = 0,ascending = True,by = ['SN', 'DateTime'])

new_result = new_result.drop_duplicates(['SN','DateTime'], keep = 'first')
new_result

'''
new_result['house'] = new_result['SN'].apply(locationHouse)
new_result['east_west lane'] = new_result['SN'].apply(locationEastwest)
new_result['north_south lane'] = new_result['SN'].apply(locationNorthsouth)
new_result['upper_lower lane'] = new_result['SN'].apply(locationUpperower)
new_result
'''

columns_list_new = ['SN','DateTime','Temp','RH', 'CO2', 'DewPt', 'Auto']
new_result.to_csv(r"D:\yu data\wjx\CO2_csv\top_middle\CO2_1.csv",encoding="utf_8",index = False, columns=columns_list_new)
