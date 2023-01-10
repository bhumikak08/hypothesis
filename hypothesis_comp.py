#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import pandas as pd
import numpy as np

import scipy.stats as stats
from statsmodels.stats import weightstats as stests
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("# Social media data analysis")
def func(n):
  def truthtable (n):
    if n < 1:
      return [[]]
    subtable = truthtable(n-1)
    return [ row + [v] for row in subtable for v in [0,1] ]
  bits=truthtable(n)  
  ANDtable = []
  ORtable = []
  for i in range(len(bits)):
    AND = 1
    for j in range(n):
        AND &= bits[i][j]
#         print(AND,"-",bits[i][j])
    ANDtable.append(AND)
  length = len(bits)
  for i in range(length):
    OR = 0
    for j in range(n):
      OR |= bits[i][j]
#         print(i)
    ORtable.append(OR)
    op=[]
  len(ORtable)
  for i in range(length):
    op.append(bits[i])
    op.append(ORtable[i])
  return op  
z=func(2)
st.write(z)  

