import streamlit as st

# Apply CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Projects", layout="wide")

# --- Custom Header ---
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
params = st.query_params
if "page" in params:
    target = params["page"]
    if target != "Projects":
        st.switch_page(f"{target}.py")

# --- State: project list ---
if "projects" not in st.session_state:
    st.session_state.projects = []

st.title("Projects")

# Place everything inside a single card
st.markdown('<div class="card">', unsafe_allow_html=True)

# --- Empty state ---
if len(st.session_state.projects) == 0:
    st.subheader("No projects available")
    st.write("Click the button below to create your first project.")
    if st.button("Create New Project"):
        st.session_state.projects.append("Project 1")
        st.experimental_rerun()

# --- If projects exist ---
else:
    if st.button("Create New Project"):
        new_name = f"Project {len(st.session_state.projects)+1}"
        st.session_state.projects.append(new_name)
        st.experimental_rerun()

    st.subheader("Your Projects")

    cols = st.columns(3)
    for idx, proj in enumerate(st.session_state.projects):
        with cols[idx % 3]:
            st.markdown(f'<div class="card"><h3>{proj}</h3>', unsafe_allow_html=True)
            if st.button(f"Open {proj}", key=f"btn_{proj}"):
                st.query_params.update({"page": "Project_Detail", "project": proj})
                st.switch_page("Project_Detail.py")
            st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div class="custom-footer">
        Vivenza © 2025
    </div>
""", unsafe_allow_html=True)
