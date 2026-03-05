import streamlit as st
st.title("Klick-Zähler")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Drück mich"):
    st.session_state.count += 1

st.write(f"Der Knopf wurde {st.session_state.count} mal gedrückt.") 
