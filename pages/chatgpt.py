import openai
import streamlit as st

openai.api_key = "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"

def get_assistant_response(messages):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    return assistant_content

st.title("GPT-3 Chatbot")
st.write("Please type your message below:")

user_input = st.text_input("User : ")

if st.button("Send"):
    messages = [{"role": "user", "content": f"{user_input}"}]
    assistant_response = get_assistant_response(messages)
    st.write(f"GPT : {assistant_response}")
