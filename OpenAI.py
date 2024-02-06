import streamlit as st
import os
from openai import OpenAI
# print(st.secrets['api_key'], "!!!여기보세요!!!")

os.environ['OPENAI_API_KEY'] = st.secrets['api_key']
# st.write(os.environ['OPENAI_API_KEY'])
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

st.title("이미지 생성기입니다.")

with st.form("form"):
    user_input = st.text_input("그리고싶은 그림은?")
    size = st.selectbox("size",['1024x1024','512x512','256x256'])
    submit =st.form_submit_button("Submit")

if submit and user_input:


# 입력받는 곳
# st.button("클릭")
# user_input = "오동나무"

gpt_prompt = [{
    "role":"system",
    "content":"Imagine the detail appeareance of the input.Response it shortly around 15 words",
}]

gpt_prompt.append(
    {
    "role":"user",
    "content": user_input})
with st.spinner("Waiting for ChatGPT ..."):
    gpt_response = client.chat.completions.create(
        model= "gpt-3.5-turbo",
        messages= gpt_prompt
    )

    dalle_prompt = gpt_response.choices[0].message.content
    st.write("dall-e prompt:",)

with st.spinner("Waiting for ChatGPT ..."):
    dalle_response = client.images.generate(
        model='dall-e-2',
        prompt = dalle_prompt,
        size = '1024x1024'
    )
# print(gpt_response.choices[0].message.content)
# st.write(gpt_prompt)  
    st.image(dalle_response.data[0].url)