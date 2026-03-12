from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(model='openrouter/hunter-alpha',openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1")

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])
chat_history= []

with open('message.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompts

#prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund?'})

#result = model.invoke(prompt)

chain = chat_template | model
result = chain.invoke({
    'chat_history':chat_history, 
    'query':'Where is my refund?'
})
print(result.content)