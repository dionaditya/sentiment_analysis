from streamlit.web import cli as stcli
from streamlit import runtime
import streamlit as st
import sys
import requests

def main():
    st.title("Sentiment Analysis App")

    # Input text from the user
    text = st.text_area("Enter text to analyze", "")

    if st.button("Analyze Sentiment"):
        if text:
        # Send the text to the Flask API
            response = requests.post('http://127.0.0.1:5000/predict', json={'text': text})
        
        if response.status_code == 200:
            sentiment = response.json().get('sentiment')
            st.write(f"The sentiment of the text is: {sentiment}")
        else:
            st.write("Error in prediction: " + response.json().get('error', 'Unknown error'))
    else:
        st.write("Please enter some text to analyze")

if __name__ == '__main__':
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())