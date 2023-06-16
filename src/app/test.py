import streamlit as st
import pandas as pd
import numpy as np
from .. src.main import extract_info_from_json

st.title('InvoiceDataMiner')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = sm.extract_info_from_pdf(uploaded_file)
    st.write(bytes_data)