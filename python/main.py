# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:05:40 2023

@author: David
"""

from asammdf import MDF
 
f = r"Graphics1.mdf"
mdf = MDF(f)
signal = mdf.get('AccelRawZ')
data = signal.samples
timestamps = signal.timestamps