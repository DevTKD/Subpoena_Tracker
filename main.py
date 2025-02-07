import streamlit as st
import pandas as pd
import os

# Function to save data to CSV
def save_data(data, filename='subpoena_data.csv'):
    if os.path.exists(filename):
        existing_data = pd.read_csv(filename)
        data = pd.concat([existing_data, data], ignore_index=True)
    data.to_csv(filename, index=False)

# Function to load data from CSV
def load_data(filename='subpoena_data.csv'):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return pd.DataFrame(columns=[
            'Judicial Branch', 'Jurisdiction', 'Court Information', 'Subpoena ID',
            'Case Name', 'Issued Date', 'Response Deadline', 'Type of Subpoena',
            'Issuing Party', 'Issuing Party Contact', 'Contact Email',
            'Compliance Status', 'Response Date', 'Notes on Compliance'
        ])

# Initialize session state variables with valid default values
if 'judicial_branch' not in st.session_state:
    st.session_state['judicial_branch'] = "Federal"
if 'jurisdiction' not in st.session_state:
    st.session_state['jurisdiction'] = ""
if 'court_information' not in st.session_state:
    st.session_state['court_information'] = ""
if 'subpoena_id' not in st.session_state:
    st.session_state['subpoena_id'] = ""
if 'case_name' not in st.session_state:
    st.session_state['case_name'] = ""
if 'issued_date' not in st.session_state:
    st.session_state['issued_date'] = None
if 'response_deadline' not in st.session_state:
    st.session_state['response_deadline'] = None
if 'type_of_subpoena' not in st.session_state:
    st.session_state['type_of_subpoena'] = "Deposition"
if 'issuing_party' not in st.session_state:
    st.session_state['issuing_party'] = ""
if 'issuing_party_contact' not in st.session_state:
    st.session_state['issuing_party_contact'] = ""
if 'contact_email' not in st.session_state:
    st.session_state['contact_email'] = ""
if 'compliance_status' not in st.session_state:
    st.session_state['compliance_status'] = "Pending"
if 'response_date' not in st.session_state:
    st.session_state['response_date'] = None
if 'notes_on_compliance' not in st.session_state:
    st.session_state['notes_on_compliance'] = ""

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

# Load existing data
submitted_data = load_data()


# Adding basic subpoena information
st.write("### Subpoena Details")
col1, col2, col3 = st.columns(3)
judicial_branch = col1.selectbox("Select a judicial branch", ["Federal", "State"], key='judicial_branch')
jurisdiction = col2.text_input("Enter the court jurisdiction", key='jurisdiction')
court_information = col3.text_input("Issuing Court Name & Location", key='court_information')

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

col4, col5, col6 = st.columns(3)
subpoena_id = col4.text_input("Enter Subpoena Number", key='subpoena_id')
case_name = col5.text_input("Enter Case Name", key='case_name')
issued_date = col6.date_input("Enter Date Issued", key='issued_date', format="MM/DD/YYYY")

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

# Containing next set of basic data
col7, col8 = st.columns(2)
response_deadline = col7.date_input("Enter Response Deadline", key='response_deadline', format="MM/DD/YYYY")
type_of_subpoena = col8.selectbox("Select Subpoena Type", ["Deposition", "Production of Documents", "Appearance"], key='type_of_subpoena')

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

# Party Information
with st.expander("Party Information"):
    col9, col10, col11 = st.columns(3)
    issuing_party = col9.text_input("Enter Issuing Party", key='issuing_party')
    issuing_party_contact = col10.text_input("Enter Contact Person", key='issuing_party_contact')
    contact_email = col11.text_input("Enter Contact Email", key='contact_email')

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

# Compliance Tracking
with st.expander("Compliance Tracking"):
    col12, col13 = st.columns(2)
    compliance_status = col12.selectbox("Select Status", ["Pending", "With Data Team", "Compiled", "Responded"], key='compliance_status')
    response_date = col13.date_input("Enter Response Date", key='response_date', format="MM/DD/YYYY")

    col14, = st.columns(1)
    notes_on_compliance = col14.text_area("Enter Notes", max_chars=500, key='notes_on_compliance')

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

# Function to clear session state
def clear_form():
    st.session_state['judicial_branch'] = "Federal"
    st.session_state['jurisdiction'] = ""
    st.session_state['court_information'] = ""
    st.session_state['subpoena_id'] = ""
    st.session_state['case_name'] = ""
    st.session_state['issued_date'] = None
    st.session_state['response_deadline'] = None
    st.session_state['type_of_subpoena'] = "Deposition"
    st.session_state['issuing_party'] = ""
    st.session_state['issuing_party_contact'] = ""
    st.session_state['contact_email'] = ""
    st.session_state['compliance_status'] = "Pending"
    st.session_state['response_date'] = None
    st.session_state['notes_on_compliance'] = ""

# Save data to CSV when the button is clicked
def submit_data():
    data = pd.DataFrame({
        'Judicial Branch': [st.session_state['judicial_branch']],
        'Jurisdiction': [st.session_state['jurisdiction']],
        'Court Information': [st.session_state['court_information']],
        'Subpoena ID': [st.session_state['subpoena_id']],
        'Case Name': [st.session_state['case_name']],
        'Issued Date': [st.session_state['issued_date']],
        'Response Deadline': [st.session_state['response_deadline']],
        'Type of Subpoena': [st.session_state['type_of_subpoena']],
        'Issuing Party': [st.session_state['issuing_party']],
        'Issuing Party Contact': [st.session_state['issuing_party_contact']],
        'Contact Email': [st.session_state['contact_email']],
        'Compliance Status': [st.session_state['compliance_status']],
        'Response Date': [st.session_state['response_date']],
        'Notes on Compliance': [st.session_state['notes_on_compliance']]
    })
    save_data(data)
    st.success("Data submitted successfully!")
    clear_form()

# Submit button with custom CSS
middle, = st.columns(1)
submit_data_button = st.button("Submit Data", on_click=submit_data)

# Load and display data from CSV
st.write("### Submitted Data")
st.dataframe(submitted_data)