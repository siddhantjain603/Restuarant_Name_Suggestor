import streamlit as st
import langchain_helper

st.title("Restuarant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian","Italian","Chinese","Mexican","Spanish","Arabic","American"))

button_clicked = st.sidebar.button("Generate Restaurant Name")

if button_clicked:

    response = langchain_helper.generate_restuarant_name_and_items(cuisine=cuisine)

    st.header(response['restuarant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')

    st.write("**Menu Items**")
    for item in menu_items:
        st.write(item)



