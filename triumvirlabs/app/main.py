import os
import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    secret_message = os.getenv("MY_SECRET_MESSAGE", "ERROR!!!!")
    st.title("Triumvir Labs")
    if st.button("Health Test"):
        st.write(secret_message)


if __name__ == "__main__":
    main()