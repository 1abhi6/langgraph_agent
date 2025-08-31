import streamlit as st
import os
from datetime import date
from langchain_core.messages import HumanMessage, AIMessage
from src.langgraph_agent.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}