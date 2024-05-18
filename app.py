import streamlit as st
import pandas as pd
import base64

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuration for the PostgreSQL connection
DATABASE_URI = 'postgresql://adithya14255:1Wg3FwivuZDU@ep-twilight-mode-70634399-pooler.ap-southeast-1.aws.neon.tech/medical?sslmode=require'

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URI)

query = "SELECT * FROM patients"

df_patients = pd.read_sql(query, engine)  


def add_bg_from_url(image_url):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url({image_url});
             background-size: cover;
             
         }}
         
         </style>
         """,
         unsafe_allow_html=True
     )
    

# Add background image
add_bg_from_url("https://4kwallpapers.com/images/walls/thumbs_3t/8324.png")
             

st.title('Patient Details Lookup')



# Input for patient's name and ID
patient_name = st.text_input('Enter Patient Name')
patient_id = st.number_input('Enter Patient ID', min_value=1)

# Search for patient
if st.button('Search'):
    patient = df_patients[(df_patients['Name'].str.lower() == patient_name.lower()) & (df_patients['ID'] == patient_id)]
    
    if not patient.empty:
        st.write('Patient Details:')
        st.table(patient)
        
        # Download link for the searched patient's details
        csv = patient.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="patient_details.csv">Download Patient Details</a>'
        st.markdown(href, unsafe_allow_html=True)
