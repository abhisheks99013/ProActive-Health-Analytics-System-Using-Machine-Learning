import streamlit as st
import sqlite3

# Function to register a new user
def register_user(username, password):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        st.success("Registration successful! You can now log in.")
    except sqlite3.IntegrityError:
        st.error("Username already exists. Please choose a different username.")
    finally:
        conn.close()

def app():
    st.title("Register Page")

    # Create a form for user registration
    with st.form(key='register_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        confirm_password = st.text_input("Confirm Password", type='password')
        submit_button = st.form_submit_button("Register")

        if submit_button:
            if password == confirm_password:
                register_user(username, password)
            else:
                st.error("Passwords do not match. Please try again.")
if __name__ == "__main__":
    app()
