#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 07:49:18 2017

@author: lixiaochi
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#load file
dfSessions = pd.read_csv('/Users/lixiaochi/Documents/study/uq/Semester5/DECO7380/Machine Learning Thesis/thesis/projects/airbnb_new_user_bookings/airBnB_destination/data/session_extract.csv')
dfTrainUsers = pd.read_csv('/Users/lixiaochi/Documents/study/uq/Semester5/DECO7380/Machine Learning Thesis/thesis/projects/airbnb_new_user_bookings/airBnB_destination/data/gd_data.csv')

dfSessions.set_index('user_id').join(dfTrainUsers.set_index('id'))
