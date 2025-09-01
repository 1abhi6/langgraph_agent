from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.prompts import ChatPromptTemplate
from src.langgraph_agent.state.state import State
from src.langgraph_agent.nodes.nodes import BasicChatbotNode
import datetime

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
    
    def basic_chatbot_build_graph(self):
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        
    def setup_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
            
        # Compile the graph
        return self.graph_builder.compile()
        
        
