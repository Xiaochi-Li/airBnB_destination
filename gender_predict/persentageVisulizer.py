#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:14:41 2017

@author: lixiaochi
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('../data/train_users_2.csv')

print df.shape


# Pie chart shows the persentage missing value of gender
var = df.groupby(['gender']).size()
lable = var.index
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('gender persentage')

# Pie chart shows the persentage missing value of age
missing_age_count = df.age.isnull().sum()
record_age_count = df.age.shape[0] - missing_age_count
var = [missing_age_count, record_age_count]
lable = ['missing age', 'record age']
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('Age missing')

# Pie chart shows the persentage missing value of signup_method
var = df.groupby(['signup_method']).size()
lable = var.index
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('signup_method persentage')

# Pie chart shows the persentage missing value of signup_flow
var = df.groupby(['signup_flow']).size()
lable = var.index
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('signup_flow persentage')

# Pie chart shows the persentage missing value of language
var = df.groupby(['language']).size()
lable = var.index
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('language persentage')

# Pie chart shows the persentage missing value of affiliate_channel
var = df.groupby(['affiliate_channel']).size()
lable = var.index
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('affiliate_channel persentage')

# Pie chart shows the persentage missing value of affiliate_provider
var = df.groupby(['affiliate_provider']).size()
lable = var.index
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('affiliate_provider persentage')


# Pie chart shows the persentage missing value of first_affiliate_tracked
var = df.fillna(value="missing data").groupby(['first_affiliate_tracked']).size()
print var
lable = var.index
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('first_affiliate_tracked persentage')

# Pie chart shows the persentage missing value of signup_app
var = df.fillna(value="missing data").groupby(['signup_app']).size()
print var
lable = var.index
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('signup_app persentage')

# Pie chart shows the persentage missing value of first_device_type
var = df.fillna(value="missing data").groupby(['first_device_type']).size()
print var
lable = var.index
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('first_device_type persentage')

# Pie chart shows the persentage missing value of first_browser
var = df.fillna(value="missing data").groupby(['first_browser']).size()
print var
lable = var.index
fig1, ax1 = plt.subplots()
ax1.pie(var,labels = lable,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('first_browser persentage')