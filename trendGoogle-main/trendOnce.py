#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:09:39 2021

@ygoats
"""

from pytrends.request import TrendReq

from plotly import tools
import plotly.offline as py
import plotly.graph_objs as go

import pandas as pd
from datetime import datetime

import masterList

import telegram_send

from time import sleep

def checkParameters():
    checkList = masterList.checkList
    
    pointSystemList = []
    
    loudCoins = []
    quietCoins = []
    
    lenList = len(checkList)
    
    for ss in range(lenList):
        sleep(5)
        pointSystem = 0
        maTen1 = 0
        maTen2 = 0
        maTen3 = 0
        maTen4 = 0
        maTen5 = 0
        maTen6 = 0
        setA = 0
        setB = 0
        setC = 0
        setD = 0
        setE = 0
        
        group1 = []
        group2 = []
        group3 = []
        group4 = []
        group5 = []
        group6 = []
        
        # Login to Google. Only need to run this once, the rest of requests will use the same session.
        pytrend = TrendReq()
    
        #keyword = input('Type a keyword / phrase and press ENTER \n')
        keyword = checkList[ss]
    
        # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
        pytrend.build_payload(kw_list=[keyword],timeframe='now 7-d')
    
        # Interest Over Time
        print('Search Interest Over Time')
        print(str(keyword))
        iot_df = pytrend.interest_over_time()
    
        dataMain=iot_df.tail(160)
    
        #print(lastTwenty.iloc[19, 0]) 
        #print(lastTwenty.iloc[18, 0])
    
        for s in range(24):
            data1 = dataMain.iloc[158-s, 0]
            group1.append(data1)
            
        for sa in range(24):
            data2 = dataMain.iloc[134-sa, 0]
            group2.append(data2)
            
        for sb in range(24):
            data3 = dataMain.iloc[110-sb, 0]
            group3.append(data3)
            
        for sc in range(24):
            data4 = dataMain.iloc[86-sc, 0]
            group4.append(data4)
            
        for sd in range(24):
            data5 = dataMain.iloc[62-sd, 0]
            group5.append(data5)
            
        for se in range(24):
            data6 = dataMain.iloc[38-se, 0]
            group6.append(data6)
    
        maTen1 = round(sum(group1)/24,2)
        maTen2 = round(sum(group2)/24,2)
        maTen3 = round(sum(group3)/24,2)
        maTen4 = round(sum(group4)/24,2)
        maTen5 = round(sum(group5)/24,2)
        maTen6 = round(sum(group6)/24,2)
    
        #print(maTen1)
        #print(maTen2)
        #print(maTen3)
        #print(maTen4)
        #print(maTen5)
        #print(maTen6)
    
        setA = float(maTen1 - maTen2)
        setB = float(maTen2 - maTen3)
        setC = float(maTen3 - maTen4)
        setD = float(maTen4 - maTen5)
        setE = float(maTen5 - maTen6)
    
        pointSystem = round(setA + setB + setC + setD + setE,2)
        
        pointSystemList.append(pointSystem)
        
    print(pointSystemList)
    
    print('Checking Highest Interest Coins')
    for ss in range(10):
        index1 = 0
        index1 = pointSystemList.index(max(pointSystemList))
        print(str(index1))
        loudCoins.append(checkList[index1])
        checkList.remove(checkList[index1])
        pointSystemList.remove(pointSystemList[index1])
    
    print('Checking Lowest Interest Coins')    
    for sss in range(10):
        index2 = 0
        index2 = pointSystemList.index(min(pointSystemList))
        print(str(index2))
        quietCoins.append(checkList[index2])
        checkList.remove(checkList[index2])
        pointSystemList.remove(pointSystemList[index2])
        
    print(str(loudCoins))
    print(str(quietCoins))
    
    
    telegram_send.send(conf='user1.conf',messages=['Top Trending Crypto' + "\n" + str(loudCoins)])
        
    telegram_send.send(conf='user1.conf',messages=['Bottom Trending Crypto' + "\n" + str(quietCoins)])

checkParameters()


    


