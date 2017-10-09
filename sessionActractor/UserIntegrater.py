#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 07:59:15 2017

@author: lixiaochi
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class UserIntegrater:
    username = ""
    action = ""
    action_type =""
    device_type = ""
    secs_elapsed = ""
    userSessionSummary = pd.DataFrame()
    
    def __init__(self, userDataFram):
        print userDataFram.shape()
    
    def rowIterater(self, userDataFram):
        for row in userDataFram.iterrows():
            print row

    