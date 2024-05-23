import streamlit as st
import snowflake.connector

st.title("""Zena's Athleisure Catalog""")

# Initialize connection.
conn = st.connection("snowflake")
