#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 07:27:58 2017

@author: lixiaochi
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import UserIntegrater

#load file
df = pd.read_csv('../data/origin/sessions.csv')
#delete row if user_id or secs_elapsed is nan

allSessions = pd.DataFrame()

currentRowId = "d1mm9tcy42"
newData = {'user_id': '',
           'action':{},
           'action_type':{},
           'action_detail':{},
           'device_type': {},
           'secs_elapsed': {
                   'sum':0,
                   'mean':0,
                   'min':0,
                   'max':0,
                   'std':0}}
secs_elapsed = []    
userInfo = pd.DataFrame()


rowNum = 0
for row in df.iterrows():
    if row[1].user_id == currentRowId:
        if newData['user_id'] == '':
            newData['user_id'] = currentRowId
            
        if row[1].action in newData['action']:
            newData['action'][row[1].action] += 1
        else:
            newData['action'][row[1].action] = 1
        if row[1].action_type in newData['action_type']:
            newData['action_type'][row[1].action_type] += 1
        else:
            newData['action_type'][row[1].action_type] = 1
            
        if row[1].action_detail in newData['action_detail']:
            newData['action_detail'][row[1].action_detail] += 1
        else:
            newData['action_detail'][row[1].action_detail] = 1 
        if row[1].device_type in newData['device_type']:
            newData['device_type'][row[1].device_type] += 1
        else:
            newData['device_type'][row[1].device_type] = 1 
        
        if not pd.isnull(df.loc[rowNum, 'secs_elapsed']):
            secs_elapsed.append(row[1].secs_elapsed)
        rowNum +=1
        
        
    elif pd.isnull(df.loc[rowNum, 'user_id']):
        df.drop(df.index[rowNum])
        rowNum +=1
    elif pd.isnull(df.loc[rowNum, 'secs_elapsed']):
        df.drop(df.index[rowNum])
        rowNum +=1
        print df.index[rowNum]
        
    else:
        newData['secs_elapsed']['sum'] = np.sum(secs_elapsed)
        newData['secs_elapsed']['mean'] = np.mean(secs_elapsed)
        if len(secs_elapsed) ==1:
            newData['secs_elapsed']['min'] = secs_elapsed[0]
            newData['secs_elapsed']['max'] = secs_elapsed[0]
        else:
            newData['secs_elapsed']['min'] = np.min(secs_elapsed)
            newData['secs_elapsed']['max'] = np.max(secs_elapsed)
        newData['secs_elapsed']['std'] = np.std(secs_elapsed)
       
        #build an data frame row based on newData
        userInfo['user_id'] = [newData['user_id']]
        for key,value in newData['action'].items():
            userInfo["action"+ "_" + str(key) ] = [value]
        for key,value in newData['action_type'].items():
            userInfo['action_type'+ '_'+ str(key) ] = [value]
        for key,value in newData['action_detail'].items():
            userInfo['action_detail'+ '_'+ str(key) ] = [value]
        for key,value in newData['device_type'].items():
            userInfo['device_type'+ '_'+ str(key) ] = [value]
        for key,value in newData['secs_elapsed'].items():
            userInfo['secs_elapsed'+ '_'+ str(key) ] = [value]  
        
        allSessions = allSessions.append(userInfo, ignore_index=True)
        
        
        currentRowId = row[1].user_id
        secs_elapsed = [] 
        newData={'user_id': '',
           'action':{},
           'action_type':{},
           'action_detail':{},
           'device_type': {},
           'secs_elapsed': {
                   'sum':0,
                   'mean':0,
                   'min':0,
                   'max':0,
                   'std':0}}
        
        if newData['user_id'] == '':
            newData['user_id'] = currentRowId
            
        if row[1].action in newData['action']:
            newData['action'][row[1].action] += 1
        else:
            newData['action'][row[1].action] = 1
        if row[1].action_type in newData['action_type']:
            newData['action_type'][row[1].action_type] += 1
        else:
            newData['action_type'][row[1].action_type] = 1
            
        if row[1].action_detail in newData['action_detail']:
            newData['action_detail'][row[1].action_detail] += 1
        else:
            newData['action_detail'][row[1].action_detail] = 1 
        if row[1].device_type in newData['device_type']:
            newData['device_type'][row[1].device_type] += 1
        else:
            newData['device_type'][row[1].device_type] = 1 
        
        if not pd.isnull(df.loc[rowNum, 'secs_elapsed']):
            secs_elapsed.append(row[1].secs_elapsed)
        rowNum +=1
        print df.index[rowNum]

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
allSessions.to_excel(writer, sheet_name='Sheet1')
 print df.index[rowNum]
# Close the Pandas Excel writer and output the Excel file.
writer.save()
        



    
        
