# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:42:34 2017

@author: marine
"""

import numpy as np
import os

filelist = os.listdir('./')
psd_histo_list = []
for i in filelist:
    if 'psd_histo' in i:
        psd_histo_list.append(i)
        
for i in range(len(psd_histo_list)):
    filename = psd_histo_list[i]
    fn = open(filename, 'r').readlines()
    coordinates=fn[11:1011]
    diameter=[]
    j=0
    while j < 998:
        x1=float(coordinates[j].split('\t')[0])
        y1=float(coordinates[j].split('\t')[1])
        x2=float(coordinates[j+1].split('\t')[0])
        y2=float(coordinates[j+1].split('\t')[1])
        x3=float(coordinates[j+2].split('\t')[0])
        y3=float(coordinates[j+2].split('\t')[1])
        
        slope1=(y2-y1)/(x2-x1)
        slope2=(y3-y2)/(x3-x2)
        
        if slope1*slope2 < 0:
            diameter.append(x2)
        
        j=j+1
        
    for j in range(len(diameter)):
        diameter[j]=np.round(diameter[j])

    diameter=list(set(diameter))
    
    output=open('output.dat','a')
    output.write(filename+'\t')
    for j in range(len(diameter)):
        output.write(str(diameter[j])+'\t')
    output.write('\n')
    output.close()
