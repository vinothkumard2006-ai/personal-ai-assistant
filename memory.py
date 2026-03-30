from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

def get_memory():
    return memory