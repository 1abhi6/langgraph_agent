from src.langgraph_agent.ui.streamlitui.load_ui import LoadStreamlitUI
import streamlit as st
import json


# Main function
def load_langgraph_agentic_app():
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error! Failed to input user input from UI")
        return

    # Text input from user
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    # elif st.session_state.IsSDLC:
    #     user_message = st.session_state.state
    else:
        user_input = st.chat_input("Input your message")
