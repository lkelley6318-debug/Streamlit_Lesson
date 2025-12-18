import streamlit as st
import numpy as np

with st.chat_message("assistant"):
    st.write("Hello Human!")
    st.bar_char(np.random.randn(30,3))


