
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Page Config ---
st.set_page_config(page_title="Academic Student Performance Analytics 2025", layout="wide")


# --- Navigation Sidebar ---
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["Data Visualization", "Model Forecasting", "Login"])



# --- 1) DATA VISUALIZATION PAGE ---
if page == "Data Visualization":
    st.title("📊 Student Performance Data Insights")
    st.markdown("Exploring key drivers of academic success in the 2025 dataset")



    data = {
    'Ethnicity': ['Group E', 'Group D', 'Group C', 'Group B', 'Group A'],
    'Parent_Edu': ["Master's", "Bachelor's", "High School", "College", "Associate's"],
    'Lunch': ['Standard', 'Free', 'Standard', 'Free', 'Standard'],
    'Maths Score': [65 , 68 , 72 , 70 , 75 ],
    'Reading Score': [64 ,67 ,69 , 70 , 73],
    'Writing Score': [62 ,65 ,70 ,71 ,74],
    'Gender' : ['male','female','male','female','female'],
    'Study_Hours' : [2,4,3,5,8],
    'SCI':[5.2,12.1,3.4,15.6,2.1]
    }

    df= pd.DataFrame(data)


    # ROW 1: Distribution & Categories
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("1. Ethnicity vs Reading")
        fig1 = px.pie(df, names='Ethnicity', values='Reading Score',
                      color_discrete_sequence=px.colors.sequential.Blues_r,
                      template='plotly_dark')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("2. Score Distribution")
        df_melt = df.melt(value_vars=['Maths Score','Reading Score','Writing Score'], var_name='Subject', value_name='Score')
        fig2 = px.bar(df_melt, x='Subject', y='Score', color='Subject')
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        st.subheader("3. Gender Performance")
        avg_gender= df.groupby('Gender')[['Maths Score','Reading Score', 'Writing Score']].mean().reset_index()
        fig3 = px.pie(avg_gender, values='Maths Score', names='Gender', hole=0.4, title="Maths Distribution")
        st.plotly_chart(fig3, use_container_width=True)

    # ROW 2: Correlations & Comparisons
    col4, col5, col6 = st.columns(3)
    with col4:
        st.subheader("4. Study Hours vs Maths Score")
        fig4 = px.scatter(
                 df,
                 x='Study_Hours',
                 y='Maths Score',
                 color='Gender',
                 size='SCI',
                 title="Impact of Study Hours on Maths Score",
                 template="plotly_dark"
         )
        st.plotly_chart(fig4, use_container_width=True)
    with col5:
        st.subheader("5. Score Consistency (SCI)")
        fig5 = px.histogram(df, x='SCI', nbins=10, title="Consistency Spread", color_discrete_sequence=['indianred'])
        st.plotly_chart(fig5, use_container_width=True)

    with col6:
        st.subheader("6. Subject Correlation")
        corr = df[['Maths Score', 'Reading Score', 'Writing Score']].corr()
        fig6 = px.imshow(corr,text_auto=True, color_continuous_scale='RdBu_r')
        st.plotly_chart(fig6, use_container_width=True)

# --- 2) MODEL FORECASTING PAGE ---
elif page == "Model Forecasting":
    st.title("🤖 Performance Forecasting")
    st.info("The Model Forecasting module is being initialized. This will include Linear Regression/Random Forest inputs.")
    # Add your input widgets here (e.g., st.number_input)

# --- LOGOUT ---
elif page == "Login":
    st.title("Secure Access")
    username= st.text_input("Username")
    password= st.text_input("Password", type="password")
    if st.button("Login"):
        st.success(f"Welcome back, {username}!")
