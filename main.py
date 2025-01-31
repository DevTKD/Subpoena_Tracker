import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f0f0;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and subtitle
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Subpoena Tracker</h1>", unsafe_allow_html=True)
st.subheader("Log and track the issuance and compliance of subpoenas")

# Adding basic subpoena information
st.write("### Subpoena Details")
col1, col2, col3 = st.columns(3)
judicial_branch = col1.selectbox("Select a judicial branch", ["Federal", "State"])
jurisdiction = col2.text_input("Enter the court jurisdiction")
court_information = col3.text_input("Issuing Court Name & Location")

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

col4, col5, col6 = st.columns(3)
subpoena_id = col4.text_input("Enter Subpoena Number")
case_name = col5.text_input("Enter Case Name/Number")
issued_date = col6.date_input("Enter Date Issued")

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

# Containing next set of basic data
col7, col8 = st.columns(2)
response_deadline = col7.date_input("Enter Response Deadline")
type_of_subpoena = col8.selectbox("Select Subpoena Type", ["Deposition", "Production of Documents", "Appearance"])

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

# Party Information
with st.expander("Party Information"):
    col9, col10, col11 = st.columns(3)
    issuing_party = col9.text_input("Enter Issuing Party")
    issuing_party_contact = col10.text_input("Enter Contact Person")
    contact_email = col11.text_input("Enter Contact Email")

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

# Compliance Tracking
with st.expander("Compliance Tracking"):
    col12, col13 = st.columns(2)
    compliance_status = col12.selectbox("Select Status", ["Pending", "With Data Team", "Compiled", "Responded"])
    response_date = col13.date_input("Enter Response Date")

    col14, = st.columns(1)
    notes_on_compliance = col14.text_area("Enter Notes", max_chars=500)

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

# Submit button with custom CSS
middle, = st.columns(1)
submit_data_button = st.button("Submit Data")