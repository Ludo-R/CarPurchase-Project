#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:31:04 2020

@author: randon
"""
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import time

engine = create_engine("mysql+pymysql://root:sqlpwd@localhost/carpurchase")

def chargement(link, table):

    df = pd.read_csv(link)
    df.to_sql(table, con = engine, if_exists='append', index = False)
    return print("done")

chargement('../CarPurchase-Project/dataset/carData.csv', 'cardata') 
