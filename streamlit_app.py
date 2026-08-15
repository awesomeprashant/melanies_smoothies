# Import python packages
import streamlit as st
import os
from snowflake.snowpark.functions import col
import requests  

# title = st.text_input('Movie Title','Life of Brian')
# st.write("Movie Title", title)

name_on_order = st.text_input('Name on Order')
st.write("Name of the smothie will be:", name_on_order)

# Write directly to the app
st.title(f"Customize You'r Smothies")

# Create a database connection to Snowflake
conn = st.connection("snowflake", ttl=os.getenv("SNOWFLAKE_CONNECTION_TTL"))
session = conn.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))
# st.dataframe(data=my_dataframe, use_container_width=True)


ingredients_list = st.multiselect("Choose up to 5",my_dataframe,max_selections=5)

if ingredients_list:
    # st.write(ingredients_list)
    # st.text(ingredients_list)
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        st.subheader(fruit_chosen + ' Nutrition Information: ')
        smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/"+ fruit_chosen)  
        st.text(smoothiefroot_response) 
        #sf_df  = st.dataframe(data=smoothiefroot_response.json, use_container_width=True)
        

    
    # st.write(ingredients_string)        

    # my_insert_stmt = """ insert into smoothies.public.orders(ingredients,NAME_ON_ORDER)
    #                    values ('""" + ingredients_string + """', 
    #                    '""" + name_on_order + """')"""
    
    # st.write(my_insert_stmt)

    # if ingredients_string:
    #    session.sql(my_insert_stmt).collect()
    #    st.success('Your Smoothie is ordered!', icon="✅")
