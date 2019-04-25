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
            '20311788', '20311774', '20311786','20299502','20311768']

house_7B = ['20299491', '20311784',	'20311781',
            '20318237', '20318223',	'20318234',
            '20299499', '20311769',	'20299501',
            '20299490', '20311777',	'20299503',
            '20318229', '20318233',	'20318235',
            '20311792', '20311790',	'20311785',
            '20299492', '20311782',	'20311779',
            '20318231', '20318232',	'20313848',
            '20311773', '20299498',	'20311775', '20423038','20284819']

house_baffles = ['20315101',	'20315104', '20315109', '20315103', '20315111', '20315113']

house_outdoor = ['20315107', '20315114', '20186710']

house_plenum = ['20318236', '20315112', '20315110', '20318228', '20315115', '20315102', '20315106', '20318226', '20315108','20423043','20315105']

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
                    '20311782', '20318232', '20299498','20423038','20284819']

east_west_west = ['20299495', '20318222', '20299504', 
                  '20311780', '20313847', '20299496', 
                  '20311787', '20318227', '20311788', 
                  '20299491', '20318237', '20299499', 
                  '20299490', '20318229', '20311792', 
                  '20299492', '20318231', '20311773', '20299502','20311768']

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
                     '20299499', '20311769', '20299501', '20299502','20284819']

north_south_midpoint = ['20311780', '20299500', '20311789',
                        '20313847', '20313849', '20318230',
                        '20299496', '20299493', '20299505',
                        '20299490', '20311777', '20299503',
                        '20318229', '20318233', '20318235',
                        '20311792', '20311790', '20311785','20311768','20423038']

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
                     '20299495', '20311780', '20311787', '20299491', '20299490', '20299492','20311768']

upper_lower_middle = ['20318225', '20318230', '20313846', '20318234', '20318235', '20313848',
                      '20313845', '20313849', '20318224', '20318223', '20318233', '20318232',
                      '20318222', '20313847', '20318227', '20318237', '20318229', '20318231','20423038','20284819']

upper_lower_lower = ['20311778', '20299505', '20311786', '20299501', '20311785', '20311775',
                     '20311783', '20299493', '20311774', '20311769', '20311790', '20299498',
                     '20299504', '20299496', '20311788', '20299499', '20311792', '20311773', '20299502']

def locationUpperlower(x):
    x = str(x)
    if x in upper_lower_upper:
        return 'upper'
    elif x in upper_lower_middle:
        return 'middle'
    elif x in upper_lower_lower:
        return 'lower'

dir_now = r'C:\Yu\csv_0820'
new_file_list = []
#获取dir_now目录下的所有csv文件名，保存在files列表中
for root, dirs, files in os.walk(dir_now):  
   pass


#CO2 大于1000格式转换
def co2ToFloat(x):
    if x == ' ':
        return x
    if type(x) == str and x != '-1':
        if ',' in x:
            x = x.replace(',','')
#        print(x)
        x = float(x)
        return x
    else:
        return x

def strToFloat(x):
    if x == " ":
        return x
    if type(x) == str:
        x = float(x)
        return x
    else:
        return round(x, 2)

k = 0
for temp_file_name in files:
    #截取传感器标识‘sn’
    sn = temp_file_name[3:11]
    files
    #new_index = 0
    #new_file = pd.DataFrame({'SN': [], 'DateTime': [], 'Temp': [], 'RH': [], 'CO2': [], 'DewPt': []})
    try:
        old_file = pd.read_csv((dir_now + '\\' + temp_file_name), skiprows = 2)
    except Exception as e:
        old_file = pd.read_excel((dir_now + '\\' + temp_file_name), skiprows = 1)
        old_file.rename(columns={'Temp, °C': 'Temp, (*C)', 'RH, %': 'RH, (%)', 'CO2, ppm': 'CO2, (ppm)', 'DewPt, °C': 'DewPt, (*C)'}, inplace=True)
    
    cn = old_file.columns
    if 'CO2, (ppm)' in cn:
        old_file.rename(columns={cn[0]: 'DateTime', cn[1]: 'Temp', cn[2]: 'RH', 
                                 cn[3]: 'CO2', cn[4]: 'DewPt'}, inplace=True)
    else:
        old_file.rename(columns={cn[0]: 'DateTime', cn[1]: 'Temp', cn[2]: 'RH', 
                                 cn[3]: 'DewPt'}, inplace=True)
    
    cn = old_file.columns
    if 'CO2' in cn:
        del_columns = set(cn) - set(cn[0 : 5])
    else:
        del_columns = set(cn) - set(cn[0 : 4])
    old_file.drop(list(del_columns), axis = 1, inplace = True)
    
    cn = old_file.columns
    if 'CO2' not in cn:
        old_file['CO2'] = '-1'
    
    old_file['SN'] = sn
    
    old_file = old_file[['SN', 'DateTime', 'Temp', 'RH', 'CO2', 'DewPt']]
    
    #co2 convert
    '''
    old_file['CO2, (ppm)']=old_file['CO2, (ppm)'].apply(co2ToFloat)
    old_file['Date Time, GMT -0500'] = old_file['Date Time, GMT -0500'].apply(pd.to_datetime)
    old_file['Temp, (*C)'] = old_file['Temp, (*C)'].apply(strToFloat)
    old_file['RH, (%)'] = old_file['RH, (%)'].apply(strToFloat)
    old_file['DewPt, (*C)'] = old_file['DewPt, (*C)'].apply(strToFloat)
    '''
    old_file['CO2'] = old_file['CO2'].apply(co2ToFloat)
    old_file['DateTime'] = old_file['DateTime'].apply(pd.to_datetime)
    old_file['Temp'] = old_file['Temp'].apply(strToFloat)
    old_file['RH'] = old_file['RH'].apply(strToFloat)
    old_file['DewPt'] = old_file['DewPt'].apply(strToFloat)
    
    
    '''
    for i in range(rows_num):
        if 'CO2, (ppm)' in columns_name:
            temp = {'SN': sn, 'DateTime': old_file['Date Time, GMT -0500'][i], 'Temp': old_file['Temp, (*C)'][i], 'RH': old_file['RH, (%)'][i], 'CO2': old_file['CO2, (ppm)'][i], 'DewPt': old_file['DewPt, (*C)'][i]}
        else:
            temp = {'SN': sn, 'DateTime': old_file['Date Time, GMT -0500'][i], 'Temp': old_file['Temp, (*C)'][i], 'RH': old_file['RH, (%)'][i], 'CO2': '-1', 'DewPt': old_file['DewPt, (*C)'][i]}
        new_file.loc[new_index] = temp
        new_index += 1
    '''
    
    new_file_list.append(old_file)
    print('finish', k)
    k += 1

#print(len(new_file_list))

new_result = pd.concat(new_file_list)
#new_result






new_result = new_result.sort_index(axis = 0,ascending = True,by = ['SN', 'DateTime'])

new_result = new_result.drop_duplicates(['SN','DateTime'], keep = 'first')
new_result


new_result['house'] = new_result['SN'].apply(locationHouse)
new_result['east_west lane'] = new_result['SN'].apply(locationEastwest)
new_result['north_south lane'] = new_result['SN'].apply(locationNorthsouth)
new_result['upper_lower lane'] = new_result['SN'].apply(locationUpperlower)
new_result


columns_list_new = ['SN','DateTime','Temp','RH', 'CO2', 'DewPt', 'house', 'east_west lane', 'north_south lane', 'upper_lower lane']
new_result.to_csv(r"C:\Yu\csv_0820\combined_0820.csv",encoding="utf_8",index = False, columns=columns_list_new)
