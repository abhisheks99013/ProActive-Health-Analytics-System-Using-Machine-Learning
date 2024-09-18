import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open("./models/diabetes_model_new.sav", 'rb'))
heart_model = pickle.load(open("./models/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("./models/parkinsons_model.sav", 'rb'))
breast_model = pickle.load(open("./models/breast_cancer_model.sav", 'rb'))

# Injecting custom CSS for animations, hover effects, and transparency
st.markdown("""
    <style>
    /* Basic styling for the entire page */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f2f6;
        color: #333;
    }
    
    /* Fade-in and pop-up effect for headings */
    h1, h2, h3 {
        animation: fadeIn 2s ease-out, popUp 2s ease-out;
        font-weight: 700;
        color: #2c3e50;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes popUp {
        from { transform: scale(0.9); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    
    /* Button animation */
    .stButton button {
        background-color: rgba(76, 175, 80, 0.8);
        border: none;
        color: white;
        padding: 12px 30px;
        text-align: center;
        font-size: 18px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
        border-radius: 5px;
    }
    
    .stButton button:hover {
        background-color: rgba(76, 175, 80, 1);
        transform: scale(1.1);
    }
    
    /* Input fields styling with transparency */
    .stTextInput > div {
        background-color: rgba(255, 255, 255, 0.9);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-radius: 5px;
    }
    
    .stTextInput > div:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Placeholder styling */
    .stTextInput input {
        color: #555;
    }
    
    .stTextInput input::placeholder {
        color: #aaa;
    }
    
    /* Success message styling */
    .stAlert {
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from { transform: translateY(100%); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    /* Sidebar active link styling */
    .nav-link.active {
        background-color: rgba(76, 175, 80, 0.8);
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Define a function to check if all elements in a list are numeric
def are_numeric(values):
    try:
        [float(val) for val in values]
        return True
    except ValueError:
        return False

# Define a function to convert input to float with error handling
def convert_to_float(value, default=0.0):
    try:
        return float(value) if value.strip() else default
    except ValueError:
        st.error(f"Invalid input: {value}. Please enter a valid number.")
        return default

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Heart Disease Prediction',
                            'Diabetes Prediction',
                            'Parkinson\'s Prediction',
                            'Breast Cancer Prediction'],
                           icons=['heart', 'activity', 'person', 'gender-female'],
                           default_index=0)

# Define the utility function
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

def are_numeric(values):
    return all(value is not None for value in values)

# Default values for placeholders
default_values = {
    'age': '45',
    'sex': '1',
    'cp': '2',
    'trestbps': '120',
    'chol': '220',
    'fbs': '1',
    'restecg': '1',
    'thalach': '160',
    'exang': '1',
    'oldpeak': '1.5',
    'slope': '2',
    'ca': '1',
    'thal': '2'
}

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    # Style configuration for columns
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .feature-box {
            border: 2px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 10px;
            background-color: #f9f9f9;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age (Enter number between 1-120)', placeholder='e.g., 45')

    with col2:
        sex = st.text_input('Sex (Enter 1 for Male, 0 for Female)', placeholder='e.g., 1')

    with col3:
        cp = st.text_input('Chest Pain types (Enter number between 0-3)', placeholder='e.g., 2')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (Enter number in mmHg)', placeholder='e.g., 120')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', placeholder='e.g., 220')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (Enter 1 for True, 0 for False)', placeholder='e.g., 1')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (Enter number between 0-2)', placeholder='e.g., 1')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', placeholder='e.g., 160')

    with col3:
        exang = st.text_input('Exercise Induced Angina (Enter 1 for Yes, 0 for No)', placeholder='e.g., 1')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise (Enter number)', placeholder='e.g., 1.5')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (Enter number between 0-2)', placeholder='e.g., 2')

    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy (Enter number between 0-3)', placeholder='e.g., 1')

    with col1:
        thal = st.text_input('thal: 1 = normal; 2 = fixed defect; 3 = reversible defect', placeholder='e.g., 2')

    # Code for Prediction
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        numeric_inputs = [convert_to_float(val) for val in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        
        # Display feature values
        st.write("Input Values:")
        for i, value in enumerate(numeric_inputs):
            st.write(f"Feature {i + 1}: {value}")
        
        if not are_numeric(numeric_inputs):
            st.warning("Please fill in all the fields with numeric values.")
        else:
            heart_prediction = heart_model.predict([numeric_inputs])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has a heart disease.'
                st.markdown("""
                    <div class="feature-box">
                        <h3 style="color: red;">Heart Disease Detected</h3>
                        <ul>
                            <li>Maintain a heart-healthy diet low in saturated fats and cholesterol.</li>
                            <li>Engage in regular physical activity, such as walking, cycling, or swimming.</li>
                            <li>Monitor your blood pressure and cholesterol levels regularly.</li>
                            <li>Take prescribed medications as directed by your healthcare provider.</li>
                            <li>Stay hydrated by drinking plenty of water.</li>
                            <li>Manage stress through relaxation techniques like meditation or yoga.</li>
                            <li>Avoid smoking and limit alcohol consumption.</li>
                            <li>Monitor and manage your weight to stay within a healthy range.</li>
                            <li>Get adequate sleep each night to support overall health.</li>
                            <li>Consult with a dietitian or healthcare provider for personalized advice.</li>
                        </ul>
                        <p style="color: red;">Please see a doctor for a thorough evaluation and management of your condition.</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                heart_diagnosis = 'The person does not have any heart disease.'
                st.markdown("""
                    <div class="feature-box">
                        <h3 style="color: green;">No Heart Disease Detected</h3>
                        <ul>
                            <li>Maintain a balanced diet rich in fruits, vegetables, and whole grains.</li>
                            <li>Incorporate regular physical activity into your routine.</li>
                            <li>Monitor your weight and maintain a healthy body mass index (BMI).</li>
                            <li>Stay hydrated and limit sugary drinks.</li>
                            <li>Get adequate sleep to support overall well-being.</li>
                            <li>Manage stress through relaxation techniques and hobbies.</li>
                            <li>Avoid smoking and excessive alcohol consumption.</li>
                            <li>Regularly check your blood pressure and cholesterol levels.</li>
                            <li>Schedule routine health check-ups with your healthcare provider.</li>
                            <li>Consider consulting a nutritionist for personalized dietary advice.</li>
                        </ul>
                        <p style="color: green;">Congratulations on maintaining good health! Keep up the great work.</p>
                    </div>
                """, unsafe_allow_html=True)
    
    st.success(heart_diagnosis)

# Define the utility function
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    # Style configuration for columns
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .feature-box {
            border: 2px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 10px;
            background-color: #f9f9f9;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', placeholder='e.g., 2')
        
    with col2:
        Glucose = st.text_input('Glucose Level', placeholder='e.g., 130')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', placeholder='e.g., 70')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value', placeholder='e.g., 20')
    
    with col2:
        Insulin = st.text_input('Insulin Level', placeholder='e.g., 80')
    
    with col3:
        BMI = st.text_input('BMI value', placeholder='e.g., 25')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', placeholder='e.g., 0.5')
    
    with col2:
        Age = st.text_input('Age of the Person', placeholder='e.g., 45')
    
    # Code for Prediction
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        numeric_inputs = [
            convert_to_float(Pregnancies),
            convert_to_float(Glucose),
            convert_to_float(BloodPressure),
            convert_to_float(SkinThickness),
            convert_to_float(Insulin),
            convert_to_float(BMI),
            convert_to_float(DiabetesPedigreeFunction),
            convert_to_float(Age)
        ]
        
        # Display feature values
        st.write("Input Values:")
        for i, value in enumerate(numeric_inputs):
            st.write(f"Feature {i + 1}: {value}")
        
        if None in numeric_inputs:
            st.warning("Please fill in all the fields with numeric values.")
        else:
            diab_prediction = diabetes_model.predict([numeric_inputs])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic.'
                st.markdown("""
                    <div class="feature-box">
                        <h3 style="color: red;">Diabetes Detected</h3>
                        <ul>
                            <li>Maintain a healthy diet low in sugar and refined carbohydrates.</li>
                            <li>Engage in regular physical activity, such as brisk walking or jogging.</li>
                            <li>Monitor your blood sugar levels regularly.</li>
                            <li>Take prescribed medications as directed by your healthcare provider.</li>
                            <li>Stay hydrated by drinking plenty of water.</li>
                            <li>Manage stress through techniques like meditation or yoga.</li>
                            <li>Get regular check-ups and follow your doctor's advice.</li>
                            <li>Reduce consumption of alcohol and avoid smoking.</li>
                            <li>Ensure adequate sleep to support overall health.</li>
                            <li>Consult a dietitian for personalized meal planning.</li>
                        </ul>
                        <p style="color: red;">Please see a doctor for a thorough evaluation and management of your condition.</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                diab_diagnosis = 'The person is not diabetic.'
                st.markdown("""
                    <div class="feature-box">
                        <h3 style="color: green;">No Diabetes Detected</h3>
                        <ul>
                            <li>Maintain a balanced diet rich in fruits, vegetables, and whole grains.</li>
                            <li>Incorporate regular physical activity into your routine.</li>
                            <li>Monitor your weight and maintain a healthy body mass index (BMI).</li>
                            <li>Stay hydrated and limit sugary drinks.</li>
                            <li>Get adequate sleep to support overall well-being.</li>
                            <li>Manage stress through relaxation techniques and hobbies.</li>
                            <li>Avoid smoking and excessive alcohol consumption.</li>
                            <li>Regularly check your blood pressure and cholesterol levels.</li>
                            <li>Schedule routine health check-ups with your healthcare provider.</li>
                            <li>Consider consulting a nutritionist for personalized dietary advice.</li>
                        </ul>
                        <p style="color: green;">Congratulations on maintaining good health! Keep up the great work.</p>
                    </div>
                """, unsafe_allow_html=True)
    
    st.success(diab_diagnosis)

# Define the utility function
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

# Parkinson's Prediction Page
if selected == 'Parkinson\'s Prediction':
    st.title('Parkinson\'s Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', placeholder='e.g., 200')
    
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', placeholder='e.g., 300')
    
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', placeholder='e.g., 100')
    
    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', placeholder='e.g., 0.1')
    
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', placeholder='e.g., 0.01')
    
    with col3:
        RAP = st.text_input('MDVP:RAP', placeholder='e.g., 0.1')
    
    with col1:
        PPQ = st.text_input('MDVP:PPQ', placeholder='e.g., 0.1')
    
    with col2:
        DDF = st.text_input('Shimmer:DDP', placeholder='e.g., 0.1')
    
    with col3:
        Shimmer = st.text_input('Shimmer', placeholder='e.g., 0.1')
    
    with col1:
        Shimmer_dB = st.text_input('Shimmer(dB)', placeholder='e.g., 0.1')
    
    with col2:
        ACP = st.text_input('AC', placeholder='e.g., 0.1')
    
    with col3:
        NHR = st.text_input('NHR', placeholder='e.g., 0.1')
    
    with col1:
        HNR = st.text_input('HNR', placeholder='e.g., 0.1')
    
    with col2:
        status = st.text_input('Status (Enter 1 for Parkinson\'s disease, 0 for Normal)', placeholder='e.g., 1')

    # Additional features
    with col3:
        # Add additional text inputs for the remaining 8 features
        feature_15 = st.text_input('Feature 15', placeholder='e.g., 0.1')
    
    with col1:
        feature_16 = st.text_input('Feature 16', placeholder='e.g., 0.1')
    
    with col2:
        feature_17 = st.text_input('Feature 17', placeholder='e.g., 0.1')
    
    with col3:
        feature_18 = st.text_input('Feature 18', placeholder='e.g., 0.1')
    
    with col1:
        feature_19 = st.text_input('Feature 19', placeholder='e.g., 0.1')
    
    with col2:
        feature_20 = st.text_input('Feature 20', placeholder='e.g., 0.1')
    
    with col3:
        feature_21 = st.text_input('Feature 21', placeholder='e.g., 0.1')
    
    with col1:
        feature_22 = st.text_input('Feature 22', placeholder='e.g., 0.1')
    
    # Code for Prediction
    park_diagnosis = ''
    if st.button('Parkinson\'s Test Result'):
        numeric_inputs = [
            convert_to_float(fo),
            convert_to_float(fhi),
            convert_to_float(flo),
            convert_to_float(Jitter_percent),
            convert_to_float(Jitter_Abs),
            convert_to_float(RAP),
            convert_to_float(PPQ),
            convert_to_float(DDF),
            convert_to_float(Shimmer),
            convert_to_float(Shimmer_dB),
            convert_to_float(ACP),
            convert_to_float(NHR),
            convert_to_float(HNR),
            convert_to_float(status),
            convert_to_float(feature_15),
            convert_to_float(feature_16),
            convert_to_float(feature_17),
            convert_to_float(feature_18),
            convert_to_float(feature_19),
            convert_to_float(feature_20),
            convert_to_float(feature_21),
            convert_to_float(feature_22)
        ]
        
        # Display feature values with styling
        st.write("Input Values:")
        for i, value in enumerate(numeric_inputs):
            color = 'green' if value is not None else 'red'
            st.markdown(f"<p style='color: {color};'>Feature {i + 1}: {value}</p>", unsafe_allow_html=True)
        
        if None in numeric_inputs:
            st.warning("Please fill in all the fields with numeric values.")
        else:
            park_prediction = parkinsons_model.predict([numeric_inputs])
            if park_prediction[0] == 1:
                park_diagnosis = 'The person has Parkinson\'s disease.'
                # Remedies and care tips
                st.markdown("""
                <div style="border: 2px solid red; padding: 10px; border-radius: 5px;">
                <h3 style='color: red;'>You have Parkinson's disease.</h3>
                <h4>Here are some remedies and self-care tips:</h4>
                <ul>
                    <li>1. Consult a neurologist for personalized treatment.</li>
                    <li>2. Follow a structured exercise program.</li>
                    <li>3. Consider speech therapy to improve communication skills.</li>
                    <li>4. Stay mentally active with cognitive exercises.</li>
                    <li>5. Maintain a healthy diet to support overall well-being.</li>
                    <li>6. Join a support group for emotional and practical support.</li>
                    <li>7. Monitor medication and report side effects to your doctor.</li>
                    <li>8. Implement safety measures at home to prevent falls.</li>
                    <li>9. Educate yourself about the disease and its progression.</li>
                    <li>10. Regularly follow up with your healthcare provider.</li>
                </ul>
                <p><strong>It is important to see a doctor as soon as possible.</strong></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                park_diagnosis = 'The person does not have Parkinson\'s disease.'
                # Health tips
                st.markdown("""
                <div style="border: 2px solid green; padding: 10px; border-radius: 5px;">
                <h3 style='color: green;'>Congratulations! You do not have Parkinson's disease.</h3>
                <h4>Here are some tips to stay healthy:</h4>
                <ul>
                    <li>1. Engage in regular physical activity.</li>
                    <li>2. Maintain a balanced and nutritious diet.</li>
                    <li>3. Stay hydrated by drinking plenty of water.</li>
                    <li>4. Get adequate sleep each night.</li>
                    <li>5. Manage stress through relaxation techniques.</li>
                    <li>6. Avoid smoking and limit alcohol consumption.</li>
                    <li>7. Keep your mind active with mental exercises.</li>
                    <li>8. Regularly check your health with routine screenings.</li>
                    <li>9. Foster strong social connections and relationships.</li>
                    <li>10. Practice good hygiene to prevent infections.</li>
                </ul>
                <p><strong>Keep up the good work and stay healthy!</strong></p>
                </div>
                """, unsafe_allow_html=True)
    st.success(park_diagnosis)

# Define the utility function
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None
# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mean_radius = st.text_input('Mean Radius', placeholder='e.g., 12.0')
    
    with col2:
        mean_texture = st.text_input('Mean Texture', placeholder='e.g., 18.0')
    
    with col3:
        mean_perimeter = st.text_input('Mean Perimeter', placeholder='e.g., 80.0')
    
    with col1:
        mean_area = st.text_input('Mean Area', placeholder='e.g., 500.0')
    
    with col2:
        mean_smoothness = st.text_input('Mean Smoothness', placeholder='e.g., 0.1')
    
    with col3:
        mean_compactness = st.text_input('Mean Compactness', placeholder='e.g., 0.1')
    
    with col1:
        mean_concavity = st.text_input('Mean Concavity', placeholder='e.g., 0.1')
    
    with col2:
        mean_concave_points = st.text_input('Mean Concave Points', placeholder='e.g., 0.1')
    
    with col3:
        mean_symmetry = st.text_input('Mean Symmetry', placeholder='e.g., 0.1')
    
    with col1:
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension', placeholder='e.g., 0.1')
    
    with col2:
        radius_error = st.text_input('Radius Error', placeholder='e.g., 1.0')
    
    with col3:
        texture_error = st.text_input('Texture Error', placeholder='e.g., 1.0')
    
    with col1:
        perimeter_error = st.text_input('Perimeter Error', placeholder='e.g., 1.0')
    
    with col2:
        area_error = st.text_input('Area Error', placeholder='e.g., 1.0')
    
    with col3:
        smoothness_error = st.text_input('Smoothness Error', placeholder='e.g., 0.01')
    
    with col1:
        compactness_error = st.text_input('Compactness Error', placeholder='e.g., 0.01')
    
    with col2:
        concavity_error = st.text_input('Concavity Error', placeholder='e.g., 0.01')
    
    with col3:
        concave_points_error = st.text_input('Concave Points Error', placeholder='e.g., 0.01')
    
    with col1:
        symmetry_error = st.text_input('Symmetry Error', placeholder='e.g., 0.01')
    
    with col2:
        fractal_dimension_error = st.text_input('Fractal Dimension Error', placeholder='e.g., 0.01')
    
    with col3:
        worst_radius = st.text_input('Worst Radius', placeholder='e.g., 15.0')
    
    with col1:
        worst_texture = st.text_input('Worst Texture', placeholder='e.g., 25.0')
    
    with col2:
        worst_perimeter = st.text_input('Worst Perimeter', placeholder='e.g., 100.0')
    
    with col3:
        worst_area = st.text_input('Worst Area', placeholder='e.g., 600.0')
    
    with col1:
        worst_smoothness = st.text_input('Worst Smoothness', placeholder='e.g., 0.15')
    
    with col2:
        worst_compactness = st.text_input('Worst Compactness', placeholder='e.g., 0.15')
    
    with col3:
        worst_concavity = st.text_input('Worst Concavity', placeholder='e.g., 0.15')
    
    with col1:
        worst_concave_points = st.text_input('Worst Concave Points', placeholder='e.g., 0.15')
    
    with col2:
        worst_symmetry = st.text_input('Worst Symmetry', placeholder='e.g., 0.15')
    
    with col3:
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension', placeholder='e.g., 0.15')
    
    # Code for Prediction
    cancer_diagnosis = ''
    if st.button('Breast Cancer Test Result'):
        numeric_inputs = [
            convert_to_float(mean_radius),
            convert_to_float(mean_texture),
            convert_to_float(mean_perimeter),
            convert_to_float(mean_area),
            convert_to_float(mean_smoothness),
            convert_to_float(mean_compactness),
            convert_to_float(mean_concavity),
            convert_to_float(mean_concave_points),
            convert_to_float(mean_symmetry),
            convert_to_float(mean_fractal_dimension),
            convert_to_float(radius_error),
            convert_to_float(texture_error),
            convert_to_float(perimeter_error),
            convert_to_float(area_error),
            convert_to_float(smoothness_error),
            convert_to_float(compactness_error),
            convert_to_float(concavity_error),
            convert_to_float(concave_points_error),
            convert_to_float(symmetry_error),
            convert_to_float(fractal_dimension_error),
            convert_to_float(worst_radius),
            convert_to_float(worst_texture),
            convert_to_float(worst_perimeter),
            convert_to_float(worst_area),
            convert_to_float(worst_smoothness),
            convert_to_float(worst_compactness),
            convert_to_float(worst_concavity),
            convert_to_float(worst_concave_points),
            convert_to_float(worst_symmetry),
            convert_to_float(worst_fractal_dimension)
        ]
        
        # Display feature values with styling
        st.write("Input Values:")
        for i, value in enumerate(numeric_inputs):
            color = 'green' if value is not None else 'red'
            st.markdown(f"<p style='color: {color};'>Feature {i + 1}: {value}</p>", unsafe_allow_html=True)
        
        if None in numeric_inputs:
            st.warning("Please fill in all the fields with numeric values.")
        else:
            cancer_prediction = breast_model.predict([numeric_inputs])
            if cancer_prediction[0] == 1:
                cancer_diagnosis = 'The person has breast cancer.'
                # Remedies and care tips
                st.markdown("""
                <div style="border: 2px solid red; padding: 10px; border-radius: 5px;">
                <h3 style='color: red;'>You have breast cancer.</h3>
                <h4>Here are some remedies and self-care tips:</h4>
                <ul>
                    <li>1. Consult an oncologist for personalized treatment options.</li>
                    <li>2. Consider joining a support group for emotional support.</li>
                    <li>3. Follow a treatment plan prescribed by your healthcare provider.</li>
                    <li>4. Maintain a healthy diet to support overall health.</li>
                    <li>5. Engage in regular physical activity, as advised by your doctor.</li>
                    <li>6. Get regular follow-up appointments and screenings.</li>
                    <li>7. Educate yourself about breast cancer and treatment options.</li>
                    <li>8. Practice good hygiene and take care of any side effects from treatment.</li>
                    <li>9. Communicate openly with your healthcare team about any concerns.</li>
                    <li>10. Seek professional help if you experience anxiety or depression.</li>
                </ul>
                <p><strong>It is crucial to see a healthcare provider as soon as possible.</strong></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                cancer_diagnosis = 'The person does not have breast cancer.'
                # Health tips
                st.markdown("""
                <div style="border: 2px solid green; padding: 10px; border-radius: 5px;">
                <h3 style='color: green;'>Congratulations! You do not have breast cancer.</h3>
                <h4>Here are some tips to stay healthy:</h4>
                <ul>
                    <li>1. Maintain a balanced and nutritious diet.</li>
                    <li>2. Engage in regular exercise to stay physically active.</li>
                    <li>3. Limit alcohol consumption and avoid smoking.</li>
                    <li>4. Perform regular self-breast exams and routine screenings.</li>
                    <li>5. Manage stress through relaxation techniques and hobbies.</li>
                    <li>6. Stay hydrated by drinking plenty of water.</li>
                    <li>7. Get adequate sleep to support overall health.</li>
                    <li>8. Foster strong social connections and relationships.</li>
                    <li>9. Practice good hygiene and wellness habits.</li>
                    <li>10. Keep up with regular health check-ups and preventive care.</li>
                </ul>
                <p><strong>Keep up the good work and stay healthy!</strong></p>
                </div>
                """, unsafe_allow_html=True)
    st.success(cancer_diagnosis)
