import streamlit as st

st.title("Gramm zu Newton Umrechner")

gramm = st.number_input("Gramm eingeben:", min_value=0.0, step=0.1)

newton = gramm * 0.00980665

st.write(f"{gramm} g = **{newton:.4f} N**")
