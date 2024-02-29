import streamlit as st
import pickle


vectortest = pickle.load(open('Notebook/vector.pkl','rb'))
modeltest = pickle.load(open('Notebook/model2.pkl','rb'))

st.set_page_config(page_title="Email Spam Classifier")


st.title("Email Spam Classifier")

input_sms = st.text_area("Enter your email message here and identify is it Sam or Ham")

if st.button('Predict'):

    # 1. vectorize
    vector_input = vectortest.transform([input_sms])
    # 2. predict
    result = modeltest.predict(vector_input)[0]
    # 3. Display Result
    if result == "spam":
        st.header("Spam")
    else:
        st.header("Not Spam")