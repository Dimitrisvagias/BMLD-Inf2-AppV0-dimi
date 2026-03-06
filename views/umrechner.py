import streamlit as st

st.title(" Gramm zu Newton Umrechner")
st.divider()
st.caption ("Gib eine Masse in Gramm ein oder benutze den Slider")
gramm = st.slider("Slider:", min_value=0.0, max_value=10000.0, step=0.1)

gramm = st.number_input("Oder Gramm eingeben:", min_value=0.0, max_value=10000.0, value=gramm, step=0.1)

newton = gramm * 0.00980665

st.divider ()


col1, col2 = st.columns(2)

with col1:
    st.metric(label="Gramm", value=f"{gramm:.1f} g")

with col2:
    st.metric(label="Newton", value=f"{newton:.4f} N")

st.divider()

