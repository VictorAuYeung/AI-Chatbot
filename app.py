from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import requests
import os
import streamlit as st

load_dotenv(find_dotenv());
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def text2text(context, text):
    API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
	
    output = query(
        {
            "inputs": "<|system|>\n" + context + "\n</s>\n" + text + "\n<|assistant|>"}
    )

    #print(output[0])
    output_str = output[0]['generated_text']
    #print(output_str)
    last_response = output_str.rfind("<|assistant|>")

    output_text = output_str[last_response + 13:]
    #print(output_text)
    output_text = output_text.replace('\n', '  \n')
    #print(output_text)
    return output_text

def main():
     st.set_page_config(page_title="Context Chatbot @VictorAuYeung", page_icon="🤖")

     st.header("Large-Language-Model Chatbot App")
     st.markdown("Project created by: 🔗[Victor Au Yeung](https://github.com/VictorAuYeung)  \nModel used: 🦾[Zephyr-7B-Beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)")
     st.markdown("##### Description: ")
     st.markdown("This chatbot uses an LLM that takes a simple context and answers user queries within the specified context. It has also been adapted to use past details and messages from the same chat session history, such as models like GPT.")
     st.markdown("(__Note: Responses utilize HuggingFace Inference API, are rate-limited and may be incomplete.__)")
     
     context = st.text_area('What is the context for the AI? *(Optional)*', placeholder='You are a helpful chatbot that will respond like a pirate.')

     # Initialize chat history
     if "messages" not in st.session_state:
        st.session_state.messages = []

     # Display chat messages from history on app rerun
     for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

     user_input = st.chat_input('What would you like to say to the AI?')

     
     # Once user has sent input
     if user_input:
        prev_input = ''
        #print(len(st.session_state.messages))
        for message in st.session_state.messages:
            
            #print(message)
            if (message['role'] == 'user'):
                prev_input += '<|user|>\n' + message['content'] + '\n</s>'
                #print(message['content'])
            
        
            elif (message['role'] == 'assistant'):
                prev_input += '<|assistant|>\n' + message['content'] + '\n</s>'
                #print(message['content'])
            
        # Combine user input with chat history, e.g. previous inputs
        prev_input += '<|user|>\n' + user_input + '\n</s>\n'
        print(prev_input)
        output = text2text(context, prev_input)


        # Add user responses to chat history
        with st.chat_message("user"):
            st.markdown(user_input)

        st.session_state.messages.append({"role": "user", "content": user_input})

        # Add assistant response to chat history
        with st.chat_message("assistant"):
            st.markdown(output)
        
        st.session_state.messages.append({"role": "assistant", "content": output})


if __name__ == '__main__':
      main()
