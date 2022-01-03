#!/usr/bin/env python
# coding: utf-8

# In[ ]:






import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
import scipy.stats as stats
from statsmodels.stats import weightstats as stests
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("# Social media data analysis")

uploaded_file = st.file_uploader("Choose a file")
def chi(a,b,c,d):
    from scipy.stats import chi2_contingency
    import pandas as pd

    data = [a,b]
    stat, p, dof, expected = chi2_contingency(data)

    # interpret p-value
    alpha = 0.05
    st.write("p value is " + str(p))
    if p <= alpha:
        st.write('reject H0:'+c)
        st.write("H1:"+d)
    else:
        st.write('accept H0:'+c)

def ot_test():
    ages = np.genfromtxt("ages.csv")

    df=pd.DataFrame(ages)
    ages_mean = np.mean(ages)
    tset, pval = ttest_1samp(ages, 36)
    if pval < 0.05:    # alpha value is 0.05 or 5%
       st.write(" we are rejecting null hypothesis")
    else:
      st.write("we are accepting null hypothesis")
def z_test():

    ztest ,pval = stests.ztest(df, x2=None, value=156)
    st.write(float(pval))
    if pval<0.05:
        st.write("reject null hypothesis")
    else:
        st.write("accept null hypothesis")
def tttest(group1,group2):

    tset, pval=stats.ttest_ind(a=group1, b=group2, equal_var=True)
    if pval < 0.05:    # alpha value is 0.05 or 5%
       st.write(" we are rejecting null hypothesis")
    else:
      st.write("we are accepting null hypothesis")

if uploaded_file is not None:
    social_career_data = pd.read_csv(uploaded_file)
    st.write(social_career_data)
    st.write("")
    st.write("")
    # creating contigency table for chi square test

    cont_table  = pd.DataFrame(index=['UseSM','NoUseSM'])
    UseSMlist= (social_career_data['AcqJobthruSM'].value_counts().to_list()[1:])
    NoUseSMlist = (social_career_data['AcqJobwithoutSM'].value_counts().to_list()[1:])
    cont_table['Y'] = UseSMlist
    cont_table['N'] = NoUseSMlist
    # defining hypothesis
    Alt="Social media doesnt help in career growth"
    Null=" Social media helps in career growth"

    chi(cont_table['Y'],cont_table['N'],Null,Alt)
   

