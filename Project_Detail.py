import streamlit as st
import pandas as pd
import plotly.express as px

# Apply CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Project Detail", layout="wide")
st.title("Project Detail")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Data Loaded!")

    chart_type = st.selectbox("Chart Type", ["Scatter", "Line", "Bar", "Heatmap"])
    if chart_type == "Scatter":
        fig = px.scatter(df, x=df.columns[0], y=df.columns[1], trendline="ols")
        st.plotly_chart(fig, use_container_width=True)
    elif chart_type == "Line":
        fig = px.line(df, x=df.columns[0], y=df.columns[1])
        st.plotly_chart(fig, use_container_width=True)
    elif chart_type == "Bar":
        fig = px.bar(df, x=df.columns[0], y=df.columns[1])
        st.plotly_chart(fig, use_container_width=True)
    elif chart_type == "Heatmap":
        fig = px.imshow(df.corr(), text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns([3, 1])

with col2:
    st.subheader("Filters")
    st.slider("Range", 0, 100, (10, 90))
    st.subheader("Parameters")
    st.text("Parameter controls here")
    st.subheader("Data Categories")
    st.text("Categories here")
