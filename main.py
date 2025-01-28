import streamlit as st

st.title("Subpoena Tracker")
st.subheader("Log and track the issuance and compliance of subpoenas.")

# Adding basic subpoena information
st.write("### Subpoena Data")
col1, col2, col3 = st.columns(3)
subpoena_number = col1.text_input("Enter Subpoena Number")
subpoena_jurisdiction = col2.text_input("Enter Issuing Jurisdiction")
subpoena_due_date = col3.date_input("Enter Subpoena Due Date", format="MM/DD/YYYY")