from src.langgraph_agent.state.state import State

class ChatbotWithToolNode:
    def __init__(self, model):
        self.model = model

    def process(self, state: State):
        user_input = state["messages"] if state["messages"] else ""
        llm_response = self.model.invoke([{"role": "user", "content": user_input}])
        
        tools_response = f"Tool Integration for {user_input}"

        return {"messages": [llm_response, tools_response]}

    
    def create_chatbot(self, tools):
        """Returns a chatbot node function"""
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node
            