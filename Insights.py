import streamlit as st

# Apply CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Insights", layout="wide")
st.title("Insights")

st.subheader("Add Widgets")
st.multiselect("Choose components", ["KPIs", "Scatter", "Line", "Bar"])

col1, col2 = st.columns([2, 1])
with col1:
    st.text("Charts go here...")
with col2:
    st.text("KPIs go here...")
