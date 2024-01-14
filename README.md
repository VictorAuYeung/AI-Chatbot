# AI-Chatbot

## Project Description
I created this project as a web application for an AI Chatbot using the Zephyr-7B-β Large-Language-Model, utilizing context and chat session history to provide users a more cohesive and lifelike response.

The model being used, Zephyr-7B-β, is itself a finetuned from the MistralAI/Mistral-7B-v0.1 model. This model is a series of AI language models specifically trained to act as helpful assistants.

For more information: 🦾 [Zephyr-7B-Beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)

In addition, this project allows users to input contexts to generate customized responses. 
The application has been modified to use information from past same-session chats, meaning responses generated will be more cohesive with contextual information, _e.g. using information from a user's previous message._

## How to Launch this Project
**1.** Download app.py into a directory.
   
**2.** Fill in your HuggingFace API Token within the .env file.
   
**3.** Ensure all python modules are installed through pip.
   
**4.** To run, use 'streamlit run app.py' to launch the web application.
   
**5.** Key in context and user input to receive AI responses.

## Examples



## Project Limitations
### 1. Rate Limited Responses
* This project uses HuggingFace's Inference API, meaning all responses are rate-limited. As such, when generating larger responses, text may be cut-off before the LLM can generate the entire, complete response.
* This can be solved by using HuggingFace's Inference Endpoints, or running a pipeline on the local device.

### 2. Faulty Response Generation
* This model may generate incomplete, false or erroneous responses at times.
* This issue is related to the underlying model's limitations, and may be improved upon in the future.

### 3. Unethical/Unfiltered Responses
* The underlying model, Zephyr-7B-β, has not been aligned to human preferences for safety within the RLHF phase or deployed with in-the-loop filtering of responses like ChatGPT. Hence, it can produce harmful/rude/unfiltered responses when prompted to do so.
* This issue is once again related to the underlying model's limitations, and may be improved upon in the future.
