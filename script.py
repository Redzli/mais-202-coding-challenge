#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 00:26:50 2018

@author: lizhengyuan
"""

# How to run this script:
# By clicking the 'run' button, a graph will be generated



import csv
import matplotlib.pyplot as plt

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')   #open data.csv
    dic = {}
    
    for row in csv_reader:
        keyword=row[16]         #'purpose'is on the 17th position of first row
        if keyword == "purpose":
            continue
        if dic.get(keyword) is None:
            int_rate = []   #create a list to store the contents of purposes
            dic[keyword]=int_rate
            int_rate.append(float(row[5]))  #use the list to store each purpose's interest rate
        else:
            dic[keyword].append(float(row[5]))  
    
    for key in dic:
        avg_rate=sum(dic[key])/len(dic[key])    #calculate average interest rate
        dic[key]=avg_rate
        print(key, dic[key])
    
        
    names = ['credit_card','car','small_business','other','wedding','debt_consolidation','home_improvement',
             'major_purchase','medical','moving','vacation','house']  #label the x-axis                   
    
    y=dic.values()   #values are plotted on y-axis
    
    plt.bar(names,y, width=0.7, color=['yellow','blue','green','red','orange','purple','grey','brown'])
    
    plt.xlabel('purpose')
    
    plt.ylabel('mean(int_rate)')
    
    plt.show()
