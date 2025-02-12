# Subpoena Tracker

## Overview
The Subpoena Tracker is a Streamlit-based web application designed to log and track the issuance and compliance of subpoenas. It allows users to input subpoena details, save them to a CSV file, and view the submitted data.

## Features
- Log subpoena details including judicial branch, jurisdiction, court information, subpoena ID, case name, issued date, response deadline, type of subpoena, issuing party, issuing party contact, contact email, compliance status, response date, and notes on compliance.
- Edit existing entries by selecting them from a dropdown list.
- Save data to a CSV file and load existing data from the CSV file.
- Clear form fields after submission.
- Custom CSS styling for a better user interface.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd subpoena_tracker
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```
2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## File Structure
- `main.py`: The main application file containing the Streamlit code.
- `requirements.txt`: A file listing the required Python packages.
- `subpoena_data.csv`: The CSV file where subpoena data is saved (created after the first submission).

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.