import streamlit as st 
import pandas as pd
import joblib
import warnings
import os

warnings.filterwarnings('ignore')
st.set_page_config(page_title='Simple Linear Regression',page_icon='🎯')
model=joblib.load('mod_Lin_Reg')

html_temp = """
		<div style="background-color:#324324;padding:8px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Simple Linear Regression </h1>
        <h4 style="color:white;text-align:center;"> (Student Marks based on Study Hour Predictions..) </h4>
		</div>
		"""

st.html(html_temp)

name=st.text_input('Enter Student Name : ')
std=st.text_input('Enter The Subject Name : ')
hou=st.slider('Select The Study Hours (1-12):',1,12)
ho=hou

if st.button('Predict'):
    prd=model.predict([[int(ho)]])
    p=prd
    r=p.round()
    st.sidebar.success(f'Hello {name},You can Score {r} Marks in {std} Subject...🎯')
    st.balloons()


   
    st.sidebar.link_button('About-Me','https://www.linkedin.com/in/muruga-perumal-iyadurai-7693592a7/')
                




