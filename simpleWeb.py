import streamlit as st

st.set_page_config(page_title="simple streamlit website")

page = st.sidebar.radio("Go to" , ["Home", "About", "Contact"])

if page == "Home":
    st.title("Home")
    st.write("Welcome to this simple streamlit website.")

    name = st.text_input("Enter your name:")
    if st.button("Submit"):
        st.write(f"Hello, {name}!!!")

elif page == "About":
    st.title("About")
    st.write("This website is built using **only streamlit**.")

elif page == "Contact":
    st.title("Contact")

    email = st.text_input("Enter your email:")
    message = st.text_area("Enter your message:")

    if st.button("Send"):
        st.write("Message sent!")            