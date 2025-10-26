# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 20:52:13 2025

@author: VENKATKARTHIKEYAN.K
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/VENKATKARTHIKEYAN.K/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav'))

heart_disease_model = pickle.load(open('C:/Users/VENKATKARTHIKEYAN.K/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav'))

parkinsons_model = pickle.load(open('C:/Users/VENKATKARTHIKEYAN.K/Desktop/Multiple Disease Prediction System/saved models/parkinson_model.sav'))



with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction']. 
                           default_index = 0)
    
    
    