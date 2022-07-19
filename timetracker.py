# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:29:26 2022

@author: Prasuna
"""

import pandas as pd
import streamlit as st

p_names = ["<select>", "Mohan", "Mani", "Raju", "Ranjith", "Vamshi", "Asif", "Sudha", "Ravi"]
p_types = ["<select>", "BI_Dashboard", "Advanced_Analytics", "EDA", "Data_Architect", "Ad-hoc"]
p_pnames = ["<select>","TD", "MRM", "Audit", "Covid_dashboard", "Projections", "HitRate", "Mixed_Models", "Provider_Escalation"]

df = pd.read_csv("C:\\Users\\Prasuna\\tracker.csv")
st.title("Time Sheet Tracker")

options_form = st.form("options_form", clear_on_submit= True)

user_name = options_form.selectbox("Select your name: ", p_names)
project_type = options_form.selectbox("Select the project type: ", p_types)
project_name = options_form.selectbox("Select the project name: ", p_pnames)

date, p_hours = options_form.columns(2)
date_worked = date.date_input("Date")
hrs_worked = p_hours.text_input("No of hrs worked")

project_desc = options_form.text_area("Enter the work description here")

#d_project, s1 = st.columns(2)
#d_project.text_area("Enter the work description here")

add_data = options_form.form_submit_button()

if add_data:
    new_data = {"Name" : user_name, "ProjectType" : project_type, "ProjectName" : project_name, "Date" :date_worked, "No_of_hrs_worked" : hrs_worked, "Description_of_work" : project_desc}
    df = df.append(new_data, ignore_index = True)
    df.to_csv("C:\\Users\\Prasuna\\tracker.csv", index = False)
    