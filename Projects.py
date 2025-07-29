import streamlit as st

# Apply CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Projects", layout="wide")
st.title("Projects")

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("All Projects")
    for i in range(12):
        st.button(f"Project {i+1}")

with col2:
    st.subheader("Upload Files")
    st.file_uploader("Upload CSV", type=["csv"])
    st.subheader("Storage")
    st.progress(40)
    st.subheader("KPIs")
    st.metric("Active", 21)
    st.metric("Pending", 45)
