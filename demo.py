
import streamlit as st 

# 🎨 Custom CSS for Styling
st.markdown("""
    <style>
        .card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            font-family: Arial, sans-serif;
        }
        .card h2 {
            color: #333;
            margin-bottom: 10px;
        }
        .card p {
            font-size: 16px;
            color: #555;
            margin: 5px 0;
        }
    </style>
""", unsafe_allow_html=True)

# 🌟 Streamlit UI Elements
st.header("👋 Hello, Welcome!")
st.title("📋 Data Entry Form")

name = st.text_input("Enter Your Name")
fnam = st.text_input("Enter Your Father's Name") 
adr = st.text_area("Enter Your Address") 
classdata = st.selectbox("Select Your Class:", ("10", "1st", "12th"))

button = st.button("✅ Submit")

# 🎯 If Button Clicked, Show Data in a Styled Card
if button:
    st.markdown(f"""
        <div class="card">
            <h2>🎓 Student Information</h2>
            <p><b>Name:</b> {name}</p>
            <p><b>Father's Name:</b> {fnam}</p>
            <p><b>Address:</b> {adr}</p>
            <p><b>Class:</b> {classdata}</p>
        </div>
    """, unsafe_allow_html=True)
