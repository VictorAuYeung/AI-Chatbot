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
### 1. Main User Interface
![image](https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/f5e0451a-dcfa-4df3-bbbe-0b6da9938ef7)



### 2. Example Questions


| Example | Normal Responses                    | Session Based Responses             |
| - | ----------------------------------- | ----------------------------------- |
| **Example #1** | ![image](https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/01cbddbe-8ffd-4a64-a547-ed38575ebc39) | ![image](https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/a8fe53e9-2c84-4535-9a6d-a1f6af4fddaf) |
| **Example #2** | ![image](https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/6b72d0e0-703b-4e68-b166-267c2f6f9e93) | ![image](https://github.com/VictorAuYeung/AI-Chatbot/assets/69711600/832548c7-599a-43ff-b7c8-4b6a7a8d1caa) |

## Benefits
### 1. Fast Performance
* This project uses HuggingFace's Inference API, as well as a less intensive 7b model. Hence, response generation is relatively quick and inexpensive, and may be suitable for the average user requesting support. (e.g. website support, knowledgebase support etc.)

### 2. Lifelike Responses
* Since this project implements context and historical messsages to create its response output, responses will feel relatively more cohesive overall. It can hold conversations, answer queries and assist in simple chat requests.

### 3. Dynamic Use Cases
* This project can be adapted to be used in a variety of cases, with an easy-to-understand user interface for most end-users to utilize. Possible use cases include creating custom character personality AI (with context), virtual texting communication (with session responses) and simple query answering.

## Limitations
### 1. Rate-Limiting
* This project uses HuggingFace's Inference API, meaning all responses are rate-limited. As such, when generating larger responses, text may be cut-off before the LLM can generate the entire, complete response.
* This can be solved by using HuggingFace's Inference Endpoints, or running a pipeline on the local device.

### 2. Response Generation
* This model may generate incomplete, false or erroneous responses at times.
* This issue is related to the underlying model's limitations, and may be improved upon in the future.

### 3. Ethical Concerns
* The underlying model, Zephyr-7B-β, has not been aligned to human preferences for safety within the RLHF phase or deployed with in-the-loop filtering of responses like ChatGPT. Hence, it can produce harmful/rude/unfiltered responses especially when prompted to do so.
* This issue is once again related to the underlying model's limitations, and may be improved upon in the future.
