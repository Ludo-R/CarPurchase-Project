#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:07:33 2020

@author: randon
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

import pymysql
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:sqlpwd@localhost/carpurchase")

sql = "SELECT * FROM cardata"

df = pd.read_sql(sql, engine)

import matplotlib.pyplot as plt
from sklearn import linear_model

x = df["Present_Price"].values
x2 = df["Year"].values
y = df["Selling_Price"].values

line = linear_model.LinearRegression(fit_intercept = True)
line2 = linear_model.LinearRegression(fit_intercept= True)

x = x.reshape(-1,1)
x2 = x2.reshape(-1,1)

line.fit(x, y)
line2.fit(x2, y)

pred = line.predict(x)
pred2 = line2.predict(x2)

fig=go.Figure()
fig.add_trace(go.Scatter(name='Values', x=df["Present_Price"], y=df["Selling_Price"], mode='markers'))
fig.add_trace(go.Scatter(name='Regression', x=df["Present_Price"], y=pred, mode='lines'))

fig2=go.Figure()
fig2.add_trace(go.Scatter(name='Values', x=df["Year"], y=df["Selling_Price"], mode='markers'))
fig2.add_trace(go.Scatter(name='Regression', x=df["Year"], y=pred2, mode='lines'))

app.layout = html.Div(children=[
    html.H1(children='Cardheko Dashboard'),
    
    html.H1(children='Première Regression Lineaire :'),

    html.Div(children='''
        Voici un modèle de regression linéaire qui utilise les données Present_Price et Seller_Price qui sont les varibles qui ont le plus de corrélation
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
        ),

    html.Div(children='Le R2 de ce modèle est de : %s' % line.score(x,y)),
    
    html.H1(children='Deuxieme Regression Lineaire :'),
    
    html.Div(children='Une deuxième regression basé sur Year & Seller_Price, la corrélation entre ces deux colonnes est plus basse.'),
    
    dcc.Graph(
    id='example-graph2',
    figure=fig2
    ),
    
    html.Div(children='Le R2 de ce modèle est de : %s' % line2.score(x2,y)),
])
             

if __name__ == '__main__':
    app.run_server(debug=True)