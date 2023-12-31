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
    input_variables = ['title','wikipedia_research'],
    template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia research {wikipedia_research} '
)

# Memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

# Llms
#llm = HuggingFaceHub(
#    repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.9, "max_length": 1000}
#)
llm = OpenAI(temperature=0.9) 

title_chain = LLMChain(llm=llm, prompt=title_template,verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template,verbose=True, output_key='script', memory=script_memory)

wiki = WikipediaAPIWrapper()

# Show stuff to the screen if there's a prompt
if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title)
    st.write(script)

    with st.expander('Title History'):
        st.info(title_memory.buffer)

    with st.expander('Script History'):
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'):
        st.info(wiki_research)
