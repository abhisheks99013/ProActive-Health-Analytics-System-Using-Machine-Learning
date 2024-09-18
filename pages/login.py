import streamlit as st
import sqlite3

# Function to authenticate user
def authenticate_user(username, password):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def app():
    st.markdown("""
    <style>
        .login-container {
            position: relative;
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            animation: fadeIn 1s ease-in-out, slideUp 0.5s ease-out;
        }
        .login-title {
            font-size: 24px;
            font-weight: bold;
            color: #003366;
            text-align: center;
            margin-bottom: 20px;
            animation: fadeIn 1s ease-in-out, slideUp 0.5s ease-out;
        }
        .form-field {
            position: relative;
            margin-bottom: 20px;
        }
        .form-field input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
        }
        .form-field input:focus {
            border-color: #003366;
            box-shadow: 0 0 12px rgba(0,0,0,0.3);
            transform: scale(1.05);
            background-color: #f0f8ff;
        }
        .login-button {
            width: 100%;
            padding: 10px;
            background-color: #003366;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s, transform 0.3s, box-shadow 0.3s;
        }
        .login-button:hover {
            background-color: #002244;
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideUp {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="login-title">Login Page</div>', unsafe_allow_html=True)

    # Create a form for user input
    with st.form(key='login_form'):
        st.markdown('<div class="form-field">', unsafe_allow_html=True)
        username = st.text_input("Username", placeholder="Enter your username")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-field">', unsafe_allow_html=True)
        password = st.text_input("Password", type='password', placeholder="Enter your password")
        st.markdown('</div>', unsafe_allow_html=True)
        
        submit_button = st.form_submit_button("Login")

        if submit_button:
            # Authenticate user
            user = authenticate_user(username, password)
            if user:
                st.success("You have successfully logged into your account. Now you can access different features of our application.")
            else:
                st.error("Invalid username or password")

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
