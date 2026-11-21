import streamlit as st

st.title("Bharat Software Solutions")
col1,col2 = st.columns(2)

with col1:
    st.image("bss_logo.jpg", width=200)
with col2:
    st.write("We provide innovative software solutions for your business needs.")

st.header("Our Courses")
st.subheader("Data Science")
st.subheader("Data Analytics")
st.subheader("Data Engineering")


