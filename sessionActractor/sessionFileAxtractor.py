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
df = pd.read_csv('../data/origin/sessions.csv')

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
            newData['user_id'] = row[1].user_id
            
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
        
    else:
        newData['secs_elapsed']['sum'] = np.sum(secs_elapsed)
        newData['secs_elapsed']['mean'] = np.mean(secs_elapsed)
        newData['secs_elapsed']['min'] = np.min(secs_elapsed)
        newData['secs_elapsed']['max'] = np.max(secs_elapsed)
        newData['secs_elapsed']['std'] = np.std(secs_elapsed)
       
        #build an data frame row based on newData
        
        
        break
        currentRowId = row[1].user_id
        print currentRowId
        userInfo = pd.DataFrame()
        newData.clear
        rowNum +=1
        



    
        
