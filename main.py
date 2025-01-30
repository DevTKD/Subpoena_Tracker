import streamlit as st

st.title("Subpoena Tracker")
st.subheader("Log and track the issuance and compliance of subpoenas.")

# Adding basic subpoena information
st.write("### Basic Subpoena Details")
col1, col2, col3 = st.columns(3)
subpoena_ID = col1.text_input("Enter Subpoena Number")
case_name = col2.text_input("Enter Case Name/Number")
issued_date = col3.date_input("Enter Date Issued", format="MM/DD/YYYY")

# Containing next set of basic data
col4, col5 = st.columns(2)
response_deadline = col4.date_input("Enter Response Deadline", format="MM/DD/YYYY")
type_of_subpoena = col5.selectbox("Select Subpoena Type", ["Deposition", "Production of documents", "Appearance"])

# Party Information
col6, col7, col8 = st.columns(3)
issuing_party = col6.text_input("Enter Issuing Party")
issuing_party_contact = col7.text_input("Enter Contact Person")
contact_email = col8 = col8.text_input("Enter Contact Email")

# Compliance Tracking
col9, col10, col11 = st.columns(3)
compliance_status = col9.selectbox("Select Status", ["Pending", "With Data Team", "Compiled", "Responded"])
# Need to add conditional for if compliance_status == responded then response_date must be entered.
response_date = col10.date_input("Enter Response Date", format="MM/DD/YYYY")
notes_on_compliance = col11.text_area("Enter Notes")
