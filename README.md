# Multiple Disease Prediction Web App & Docker Container

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

*This project utilizes StreamLit and Docker to create an interactive web application for predicting various diseases. This project includes prediction models for diabetes, Parkinson's disease, heart disease, and breast cancer.*

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Models](#models)
- [License](#license)

## About

*This web app provides a user-friendly interface to predict multiple diseases based on various input features. The machine learning models used in this application are trained on relevant datasets to make accurate predictions.*

The diseases currently supported by this web app include:
- Diabetes
- Parkinson's disease
- Heart disease
- Breast cancer

## Web App

- [Access the Web App](https://medipredict-v1.streamlit.app/) - Use the web app to predict multiple diseases.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AryanKaushal2002/MediPredict.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Navigate to the project directory:

    ```bash
    cd plant-disease-prediction
    ```

4. Create a virtual environment:

    ```bash
    python -m venv venv
    ```
5. Activate the virtual environment(You will have to create a virtual environment for the project):

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

6. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage for StreamLit

1. Run the web app:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and go to `http://localhost:8080` to access the web app.

3. Select the disease prediction page you want to use and provide the required input features.

4. Click on the **Test Result** button to generate the prediction result.

## Usage with Docker
1. Build the Docker image:

    ```bash
    docker build -t medipredict:v1.0 .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 80 medipredict:v1.0
    ```

3. Access the application in your browser at [http://localhost:8080](http://localhost:8080).

## Models

The machine learning models used in this web app are trained on publicly available datasets specific to each disease. Here is a brief description of each model:

- Diabetes Model: This model predicts the likelihood of a person having diabetes based on input features such as glucose level, blood pressure, BMI, etc.

- Parkinson's Disease Model: This model predicts the presence of Parkinson's disease in a person based on features extracted from voice recordings.

- Heart Disease Model: This model predicts the presence of heart disease based on various clinical and demographic features of a person.

- Breast Cancer Model: This model predicts whether a breast mass is malignant or benign using features derived from breast cytology.


## License

*This project is licensed under the [MIT License](LICENSE).*

---
