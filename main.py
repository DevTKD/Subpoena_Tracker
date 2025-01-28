import streamlit as st

st.title("Subpoena Tracker")
st.subheader("Log and track the issuance and compliance of subpoenas.")

# Adding basic subpoena information
st.write("### Basic Subpoena Details")
col1, col2, col3 = st.columns(3)
subpoena_ID = col1.text_input("Enter Subpoena Number")
case_name = col2. text_input("Enter Case Name/Number")
issued_date = col3.date_input("Enter Date Issued", format="MM/DD/YYYY")

#Contuning next set of basic data
col4, col5 = st.columns(2)
response_deadline = col4.date_input("Enter Response Deadline", format="MM/DD/YYYY")
type_of_subpoena = col5.text_input("Enter Subpoena Type")
