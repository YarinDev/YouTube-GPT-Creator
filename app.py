# Bring in dependencies
import os
from apikey import apikey

# Bring in Streamlit 
import streamlit as st

# Bring in Langchain modules
from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper


#HUGGINGFACEHUB_API_TOKEN = apikey
#//os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('🦜️🔗 YouTube GPT Creator')
prompt = st.text_input('Enter a prompt for the AI to complete:')

# Prompt templates

title_template = PromptTemplate(
    input_variables = ['topic'],
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template='write me a youtube video script based on this title TITLE: {title}'
)

# Memory
memory = ConversationBufferMemory(input_key='topic', output_key='chat history')

# Llms
#llm = HuggingFaceHub(
#    repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.9, "max_length": 1000}
#)
llm = OpenAI(temperature=0.9) 

title_chain = LLMChain(llm=llm, prompt=title_template,verbose=True, output_key='title')
script_chain = LLMChain(llm=llm, prompt=script_template,verbose=True, output_key='script')
sequantial_chain = SequentialChain(chains=[title_chain,script_chain],input_variables=['topic'], verbose=True, output_variables=['title','script'])

# Show stuff to the screen if there's a prompt
if prompt:
    response = sequantial_chain({'topic':prompt})
    st.write(response['title'])
    st.write(response['script'])
