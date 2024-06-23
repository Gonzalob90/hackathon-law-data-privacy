"""
main.py
1. Upload the notification letter
2. Generate advice
"""

import streamlit as st
from io import StringIO
from advisor import Adviser
from utils import read_pdf

adviser = Adviser()

st.set_page_config(layout="wide")
section = st.sidebar.selectbox("Section", ["Check Compensation"])
st.header("Data Privacy Adviser")


if section == "Check Compensation":
    st.subheader("1. Upload you notification letter")

    document = None
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf"])
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            document = read_pdf(uploaded_file)
        else:
            string_data = StringIO(uploaded_file.getvalue().decode("utf-8"))
            document = string_data.read()
        st.text(document)

    if document is not None:
        st.write("")
        st.subheader("2. Suggestion (not legal advice)")
        with st.spinner("Reviewing your document..."):
            advice = adviser.get_gdpr_checks(document)
        st.write(advice)