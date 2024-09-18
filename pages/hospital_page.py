import streamlit as st

def app():
    # Set page title, icon, and layout
    st.set_page_config(
        page_title="Multiple Disease Prediction System Using Machine Learning",
        page_icon="🩺",
        layout="wide"
    )

    # Advanced CSS for animations, colors, and styling
    st.markdown("""
        <style>
            /* Global Styling */
            body {
                background: #f4f7f9; /* Very light grey background */
                font-family: 'Roboto', sans-serif;
                color: #333;
                overflow-x: hidden;
                margin: 0;
                padding: 0;
            }
            .college-header {
                text-align: center;
                padding: 20px 20px;
                color: #003366;
                text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
                font-size: 1.5em;
                margin-bottom: 0;
                animation: fadeIn 1s ease-in-out;
            }
            .main-header {
                text-align: center;
                padding: 60px 20px;
                color: #003366;
                text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);
                font-size: 4em;
                animation: fadeIn 2s ease-in-out;
            }
            .sub-header {
                text-align: center;
                color: #003366;
                margin-bottom: 40px;
                font-size: 1.8em;
                animation: fadeIn 2s ease-in-out;
            }
            .content-section {
                padding: 60px 20px;
                background: #ffffff;
                margin: 20px 0;
                border-radius: 15px;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
                transform: scale(1);
                transition: transform 0.5s ease, box-shadow 0.5s ease;
                position: relative;
                z-index: 1;
                opacity: 1;
                overflow: hidden; /* Ensures the wavy effect stays within bounds */
            }
            .content-section:hover {
                transform: scale(1.03);
                box-shadow: 0 20px 30px rgba(0, 0, 0, 0.2);
            }
            .content-section::before {
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.1);
                transform: scaleY(0);
                transform-origin: bottom;
                transition: transform 0.6s ease;
                z-index: -1;
            }
            .content-section:hover::before {
                transform: scaleY(1);
            }
            .drop-down {
                font-size: 1.2em;
                margin: 20px 0;
                cursor: pointer;
                padding: 10px 15px;
                border-radius: 10px;
                border: 2px solid #003366;
                color: #003366;
                background: #e6f0ff;
                text-align: center;
                transition: all 0.3s;
                animation: fadeIn 1.5s ease-in-out;
            }
            .drop-down:hover {
                background: #003366;
                color: white;
            }
            .animated-background {
                background: linear-gradient(120deg, #e0e0e0, #ffffff);
                background-size: 400% 400%;
                animation: backgroundAnimation 15s ease infinite;
                padding: 60px 20px;
                border-radius: 15px;
                margin-top: 50px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
                position: relative;
                z-index: 1;
                overflow: hidden;
            }
            .slide-over-background {
                padding: 80px 20px;
                text-align: center;
                font-size: 1.3em;
                color: #333;
                background: #f9f9f9;
                animation: slideInFromBottom 2s ease-in-out forwards;
                margin-top: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
                position: relative;
                z-index: 1;
                overflow: hidden;
            }
            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }
            @keyframes slideInFromBottom {
                0% { transform: translateY(100px); opacity: 0; }
                100% { transform: translateY(0); opacity: 1; }
            }
            @keyframes backgroundAnimation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            /* Wavy effect */
            .wavy-background {
                position: relative;
                overflow: hidden;
                background: linear-gradient(120deg, #f4f7f9, #ffffff);
                background-size: 400% 400%;
                animation: backgroundAnimation 15s ease infinite;
            }
            .wavy-background::before {
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 200%;
                background: rgba(0, 0, 0, 0.2); /* Black waves */
                transform: translateY(-50%) skewY(-5deg);
                z-index: -1;
                opacity: 0.3;
                animation: waves 1s linear infinite;
            }
            @keyframes waves {
                0% { background-position: 0% 50%; }
                100% { background-position: 100% 50%; }
            }
        </style>
    """, unsafe_allow_html=True)

    # College Header
    st.markdown("<h2 class='college-header'>NIE 2025 Batch Final Year Project</h2>", unsafe_allow_html=True)

    # Main Header
    st.markdown("<h1 class='main-header'>ProActive Health Analytics System Using Machine Learning</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='sub-header'>Empower Your Health with Predictive Insights and Advanced Analytics</h3>", unsafe_allow_html=True)

    # Content Sections with Wavy Effect
    st.markdown("""
        <div class='content-section wavy-background'>
            <h2 style='text-align: center; color: #003366;'>Explore Our Cutting-Edge Models</h2>
            <p style='text-align: justify; font-size: 1.2em;'>
                Dive into the next generation of healthcare with predictive analytics that revolutionize the way we approach disease prevention. 
                Our system is built to provide accurate and reliable predictions across a range of common diseases.
            </p>
            <ul style='font-size: 1.2em; line-height: 1.8;'>
                <li>💡 <strong>Heart Disease Detection:</strong> Utilizing advanced algorithms for early diagnosis and improved outcomes.</li>
                <li>💡 <strong>Diabetes Risk Assessment:</strong> Monitor your health metrics and understand your risks in real-time.</li>
                <li>💡 <strong>Parkinson's Disease Predictor:</strong> Access innovative tools for proactive health management.</li>
                <li>💡 <strong>Breast Cancer Analysis:</strong> Leveraging machine learning for more accurate and timely detection.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class='content-section wavy-background'>
        <h2 style='text-align: center; color: #003366;'>Technologies and Libraries Used</h2>
        <p style='text-align: justify; font-size: 1.2em;'>
            Our Multiple Disease Prediction System utilizes a range of modern technologies, frameworks, and libraries to ensure accuracy, reliability, and a smooth user experience. Below are the key components of our tech stack:
        </p>
        <ul style='font-size: 1.2em; line-height: 1.8;'>
            <li><strong>Python:</strong> The primary programming language used for backend development and model implementation.</li>
            <li><strong>Streamlit:</strong> A framework for building interactive web applications for data science and machine learning.</li>
            <li><strong>Pandas:</strong> A library for data manipulation and analysis.</li>
            <li><strong>NumPy:</strong> A library for numerical computing with support for large matrices and arrays.</li>
            <li><strong>Scikit-learn:</strong> A machine learning library for building predictive models.</li>
            <li><strong>TensorFlow:</strong> An open-source library for deep learning and neural network modeling.</li>
            <li><strong>Matplotlib:</strong> A plotting library used for visualizing data and model results.</li>
            <li><strong>Seaborn:</strong> A statistical data visualization library based on Matplotlib.</li>
            <li><strong>Flask:</strong> A web framework used for creating a REST API to serve machine learning models.</li>
            <li><strong>Heroku:</strong> A cloud platform for deploying and managing applications.</li>
            <li><strong>Jupyter:</strong> A tool for creating and sharing live code, equations, visualizations, and narrative text.</li>
        </ul>
        <p style='text-align: justify; font-size: 1.2em;'>
            These tools and libraries work together to provide a comprehensive, user-friendly system for disease prediction and health management.
        </p>
    </div>
""", unsafe_allow_html=True)

    st.markdown("""
    <div class='content-section wavy-background'>
        <h2 style='text-align: center; color: #003366;'>Machine Learning Models & Classifications</h2>
        <p style='text-align: justify; font-size: 1.2em;'>
            Our system employs a range of advanced machine learning models to provide accurate health predictions. Each model is carefully chosen based on its effectiveness for the specific type of health issue. Here's a summary of the models used and their classifications:
        </p>
        <ul style='font-size: 1.2em; line-height: 1.8;'>
            <li>
                <strong>Heart Disease Detection:</strong> 
                <ul>
                    <li>Model Used: Random Forest Classifier</li>
                    <li>Classification: Supervised Learning, Ensemble Method</li>
                </ul>
            </li>
            <li>
                <strong>Diabetes Risk Assessment:</strong> 
                <ul>
                    <li>Model Used: Logistic Regression</li>
                    <li>Classification: Supervised Learning, Linear Model</li>
                </ul>
            </li>
            <li>
                <strong>Parkinson's Disease Prediction:</strong> 
                <ul>
                    <li>Model Used: Support Vector Machine (SVM)</li>
                    <li>Classification: Supervised Learning, Classification Algorithm</li>
                </ul>
            </li>
            <li>
                <strong>Breast Cancer Analysis:</strong> 
                <ul>
                    <li>Model Used: K-Nearest Neighbors (KNN)</li>
                    <li>Classification: Supervised Learning, Instance-Based Learning</li>
                </ul>
            </li>
        </ul>
    </div>
""", unsafe_allow_html=True)


    st.markdown("""
        <div class='content-section wavy-background'>
            <h2 style='text-align: center; color: #003366;'>Why Choose Us?</h2>
            <p style='text-align: justify; font-size: 1.2em;'>
                Our platform integrates the power of data science and predictive algorithms, crafted by experts to ensure precision, reliability, and ease of use. 
                Each model is trained on a vast dataset of clinical data, providing unparalleled insights that are trustworthy and actionable.
            </p>
            <p style='font-size: 1.2em; line-height: 1.8;'>
                With a user-friendly interface and cutting-edge technology, our system is designed to support healthcare professionals and individuals alike. 
                Engage with real-time analytics and stay ahead of health concerns with confidence and clarity.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='content-section wavy-background'>
            <h2 style='text-align: center; color: #003366;'>Interactive Features</h2>
            <p style='text-align: justify; font-size: 1.2em;'>
                Our system is equipped with interactive features designed to enhance user experience and provide deeper insights into health data. 
                Explore the following features to maximize your understanding and utilization of our predictive models.
            </p>
            <div class='drop-down'>Feature 1: Real-time Data Analysis</div>
            <div class='drop-down'>Feature 2: Personalized Health Insights</div>
            <div class='drop-down'>Feature 3: Advanced Visualization Tools</div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
