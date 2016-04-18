# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:57:55 2016

@author: warriorzhai
"""

import tushare as ts
import os
import pymongo


def df_todict(df):
    d={}
    for colname in df:
        d[colname]=df[colname].tolist()
    return d

data=ts.get_gem_classified().ix[:5]
data=df_todict(data)
client = pymongo.MongoClient('mongodb://admin:admin@ds011281.mlab.com:11281/stkdb')
db = client.stkdb
collection = db.test
collection.insert_one(data)

