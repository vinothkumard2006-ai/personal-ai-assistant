from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from tools import search_tool, calculator_tool
from memory import get_memory
from config import OPENAI_API_KEY

llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7
)

tools = [
    Tool(name="Search", func=search_tool, description="Search info from Wikipedia"),
    Tool(name="Calculator", func=calculator_tool, description="Do math calculations")
]

agent = initialize_agent(
    tools,
    llm,
    agent="conversational-react-description",
    memory=get_memory(),
    verbose=True
)

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    response = agent.run(user)
    print("AI:", response)