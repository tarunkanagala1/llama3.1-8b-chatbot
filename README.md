
# Llama 3.1 Model Chatbot on Local Machine

A simple way to interact with the latest Llama 3.1 with 8b/70b/405b parameters model on a local machine without Internet fully remotely.

Can be used for learning, experimenting in your home cluster,etc.

Made by using LangChain , Ollama and Streamlit.

All links are provided for downloading, installing the model.



## Installation
pip install -r requirements.txt

Install all the requirement packages.

Download Ollama from https://ollama.com/

Go to https://ollama.com/library/llama3.1 and choose the model as per your constraints.

Install Ollama and run it.

Open a cmd or terminal and 

To download any model using Ollama use

Ollama pull model_name (it will be downloaded in your local drive.)




```bash
 To download the model
 ollama pull model_name

To run the model
 ollama run model_name
```
 ```bash
 To run the script 
streamlit run file_name
```


## Preferences

To change upto the preferences make changes in 

llm=Ollama(model="llama3.1:latest") # for base 8b model.
llm=Ollama(model="llama3.1:70b")  for 70b model.
llm=Ollama(model="llama3.1:405b") for 405b model.
