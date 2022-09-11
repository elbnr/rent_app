import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

st.title('EDA on House rent prices')
st.markdown('Created by **_Abhishek_Sharma**.')
df = pd.read_csv("House_Rent_Dataset.csv")
st.dataframe(df) 

a =df.sort_values(by = "Size",ascending = False)
fig = px.bar(data_frame = a, y='City', x='Size',template = "simple_white",color = "Bathroom",color_discrete_sequence = ["white"],color_continuous_scale = px.colors.sequential.Burg,barmode ="overlay", title = "City x areas sqm")
fig.update_xaxes(tickangle = 90)#change the angle of x axis labels
fig.update_yaxes(tickangle = 0)#change the angle of y axis labels
fig.update_coloraxes(showscale=False)# Hide scale
fig.update_layout(title = {"text":"City_price_area_square meter","font":{"size":40}},title_x = 0.12,title_font_family = "Times New Roman",title_font_color = "white")
fig.update_layout(font_family = "classic-roman",font_color = "black",yaxis_title = {"text":"City","font":{"size":20}},xaxis_title = {"text":"Size","font":{"size":20}})
fig.update_xaxes(title_font_color ="red")
fig.update_yaxes(title_font_color ="green")
fig.add_annotation( x =4000, y="6",text = "Hyderabad and chennai are on the top", showarrow = False ,font = dict(family = "courier New, monospace",size =16,color="white"))

fig2 = px.bar(df, x="BHK", y="Rent", color="City",barmode ="overlay")
fig2.update_layout(title = {"text":"BHK wise rent","font":{"size":40}},title_x = 0.12,title_font_family = "Times New Roman",title_font_color = "Green")
fig2.add_annotation( x = 5, y="3600000",text = "Mumbai and banglore have high rent", showarrow = False ,font = dict(family = "courier New, monospace",size =16,color="white"))

fig3 = px.histogram(df, x="Tenant Preferred",color_discrete_sequence=['indianred'] )
fig3.add_annotation( x = 1.2, y="825",text = "People prefer more bachlors", showarrow = True ,font = dict(family = "courier New, monospace",size =16,color="white"))
fig3.update_layout(title = {"text":"Prerence of owner","font":{"size":40}},title_x = 0.12,title_font_family = "Times New Roman",title_font_color = "grey")

visualization = st.radio(
     "What you want to see",
     ('City', 'Preference', 'Rent'))

if visualization == 'City':
     st.plotly_chart(fig, use_container_width=True)
elif visualization == "Preference":
     st.plotly_chart(fig3)
else:
     st.plotly_chart(fig2, use_container_width=True)
