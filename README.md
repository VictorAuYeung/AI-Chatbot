# AI-Chatbot (Contextual Text Generation)

## Project Description
I created this personal project by implementing an AI chat bot using the Zephyr-7B-β Large-Language-Model, and utilizing context and chat session history to hold more lifelike conversations. It has a simple UI and mimics conversational AI models like ChatGPT, but trades extensive training for a more optimized performance.

The model being used, Zephyr-7B-β, is itself a finetuned from the MistralAI/Mistral-7B-v0.1 model. This model is a series of AI language models specifically trained to act as helpful assistants.

For more information: 🦾 [Zephyr-7B-Beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)

In addition, this project allows users to input contexts to generate customized responses. 
The application has been modified to use information from past same-session chats, meaning responses generated will be more cohesive with contextual information, _e.g. using information from a user's previous message._

The user interface is made using StreamLit. All code logic is stored in _app.py_.

<a href="https://huggingface.co/spaces/victorauyeungxf/AI-Chatbot-Zephyr7b" target="_blank">
  <img src="https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/ad5c3033-3a33-4297-9aad-f6a4444c5edf" alt="Try it on HuggingFace Spaces" width="170">
</a>

This project is also hosted on HuggingFace Spaces. To try the [live demo](https://huggingface.co/spaces/victorauyeungxf/AI-Chatbot-Zephyr7b), click the button above.

## 1. Main User Interface
![image](https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/f5e0451a-dcfa-4df3-bbbe-0b6da9938ef7)

## How to Launch this Project on Your Own
**1.** Download _app.py_ into your directory.
   
**2.** Create a _.env_ file in the same directory, and add in your HuggingFace API Token using ```HUGGINGFACEHUB_API_TOKEN = ""```.
   
**3.** Ensure all required python modules are correctly installed through pip.
   
**4.** To run, use **'streamlit run app.py'** to launch the web application.
   
**5.** On the UI, key in the optional context and user query, to receive AI responses.

## Example Prompt 1
![image](https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/01cbddbe-8ffd-4a64-a547-ed38575ebc39)
* This is a normal prompt, expecting a normal, one message response.<br>
## Example Prompt 2
![image](https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/a8fe53e9-2c84-4535-9a6d-a1f6af4fddaf)
* This prompt uses the session chat feature, which allows the chat bot to return responses based on **past chat messages**. <br>
## Example Prompt 3
![image](https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/6b72d0e0-703b-4e68-b166-267c2f6f9e93)
* This prompt expects a response that has **indentations**, e.g. Tips, instructions, checklist, etc. <br>
## Example Prompt 4
![image](https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/832548c7-599a-43ff-b7c8-4b6a7a8d1caa)
* This prompt expects a response that has **line breaks**, e.g. song lyrics, poems, stories, etc. <br>

## Some Background Logic
<img src="https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/25895589-5036-4e2a-9bd2-cfc20b1ef868" width="90%"/>
<br>
* This system can definitely be improved upon, but serves as a basis for the continuation of AI conversations.
<br>


## Project Benefits
There are some benefits of using a pre-trained LLM model, as well as implementing chat history and contextual input features.
### 1. Fast Performance
* This project uses HuggingFace's Inference API, as well as a less intensive 7b model. Hence, response generation is relatively quick and inexpensive, and may be suitable for most end-users. (e.g. website support, knowledgebase support, ticket support etc.)

### 2. Relatively Lifelike Responses
* Since this project implements context and historical messsages to develop its response output, conversations will feel relatively more coherent overall. It can hold full length conversations, answer queries and assist in most chat requests.

### 3. Dynamic Use Cases
* This project has alot of potential to be adapted into a variety of use cases, with an easy-to-understand user interface for most end-users. Possible use cases include (and are not limited to) creating custom character personality AI (with context), virtual conversational companionship (with session responses) and query/data manipulation (using the extensive text generation model).

## Limitations
These limitations are usually present in most AI models and are not a cause of concern for this project, of which the aim is to create a helpful, easy-to-use chatbot with contextual capabilities.
### 1. Rate-Limiting
* This project uses HuggingFace's Inference API, meaning all responses are rate-limited. As such, when generating larger responses, text may be cut-off before the LLM can generate the entire, complete response.
* This can be solved by using HuggingFace's Inference Endpoints, or running a pipeline on the local device.

### 2. Response Generation
* This model may generate incomplete, false or erroneous responses at times.
* This issue is related to the underlying model's limitations, and may be improved upon in the future.

### 3. Potential Ethical Concerns
* The underlying model, Zephyr-7B-β, has not been aligned to human preferences for safety within the RLHF phase or deployed with in-the-loop filtering of responses like ChatGPT. Hence, it can produce harmful/rude/unfiltered responses especially when prompted to do so.
* This issue is once again related to the underlying model's limitations, and may be improved upon in the future.

