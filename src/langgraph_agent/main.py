from src.langgraph_agent.ui.streamlitui.load_ui import LoadStreamlitUI
from src.langgraph_agent.llms.groqllm import GroqLLM
from src.langgraph_agent.graph.graph_builder import GraphBuilder
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
        user_message = st.chat_input("Input your message")
        
    if user_input:
        try:
            # Configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
            
            if not model:
                st.error("LLM could not be initialized!")
                return
            
            # Initalize and setup the graph based on the usecase
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("No usecase selected!")
                return
            
            # Graph Builder
            graph_builder = GraphBuilder(model)
            
            try:
                graph = graph_builder.setup_graph(usecase)
            except Exception as e:
                st.error("Error! Graph setup failed!", e)
                return 

        except Exception as e:
            raise ValueError("Error! Could not initalize LLM", e)
        
        
    