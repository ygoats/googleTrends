#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:09:39 2021

@ygoats
"""

import trend
import telegram_send
from datetime import datetime
import masterList
from time import sleep

trendChecking = True

def Main():
    
    while trendChecking == True:
        
        try:
            now = datetime.now()
            t = now.strftime("%H:%M:%S")
            
            sleep(5)
            
            if t >= '05:00:00' and t <= '05:01:00':
                try:
                    trend.checkParameters()
                except Exception as e:
                    print(e)
                    continue
                
        except Exception as e:
            print(e)
            continue
            
if __name__ == '__main__':
    Main()
