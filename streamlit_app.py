import streamlit as st
import snowflake.connector
import pandas


st.title('Zena\'s Amazing Athleisure Catalog')
# connect to snowflake
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cnx = st.connection("snowflake")
my_cur = my_cnx.cursor()
# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
# put the dafta into a dataframe
df = pandas.DataFrame(my_catalog)
# temp write the dataframe to the page so I Can see what I am working with
# streamlit.write(df)
# put the first column into a list
color_list = df[0].values.tolist()
# print(color_list)

