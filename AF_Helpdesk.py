import streamlit as st
import cx_Oracle

# Function to fetch data from Oracle database based on department
def fetch_data(department):
    # Connect to Oracle database
    connection = cx_Oracle.connect('hr/HR@localhost:1521/XE')
    cursor = connection.cursor()

    # Fetch data based on department
    query = f"SELECT name, contact, Email_ID, Whatsapp_No, Prefered_language FROM CONTACT WHERE department = '{department}'"
    cursor.execute(query)
    data = cursor.fetchall()

    # Close connection
    cursor.close()
    connection.close()

    return data

# Main function to run Streamlit web app
def main():
    st.set_page_config(page_title="Helpdesk",page_icon=":telephone_receiver:",layout="wide")
    st.title(" :telephone_receiver: Anudip Foundation For Social Welfare")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
    

    # Sidebar for department selection
    department = st.sidebar.selectbox('Select Department', ('Academic Excellence', 'Attendance', 'L&D', 'DV Team','Content', 'Tech Team'))

    # Fetch data based on selected department
    data = fetch_data(department)

    # Display data in main panel
    if data:
        st.subheader(f'Helpdesk from {department}:')
        for row in data:
            st.write(f"Name: {row[0]}")
            st.write(f"Contact: {row[1]}")
            st.write(f"Email ID: {row[2]}")
            st.write(f"Whatsapp No: {row[3]}")
            st.write(f"Preferred Language: {row[4]}")
            st.write("---")
    else:
        st.write("No data available for this department.")

if __name__ == "__main__":
    main()
