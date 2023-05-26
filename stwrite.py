# -*- coding: utf-8 -*-
"""
Created on Thu May 25 18:36:58 2023

@author: dejol
"""

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

st.write('Hello *world* :sunglasses:')

df = pd.DataFrame({
    'London': ['puppy','kitten','ice cream'],
    'Jen': ['Tiger','daisy','waggles']})

st.write(df)

x = [i*10 for i in range(10)]
y = [i*20 for i in range(10)]

df2 = pd.DataFrame({
    'Dan': x,
    'Jen': y})


st.write(df2)