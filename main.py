# import streamlit as st

# st.set_page_config(page_title="SIWES Management System", page_icon="🎓")

# st.title("Welcome to the SIWES Management System")
# st.write("Manage SIWES supervision, assessment, and student progress tracking.")

# # Redirect Button to Login Page
# if st.button("Go to Login Page"):
#     st.switch_page("pages/login.py")  # Correct format

import streamlit as st

# Page Configuration
st.set_page_config(page_title="SIWES Management System", page_icon="🎓", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Background and Fonts */
        body {
            font-family: 'Arial', sans-serif;
        }
        
        .main {
            background-color:rgb(20, 25, 124);
            padding: 20px;
            border-radius: 10px;
        }

        /* Container for Centering */
        .container {
            max-width: 800px;
            margin: auto;
            text-align: center;
            padding: 50px 20px;
        }

        /* Logo Styling */
        .logo {
            width: 120px;
            margin-bottom: 10px;
        }
        
        .logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Title */
        h1 {
            color: #2c3e50;
            font-size: 2.5rem;
            font-weight: bold;
        }

        /* Description */
        .description {
            font-size: 1.2rem;
            color: #34495e;
            margin-bottom: 30px;
        }

        /* Styled Button */
        .custom-button {
            background-color:rgb(163, 19, 21);
            color: white;
            padding: 12px 25px;
            border-radius: 25px;
            text-decoration: none;
            font-size: 1rem;
            font-weight: bold;
            display: inline-block;
            transition: 0.3s;
        }

        .custom-button:hover {
            background-color:rgb(223, 166, 171);
        }
    </style>
""", unsafe_allow_html=True)


# Display Logo
st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
st.image("miva_logo.jpg", width=120)
st.markdown("</div>", unsafe_allow_html=True)

# <img src='miva_logo.jpg' class='logo' />

# Main Container
st.markdown("""
    <div class='container'>
        <h1>Welcome to the SIWES Management System</h1>
        <p class='description'>Manage SIWES supervision, assessment, and student progress tracking with ease.</p>
        <a href='#' class='custom-button'>Go to Login Page</a>
    </div>
""", unsafe_allow_html=True)