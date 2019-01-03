#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 00:26:50 2018

@author: lizhengyuan
"""

# This file has to be run in the same directory with data.csv
# How to run this script:
# type 'python script.py' in terminal


#from prettytable import PrettyTable
import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd

#table=PrettyTable()

#table.field_names=["purpose","avg_rate"]

#def dataframe(cols, ind):
#    """Quickly make a DataFrame"""
#    data = {c: [str(c) + str(i) for i in ind]
#            for c in cols}
#    return pd.DataFrame(data, ind)

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

    
    graph_list=dic.keys() 
    graph_list.sort()   # alphabetically sort the contents
    int_list=[]
    text=[]
    for graph in graph_list:
        int_list.append(dic[graph])
        text.append([graph,'%.3f'%dic[graph]])

    fig = plt.figure(figsize=(23,6))    #create the table
    ax = plt.subplot2grid((7,14), (0,0), colspan=3)
    col_label=('purpose','avg_rate')    #specify the headers of table
    table=ax.table(cellText=text,colLabels=col_label,loc='upper right')
    ax.axis("off")

    plt.subplot2grid((5,12), (0,4),colspan=9,rowspan=3)
    left = np.arange(len(dic))
    height = int_list   #make the avg_int into rows

    color_list=['red','yellow','blue','green','brown','pink','lightblue',
    'purple']  #specify the colours
    plt.bar(left,height,color=color_list,align='center')

    #plot the table and graph:
    plt.xlabel('purpose')
    plt.ylabel('mean(int_rate)')
    plt.xticks(left,graph_list,fontsize=7)
    plt.yticks(np.arange(0, 20, 2.5),fontsize=6)

    plt.show()






