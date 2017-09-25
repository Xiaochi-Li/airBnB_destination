#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 06:01:28 2017

@author: lixiaochi
"""
from sklearn import preprocessing
import pandas as pd

# prarm only one column of data
# return an encoder that can 
def lable_encode (df):
    # list record all data category in column
    
#    column_value_category =[]
#    for data in column:
#        if data not in column_value_category:
#            column_value_category.append(data)
           
    # string value encoder
    le = preprocessing.LabelEncoder()
    df_lable_encoded = df.apply(le.fit_transform)
    return df_lable_encoded

def one_hot_encode (df):
#    ohe = preprocessing.OneHotEncoder()
#    ohe.fit(df)
#    return ohe.transform(df).toarray()
    return pd.get_dummies(df.language)

