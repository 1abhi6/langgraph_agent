from src.langgraph_agent.state.state import State

class BasicChatbotNode:
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> State:
        return {"messages": [self.llm.invoke(state["messages"])]}


    