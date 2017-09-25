 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 11:27:58 2017

@author: lixiaochi
"""
import pandas as pd
import stringEncoder
import seaborn as sn

from sklearn.preprocessing import Imputer
from sklearn.utils import shuffle
from sklearn import tree
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

#an training mtrix contain all newly registered airbnb users.
df = pd.read_csv('../data/train_users_2.csv')
#a datafram stores randomly reordered data from musiclist dataframe
df = shuffle(df)
df.drop(["id"], 1, inplace=True)

des_country = df.country_destination

result_lable =[]
for data in des_country:
    if data not in result_lable:
        result_lable.append(data)
        

# one-hot-encode all the categorical data:
# gender signup_method language affiliate_channel 
# affiliate_provider first_affiliate_tracked signup_app	
# first_device_type first_browser	country_destination
oh_gender = pd.get_dummies(df.gender, prefix="gender")
oh_language = pd.get_dummies(df.language, prefix="language")
oh_signup_method = pd.get_dummies(df.signup_method, prefix="signup_method")
oh_affiliate_channel = pd.get_dummies(df.affiliate_channel, prefix="affiliate_channel")
oh_affiliate_provider = pd.get_dummies(df.affiliate_provider, prefix="affiliate_provider")
oh_first_affiliate_tracked = pd.get_dummies(df.first_affiliate_tracked, prefix="first_affiliate_tracked")
oh_signup_app = pd.get_dummies(df.signup_app, prefix="signup_app")
oh_first_device_type = pd.get_dummies(df.first_device_type, prefix="first_device_type")
oh_first_browser = pd.get_dummies(df.first_browser, prefix="first_browser")

#dropped date_account_created date_first_booking add back later
df.drop(['date_account_created','gender', 'signup_method', 'date_first_booking',
         'language', 'affiliate_channel', 
         'affiliate_provider', 'first_affiliate_tracked', 
         'signup_app', 'first_device_type', 'first_browser','country_destination'],1,inplace=True)
# from the traning set
df = pd.concat([df,oh_gender, oh_language, 
                oh_signup_method, oh_affiliate_channel, 
                oh_affiliate_provider,
                oh_first_affiliate_tracked, oh_signup_app,
                oh_first_device_type, oh_first_browser],axis=1)

    # fill all NaN data with 0, redo after
df = df.fillna("0")

#seperate data.
x_train, x_test, y_train, y_test = train_test_split(df, des_country, test_size=0.3)

#music list decition tree classifier
clf = tree.DecisionTreeClassifier(criterion='entropy',min_samples_split=60)
clf = clf.fit(x_train,y_train)
#make prediction
y_predict = clf.predict(x_test)
#calulate overall Scoring .
precision, recall, fscore, support = score(y_test, y_predict,labels=result_lable)
print('precision: {}'.format(precision))
print precision_score(y_test, y_predict, average='weighted') 
print accuracy_score(y_test, y_predict)


#generate confusion matrix
cnf_matrix = confusion_matrix(y_test, y_predict, labels = result_lable)
cnf_matrix = pd.DataFrame(cnf_matrix, index = [i for i in result_lable],
                          columns = [i for i in result_lable])
# Plot non-normalized confusion matrix
sn.heatmap(cnf_matrix, annot= True, cmap="YlGnBu",fmt="d")