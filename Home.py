import streamlit as st

# Apply custom CSS for global styling
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Home", layout="wide")
st.title("Command Center")

# Available widgets
widgets = ["Recent Activity", "Project Grid", "KPI Summary", "Storage Summary", "Notes"]
selected = st.multiselect("Customize Dashboard", widgets, default=widgets)

# Layout columns
col1, col2, col3 = st.columns([1, 2, 1])

# Recent Activity
if "Recent Activity" in selected:
    with col1:
        st.markdown('<div class="card"><h3>Recent Activity</h3>', unsafe_allow_html=True)
        st.write("Timeline of updates")
        st.markdown('</div>', unsafe_allow_html=True)

# Notes
if "Notes" in selected:
    with col1:
        st.markdown('<div class="card"><h3>Pinned Notes</h3>', unsafe_allow_html=True)
        st.text_area("Notes")
        st.markdown('</div>', unsafe_allow_html=True)

# Project Grid
if "Project Grid" in selected:
    with col2:
        st.markdown('<div class="card"><h3>Projects</h3>', unsafe_allow_html=True)
        for i in range(9):
            st.button(f"Project {i+1}")
        st.markdown('</div>', unsafe_allow_html=True)

# Files & Storage
if "Storage Summary" in selected:
    with col3:
        st.markdown('<div class="card"><h3>Files & Storage</h3>', unsafe_allow_html=True)
        st.progress(60)
        st.markdown('</div>', unsafe_allow_html=True)

# KPIs
if "KPI Summary" in selected:
    with col3:
        st.markdown('<div class="card"><h3>KPIs</h3>', unsafe_allow_html=True)
        st.metric("Metric A", "21")
        st.metric("Metric B", "45")
        st.markdown('</div>', unsafe_allow_html=True)
