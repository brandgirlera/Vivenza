import streamlit as st

# Apply global styling
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Home", layout="wide")

# --- Custom Header with Navigation ---
st.markdown("""
    <div class="custom-header">
        <form action="?page=Home" method="get"><button>Home</button></form>
        <form action="?page=Projects" method="get"><button>Projects</button></form>
        <form action="?page=Project_Detail" method="get"><button>Project Detail</button></form>
        <form action="?page=File_Library" method="get"><button>File Library</button></form>
        <form action="?page=Insights" method="get"><button>Insights</button></form>
    </div>
""", unsafe_allow_html=True)

# --- Handle page navigation ---
params = st.query_params()
if "page" in params:
    target = params["page"][0]
    if target != "Home":
        st.switch_page(f"{target}.py")

# --- Page Content ---
st.title("Dashboard")

# Row 1
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card"><h3>Recent Activity</h3>', unsafe_allow_html=True)
    st.write("Timeline of updates")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><h3>Projects</h3>', unsafe_allow_html=True)
    for i in range(1, 5):
        st.button(f"Project {i}")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card"><h3>Files & Storage</h3>', unsafe_allow_html=True)
    st.progress(60)
    st.markdown('</div>', unsafe_allow_html=True)

# Row 2
c4, c5, c6 = st.columns(3)

with c4:
    st.markdown('<div class="card"><h3>Pinned Notes</h3>', unsafe_allow_html=True)
    st.text_area("Notes")
    st.markdown('</div>', unsafe_allow_html=True)

with c5:
    st.markdown('<div class="card"><h3>KPIs</h3>', unsafe_allow_html=True)
    st.metric("Metric A", "21")
    st.metric("Metric B", "45")
    st.metric("Metric C", "10")
    st.markdown('</div>', unsafe_allow_html=True)

with c6:
    st.markdown('<div class="card"><h3>Visualization</h3>', unsafe_allow_html=True)
    st.line_chart([1, 3, 2, 4, 5])
    st.markdown('</div>', unsafe_allow_html=True)

# --- Custom Footer ---
st.markdown("""
    <div class="custom-footer">
        Vivenza © 2025
    </div>
""", unsafe_allow_html=True)
