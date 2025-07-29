import streamlit as st

# Apply custom CSS for styling
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Home", layout="wide")
st.title("Command Center")

# Widget selector
widgets = ["Recent Activity", "Project Grid", "KPI Summary", "Storage Summary", "Notes"]
selected = st.multiselect("Customize Dashboard", widgets, default=widgets)

# Layout: 3 columns
col1, col2, col3 = st.columns([1, 2, 1])

if "Recent Activity" in selected:
    with col1:
        st.subheader("Recent Activity")
        st.write("Timeline of updates")

if "Notes" in selected:
    with col1:
        st.subheader("Pinned Notes")
        st.text_area("Notes")

if "Project Grid" in selected:
    with col2:
        st.subheader("Projects")
        for i in range(9):
            st.button(f"Project {i+1}")

if "Storage Summary" in selected:
    with col3:
        st.subheader("Files & Storage")
        st.progress(60)

if "KPI Summary" in selected:
    with col3:
        st.subheader("KPIs")
        st.metric("Metric A", "21")
        st.metric("Metric B", "45")
