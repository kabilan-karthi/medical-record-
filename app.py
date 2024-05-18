import streamlit as st
import pandas as pd
import base64

# Define patient details with additional medical fields
patients = [
    {'ID': 1, 'Name': 'John Doe', 'Age': 30, 'Height': 175, 'Medical Contents': 'Healthy', 'Blood Pressure': '120/80', 'Heart Rate': 72, 'Blood Sugar': 90, 'Cholesterol': 180, 'BMI': 24, 'Allergies': 'None', 'Medications': 'None', 'Smoking Status': 'Non-smoker', 'Alcohol Consumption': 'None', 'Physical Activity': 'Regular', 'Diet': 'Balanced', 'Family History': 'None', 'Mental Health': 'Good', 'Sleep Patterns': 'Normal', 'Vision': '20/20', 'Hearing': 'Normal', 'Respiratory Rate': 16, 'Temperature': 98.6, 'Pain Level': 0},
    {'ID': 2, 'Name': 'Jane Smith', 'Age': 25, 'Height': 165, 'Medical Contents': 'Allergy to peanuts', 'Blood Pressure': '110/70', 'Heart Rate': 68, 'Blood Sugar': 85, 'Cholesterol': 170, 'BMI': 22, 'Allergies': 'Peanuts', 'Medications': 'Antihistamines', 'Smoking Status': 'Non-smoker', 'Alcohol Consumption': 'Occasional', 'Physical Activity': 'Regular', 'Diet': 'Vegetarian', 'Family History': 'Allergies', 'Mental Health': 'Good', 'Sleep Patterns': 'Normal', 'Vision': '20/20', 'Hearing': 'Normal', 'Respiratory Rate': 14, 'Temperature': 98.6, 'Pain Level': 0},
    {'ID': 3, 'Name': 'Sam Wilson', 'Age': 45, 'Height': 180, 'Medical Contents': 'Diabetic', 'Blood Pressure': '130/85', 'Heart Rate': 75, 'Blood Sugar': 150, 'Cholesterol': 200, 'BMI': 26, 'Allergies': 'None', 'Medications': 'Insulin', 'Smoking Status': 'Non-smoker', 'Alcohol Consumption': 'Occasional', 'Physical Activity': 'Moderate', 'Diet': 'Low carb', 'Family History': 'Diabetes', 'Mental Health': 'Good', 'Sleep Patterns': 'Normal', 'Vision': '20/25', 'Hearing': 'Normal', 'Respiratory Rate': 18, 'Temperature': 98.6, 'Pain Level': 0},
    {'ID': 4, 'Name': 'Sara Connor', 'Age': 35, 'Height': 170, 'Medical Contents': 'Asthmatic', 'Blood Pressure': '115/75', 'Heart Rate': 70, 'Blood Sugar': 90, 'Cholesterol': 180, 'BMI': 23, 'Allergies': 'Pollen', 'Medications': 'Inhaler', 'Smoking Status': 'Non-smoker', 'Alcohol Consumption': 'None', 'Physical Activity': 'Moderate', 'Diet': 'Balanced', 'Family History': 'Asthma', 'Mental Health': 'Good', 'Sleep Patterns': 'Normal', 'Vision': '20/20', 'Hearing': 'Normal', 'Respiratory Rate': 16, 'Temperature': 98.6, 'Pain Level': 0},
    {'ID': 5, 'Name': 'Tom Cruise', 'Age': 55, 'Height': 178, 'Medical Contents': 'High blood pressure', 'Blood Pressure': '140/90', 'Heart Rate': 78, 'Blood Sugar': 95, 'Cholesterol': 220, 'BMI': 27, 'Allergies': 'None', 'Medications': 'Antihypertensives', 'Smoking Status': 'Non-smoker', 'Alcohol Consumption': 'Moderate', 'Physical Activity': 'Regular', 'Diet': 'Low salt', 'Family History': 'Hypertension', 'Mental Health': 'Good', 'Sleep Patterns': 'Normal', 'Vision': '20/25', 'Hearing': 'Normal', 'Respiratory Rate': 16, 'Temperature': 98.6, 'Pain Level': 0},
    {'ID': 6, 'Name': 'Emma Watson', 'Age': 28, 'Height': 167, 'Medical Contents': 'Healthy', 'Blood Pressure': '120/80', 'Heart Rate': 72, 'Blood Sugar': 90, 'Cholesterol': 180, 'BMI': 24, 'Allergies': 'None', 'Medications': 'None', 'Smoking Status': 'Non-smoker', 'Alcohol Consumption': 'Occasional', 'Physical Activity': 'Regular', 'Diet': 'Balanced', 'Family History': 'None', 'Mental Health': 'Good', 'Sleep Patterns': 'Normal', 'Vision': '20/20', 'Hearing': 'Normal', 'Respiratory Rate': 16, 'Temperature': 98.6, 'Pain Level': 0},
    {'ID': 7, 'Name': 'Robert Downey', 'Age': 50, 'Height': 175, 'Medical Contents': 'Iron deficiency', 'Blood Pressure': '125/80', 'Heart Rate': 70, 'Blood Sugar': 95, 'Cholesterol': 190, 'BMI': 25, 'Allergies': 'None', 'Medications': 'Iron supplements', 'Smoking Status': 'Non-smoker', 'Alcohol Consumption': 'Moderate', 'Physical Activity': 'Regular', 'Diet': 'Balanced', 'Family History': 'Anemia', 'Mental Health': 'Good', 'Sleep Patterns': 'Normal', 'Vision': '20/25', 'Hearing': 'Normal', 'Respiratory Rate': 16, 'Temperature': 98.6, 'Pain Level': 0},
    {'ID': 8, 'Name': 'Chris Hemsworth', 'Age': 37, 'Height': 190, 'Medical Contents': 'Healthy', 'Blood Pressure': '120/80', 'Heart Rate': 72, 'Blood Sugar': 90, 'Cholesterol': 180, 'BMI': 24, 'Allergies': 'None', 'Medications': 'None', 'Smoking Status': 'Non-smoker', 'Alcohol Consumption': 'Occasional', 'Physical Activity': 'Regular', 'Diet': 'Balanced', 'Family History': 'None', 'Mental Health': 'Good', 'Sleep Patterns': 'Normal', 'Vision': '20/20', 'Hearing': 'Normal', 'Respiratory Rate': 16, 'Temperature': 98.6, 'Pain Level': 0},
    {'ID': 9, 'Name': 'Scarlett Johansson', 'Age': 35, 'Height': 164, 'Medical Contents': 'Allergic to shellfish', 'Blood Pressure': '115/75', 'Heart Rate': 68, 'Blood Sugar': 85, 'Cholesterol': 170, 'BMI': 22, 'Allergies': 'Shellfish', 'Medications': 'Antihistamines', 'Smoking Status': 'Non-smoker', 'Alcohol Consumption': 'Occasional', 'Physical Activity': 'Regular', 'Diet': 'Balanced', 'Family History': 'Allergies', 'Mental Health': 'Good', 'Sleep Patterns': 'Normal', 'Vision': '20/20', 'Hearing': 'Normal', 'Respiratory Rate': 14, 'Temperature': 98.6, 'Pain Level': 0},
    {'ID': 10, 'Name': 'Mark Ruffalo', 'Age': 52, 'Height': 180, 'Medical Contents': 'Hypertension', 'Blood Pressure': '135/85', 'Heart Rate': 74, 'Blood Sugar': 95, 'Cholesterol': 200, 'BMI': 26, 'Allergies': 'None', 'Medications': 'Antihypertensives', 'Smoking Status': 'Non-smoker', 'Alcohol Consumption': 'Moderate', 'Physical Activity': 'Moderate', 'Diet': 'Low salt', 'Family History': 'Hypertension', 'Mental Health': 'Good', 'Sleep Patterns': 'Normal', 'Vision': '20/25', 'Hearing': 'Normal', 'Respiratory Rate': 16, 'Temperature': 98.6, 'Pain Level': 0}
]

# Create a DataFrame
df_patients = pd.DataFrame(patients)
def add_bg_from_url(image_url):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url({https://media.istockphoto.com/id/1327568875/photo/healthcare-business-graph-data-and-growth-insurance-healthcare-doctor-analyzing-medical-of.jpg?s=612x612&w=0&k=20&c=R4idIeTPq0f1TPSJwAq4KUeLUQg6ul8eIBSjvs9MXQk=});
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    

# Add background image
add_bg_from_url("https://media.istockphoto.com/id/1327568875/photo/healthcare-business-graph-data-and-growth-insurance-healthcare-doctor-analyzing-medical-of.jpg?s=612x612&w=0&k=20&c=R4idIeTPq0f1TPSJwAq4KUeLUQg6ul8eIBSjvs9MXQk=") 
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
