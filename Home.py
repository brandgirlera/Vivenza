import streamlit as st

# Apply CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Home", layout="wide")
st.title("Dashboard")

# Row 1: 3 panels
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.markdown('<div class="card"><h3>Recent Activity</h3>', unsafe_allow_html=True)
    st.write("Timeline of updates")
    st.markdown('</div>', unsafe_allow_html=True)

with row1_col2:
    st.markdown('<div class="card"><h3>Projects</h3>', unsafe_allow_html=True)
    for i in range(1, 5):
        st.button(f"Project {i}")
    st.markdown('</div>', unsafe_allow_html=True)

with row1_col3:
    st.markdown('<div class="card"><h3>Files & Storage</h3>', unsafe_allow_html=True)
    st.progress(60)
    st.markdown('</div>', unsafe_allow_html=True)

# Row 2: 3 panels
row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.markdown('<div class="card"><h3>Pinned Notes</h3>', unsafe_allow_html=True)
    st.text_area("Notes")
    st.markdown('</div>', unsafe_allow_html=True)

with row2_col2:
    st.markdown('<div class="card"><h3>KPIs</h3>', unsafe_allow_html=True)
    st.metric("Metric A", "21")
    st.metric("Metric B", "45")
    st.metric("Metric C", "10")
    st.markdown('</div>', unsafe_allow_html=True)

with row2_col3:
    st.markdown('<div class="card"><h3>Visualization</h3>', unsafe_allow_html=True)
    st.line_chart([1, 3, 2, 4, 5])
    st.markdown('</div>', unsafe_allow_html=True)
