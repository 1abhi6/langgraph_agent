from langchain_community.tools import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns the list of Tool
    """
    
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    
    """Gets and returns tools"""
    
    return ToolNode(tools=tools)