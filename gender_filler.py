#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 07:13:45 2017

@author: lixiaochi
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
import seaborn as sn
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import NearMiss


    
df = pd.read_csv('../../data/train_users_2.csv')


# replace all unknown data with non
df.replace('-unknown-', np.nan, inplace=True)
df = df.dropna()

gender_relat_data = df
#30 data for under sampling
thir_X = gender_relat_data
#other data for upsampling
thir_Y = thir_X.gender
thir_X.drop(['id','gender','date_account_created','country_destination'],1,inplace=True)

# one-hot encoding
oh_signup_method = pd.get_dummies(thir_X.signup_method, prefix="signup_method")
oh_language = pd.get_dummies(thir_X.language, prefix="language")
oh_signup_flow = pd.get_dummies(thir_X.signup_flow, prefix="signup_flow")
oh_affiliate_channel = pd.get_dummies(thir_X.affiliate_channel, prefix="affiliate_channel")
oh_affiliate_provider = pd.get_dummies(thir_X.affiliate_provider, prefix="affiliate_provider")
oh_first_affiliate_tracked = pd.get_dummies(thir_X.first_affiliate_tracked, prefix="first_affiliate_tracked")
oh_signup_app = pd.get_dummies(thir_X.signup_app, prefix="signup_app")
oh_first_device_type = pd.get_dummies(thir_X.first_device_type, prefix="first_device_type")
oh_first_browser = pd.get_dummies(thir_X.first_browser, prefix="first_browser")
thir_X.drop(['signup_method','language', 'signup_flow',
          'affiliate_channel', 
         'affiliate_provider', 'first_affiliate_tracked', 
         'signup_app', 'first_device_type', 'first_browser'],1,inplace=True)
thir_X.shape
thir_X = pd.concat([thir_X,oh_signup_method,oh_language,
                    oh_affiliate_channel,oh_affiliate_provider,
                    oh_first_affiliate_tracked,oh_first_browser],axis=1)
nm1 = NearMiss(ratio={'MALE':44942, 'FEMALE':44942},random_state=4, version =2)
Xthir_resample,Ythir_resample = nm1.fit_sample(thir_X,thir_Y)

df_xthir = pd.DataFrame(Xthir_resample)
df_ythir = pd.DataFrame(Ythir_resample,columns = ['gender'])
#df_ythir['gender'].value_counts()
df_other = pd.concat([df_xthir,df_ythir],axis=1)

#seperate features and samples
df_whole_Y = df_other['gender']
df_other.drop(['gender'],1,inplace=True)
df_whole_X = df_other
df_whole_X.head(3)
x_train, x_test, y_train, y_test = train_test_split(df_whole_X, df_whole_Y, test_size=0.3)

result_lable = ['MALE','FEMALE','OTHER']
clf = tree.DecisionTreeClassifier(criterion='entropy',min_samples_split=1000)
clf = clf.fit(x_train,y_train)


# fill the gender to all samples
all_samples = pd.read_csv('../../data/train_users_2.csv')
all_gender = clf.predict(x_test)
all_samples.replace('-unknown-', np.nan, inplace=True)

