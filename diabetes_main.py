# Code for 'diabetes_main.py' file.

# Importing the necessary Python modules.
import streamlit as st
import numpy as np
import pandas as pd

# Configure your home page by setting its title and icon that will be displayed in a browser tab.
st.set_page_config(page_title = 'Early Diabetes Prediction Web App',
                    page_icon = ':boy',
                    layout = 'wide',
                    initial_sidebar_state = 'auto'
                    )

# Loading the dataset.
@st.cache()
def load_data():
    # Load the Diabetes dataset into DataFrame.

    df = pd.read_csv('https://s3-whjr-curriculum-uploads.whjr.online/b510b80d-2fd6-4c08-bfdf-2a24f733551d.csv')
    df.head()

    # Rename the column names in the DataFrame.
    df.rename(columns = {"BloodPressure": "Blood_Pressure",}, inplace = True)
    df.rename(columns = {"SkinThickness": "Skin_Thickness",}, inplace = True)
    df.rename(columns = {"DiabetesPedigreeFunction": "Pedigree_Function",}, inplace = True)

    df.head() 

    return df

diabetes_df = load_data()

# Create the Page Navigator for 'Home', 'Predict Diabetes' and 'Visualise Decision Tree' web pages in 'diabetes_main.py'
# Import the 'diabetes_predict' 'diabetes_home', 'diabetes_plots' Python files
import diabetes_predict as predict
import diabetes_home as home
import diabetes_plot as plot


# Adding a navigation in the sidebar using radio buttons
# Create the 'pages_dict' dictionary to navigate.
pages_dict = {"Home": home,
              "Predict Diabetes":predict,
              "Visualise Decision Tree":plot
             }
# Add radio buttons in the sidebar for navigation and call the respective pages based on user selection.
st.sidebar.title("Navigator")
user_choice = st.sidebar.radio("Go to",(pages_dict))

if user_choice == "Home":
  home.app(diabetes_df)

else:
  selected_app = pages_dict[user_choice]
  selected_app.app(diabetes_df)   