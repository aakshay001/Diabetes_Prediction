# Import the streamlit modules.
import streamlit as st

# Define a function 'app()' which accepts 'census_df' as an input.
def app(diabetes_df):
    # Set the title to the home page contents.
    st.title("Early Diabetes Prediction Web App")
    # Provide a brief description for the web app.
    st.text("""Diabetes is a chronic (long-lasting) health conditionthat affects how your body turns food into energy.There isn’t
    a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help inreducing the impact
    of diabetes.This Web app will help you to predict whether a person hasdiabetes or is prone to get diabetes in future
    by analysing the values of several features using the Decision Tree Classifier.""")

    # Add the 'beta_expander' to view full dataset 
    st.subheader("View Data")
    with st.beta_expander("View Dataset"):
      st.table(diabetes_df)
    

    beta_col1,beta_col2,beta_col3 = st.beta_columns(3)
    # Add a checkbox in the first column. Display the column names of 'diabetes_df' on the click of checkbox.
    with beta_col1:
      if st.checkbox("Show all Column Names"):
        st.table(list(diabetes_df.columns))

    # Add a checkbox in the second column. Display the column data-types of 'diabetes_df' on the click of checkbox.
    with beta_col2:
      if st.checkbox("View column data-type"):
        st.text(diabetes_df.dtypes)

    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with beta_col3:
      if st.checkbox("View Column Data"):
        col = st.selectbox("Select Column",list(diabetes_df.columns))
        st.table(diabetes_df[col])

    if st.checkbox("Show Summary"):
      st.table(diabetes_df.describe())  