from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
    # differ from prompt template (below is wrong)
    # SystemMessage(content="you are a helpful {domain} expert"),
    # HumanMessage(content="Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'Dusra'})

print(prompt)