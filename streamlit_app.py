import streamlit as st
import snowflake.connector

streamlit.title("""Zena's Athleisure Catalog""")

# Initialize connection.
conn = st.connection("snowflake")
