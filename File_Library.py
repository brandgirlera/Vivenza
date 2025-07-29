import streamlit as st

# Apply CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="File Library", layout="wide")
st.title("File Library")

st.text_input("Search files")
cols = st.columns(4)
for i in range(12):
    with cols[i % 4]:
        st.button(f"File {i+1}")
