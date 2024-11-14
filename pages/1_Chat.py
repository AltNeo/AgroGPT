import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# Load Font Awesome via a <link> tag
st.markdown(
        r"""<head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        </head>
        """,
        unsafe_allow_html=True
    )

def main():
    # Navigation button to return home
    if st.button('🏠 Home', key='nav_home', help='Return Home'):
        st.switch_page("main.py")

    # Custom CSS for aligning the title, logo, and subheading
    st.markdown(
        r"""<style>
        /* Set background color for the entire page */
        .stApp {
            background-color: #e0f0e3;  /* Pastel green */
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 20px 0;
            background-color: #e0f0e3;  /* Pastel green */
            margin-bottom: 20px;
        }
        .logo-img {
            width: 80px;  /* Adjust the size of the logo here */
            margin-right: 10px;  /* Reduce spacing between the logo and heading */
        }
        .heading-text {
            text-align: center;
            margin: 0;  /* Remove margins around the heading */
            padding: 0;  /* Remove padding around the heading */
            font-size: 50px;  /* Adjust the size of the heading text */
            color: black;  /* Set text color to black */
        }
        .subheading {
            text-align: center;
            margin-top: 30px;  /* Adjust spacing between title and subheading */
            font-size: 20px;
            color: black;  /* Optional: You can change the color to make it distinct */
        }
        .english-button {
            display: block;
            margin: 10px auto;  /* Center the button */
            padding: 5px 20px;  /* Padding for the button */
            font-size: 16px;  /* Font size of the button text */
            background-color: #007BFF;  /* Button color */
            color: white;  /* Text color */
            border: none;  /* No border */
            border-radius: 5px;  /* Rounded corners */
            cursor: pointer;  /* Cursor change on hover */
        }
        .english-button:hover {
            background-color: #0056b3;  /* Darker shade on hover */
        }

        .mic-button {
            display: block;
            margin: 20px auto;  /* Center the button and add some space from the English button */
            width: 60px;  /* Diameter of the circular button */
            height: 60px;  /* Diameter of the circular button */
            background-color: #007BFF;  /* Blue background color like the English button */
            color: white;  /* Icon color */
            border: none;  /* No border */
            border-radius: 50%;  /* Makes the button round */
            font-size: 24px;  /* Size of the microphone icon */
            cursor: pointer;  /* Cursor change on hover */
        }
        .mic-button:hover {
            background-color: #0056b3;  /* Darker shade of blue on hover */
        }

        /* Container for small buttons next to each other */
        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;  /* Add space between the buttons */
            margin-top: 20px;  /* Add some space from the mic button */
        }

        .small-button {
            padding: 5px 15px;  /* Small padding */
            font-size: 14px;  /* Smaller font size */
            background-color: #007BFF;  /* Blue background color like the English button */
            color: white;  /* Text color */
            border: none;  /* No border */
            border-radius: 5px;  /* Rounded corners */
            cursor: pointer;  /* Cursor change on hover */
        }
        .small-button:hover {
            background-color: #0056b3;  /* Darker blue on hover */
        }

        .examples-container {
            text-align: center;
            margin-top: 10px;  /* Adds space above the text */
        }
        .examples-text {
            font-size: 18px;  /* Font size of the text */
            color: #333333;  /* Dark gray color for the text */
            font-weight: bold;  /* Makes the text bold */
        }

        /* Style for rectangular buttons arranged in two rows, each row having two buttons */
        .example-buttons-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;  /* Vertical space between the rows */
        }

        .button-row {
            display: flex;
            justify-content: center;
            gap: 20px;  /* Horizontal space between the buttons */
        }

        .example-button {
            padding: 10px 20px;  /* Padding for rectangular buttons */
            font-size: 14px;  /* Adjust font size */
            background-color: #e0f0e3;  /* Pastel green */
            color: black;  /* Black text color */
            border: 2px solid #007BFF;  /* Border color */
            border-radius: 5px;  /* Slightly rounded corners */
            cursor: pointer;
            width: 300px;  /* Set a fixed width for all buttons */
            height: 50px;  /* Fixed height to ensure text is centered */
            display: flex;
            justify-content: center;
            align-items: center;  /* Center text vertically and horizontally */
            text-align: center;
            white-space: nowrap;  /* Prevent text from wrapping */
        }

        .example-button:hover {
            background-color: #f0f0f0;  /* Light gray hover effect */
        }        /* Hide sidebar */
        [data-testid="stSidebar"][aria-expanded="true"] {
            display: none;
        }
        [data-testid="stSidebar"][aria-expanded="false"] {
            display: none;
        }
        /* Hide sidebar */
        [data-testid="stSidebar"][aria-expanded="true"] {
            display: none;
        }
        [data-testid="stSidebar"][aria-expanded="false"] {
            display: none;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    # Displaying the logo and heading side by side
    st.markdown(
        r"""
        <div class="header-container">
            <h1 class='heading-text'>AgroGPT</h1>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Display the subheading
    st.markdown(r"<h2 class='subheading'>Agriculture CoPilot for India</h2>", unsafe_allow_html=True)


    st.markdown(r"""
        <button class="english-button">English</button>
    """, unsafe_allow_html=True)

    # Microphone button with Font Awesome icon
    st.markdown(r"""
        <button class="mic-button"><i class="fas fa-microphone"></i></button>
    """, unsafe_allow_html=True)

    # Container for small buttons
    st.markdown(r"""
        <div class="button-container">
            <button class="small-button"><i class="fas fa-keyboard"></i></button>
            <button class="small-button">Lang</button>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(r"""
        <div class="examples-container">
            <p class="examples-text"><strong>Few examples to ask!</strong></p>
        </div>
    """, unsafe_allow_html=True)

    # Add two rows of rectangular buttons, each row having two buttons aligned side by side
    st.markdown(r"""
        <div class="example-buttons-container">
            <!-- First row of buttons -->
            <div class="button-row">
                <button class="example-button">How to improve soil condition?</button>
                <button class="example-button">Effective methods for pest control on cabbage?</button>
            </div>
            <!-- Second row of buttons -->
            <div class="button-row">
                <button class="example-button">Best time to plant okra in North India?</button>
                <button class="example-button">Methods for pest control on mango tree?</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()