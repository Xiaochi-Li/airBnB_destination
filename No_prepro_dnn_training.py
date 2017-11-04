#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 08:31:19 2017

@author: lixiaochi
"""

import pandas as pd
import seaborn as sn
import numpy as np

import keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.regularizers import l2


from sklearn.preprocessing import Imputer
from sklearn.utils import shuffle
from sklearn import tree
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

df = pd.read_csv('./data/sesion_joind_gender_age.csv')

df = df.fillna(method="backfill")
df = df.fillna(method="ffill")

Y = df.country_destination
df.drop(["country_destination","id","date_account_created","timestamp_first_active"], 1, inplace=True)

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
df.drop(['gender', 'signup_method',
         'language', 'affiliate_channel', 
         'affiliate_provider', 'first_affiliate_tracked', 
         'signup_app', 'first_device_type', 'first_browser'],1,inplace=True)
# from the traning set
x_train = pd.concat([df,oh_gender, oh_language, 
                oh_signup_method, oh_affiliate_channel, 
                oh_affiliate_provider,
                oh_first_affiliate_tracked, oh_signup_app,
                oh_first_device_type, oh_first_browser],axis=1)
    

x_train["age"] = x_train["age"]/2014
x_train["signup_flow"] = x_train["signup_flow"]/25


y = pd.get_dummies(Y, prefix="countary")
print y.head(3)
model = Sequential()

# 1st Layer - Add an input layer of 132 nodes with the same input shape as
# the training samples in X
model.add(Dense(2333, input_dim = 449 ,W_regularizer = l2(.01)))
model.add(Activation('sigmoid'))
model.add(keras.layers.Dropout(0.50))


model.add(Dense(777,W_regularizer = l2(.01)))
model.add(Activation('sigmoid'))
model.add(keras.layers.Dropout(0.5))

model.add(Dense(259,W_regularizer = l2(.01)))
model.add(Activation('sigmoid'))
model.add(keras.layers.Dropout(0.5))

model.add(Dense(86,W_regularizer = l2(.01)))
model.add(Activation('sigmoid'))
model.add(keras.layers.Dropout(0.5))

model.add(Dense(12, activation = 'softmax'))
model.compile(loss="categorical_crossentropy", optimizer="RMSProp", metrics = ["accuracy"])
# Uncomment this line to print the model architecture
#callbacks = [
#   keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0.001, patience=0, verbose=2, mode='auto')
#]

#convert datafram to np-array
x_train=np.array(x_train)


y_new=np.array(y)

x_nw_train, x_nw_test, y_nw_train, y_nw_test = train_test_split(x_train,y_new, test_size=0.3)
model.fit(x_nw_train, y_nw_train, validation_data=(x_nw_test,y_nw_test),epochs = 32, batch_size=200, verbose=2)

#keras.utils.plot_model(model, to_file='model.png', show_shapes=False, show_layer_names=True, rankdir='TB')

y_nw_predict = model.predict(x_nw_test)


df_prediction = pd.DataFrame(y_nw_predict)
df_y_nw_test = pd.DataFrame(y_nw_test)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('nn_predict_se_age_gender_prob.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df_prediction.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('nn_real_se_age_gender_realts.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df_y_nw_test.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()