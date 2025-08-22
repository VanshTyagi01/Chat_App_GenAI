# for understanding how message can be stored

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

message = [
    SystemMessage(content='You are a helpful Assistant'),
    HumanMessage(content='Tell me about langchain')
]
result = model.invoke(message)

message.append(AIMessage(content=result.content))
print(message)