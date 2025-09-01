from langchain_groq import ChatGroq
import streamlit as st
import os


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            # Get API key from UI input or env var
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "").strip()
            env_api_key = os.getenv("GROQ_API_KEY", "").strip()
            selected_groq_model = self.user_controls_input.get("selected_groq_model_option", "").strip()

            # Decide which key to use
            final_api_key = groq_api_key if groq_api_key else env_api_key

            if not final_api_key:
                st.error("Please provide a Groq API Key (via UI or environment variable).")
                return None  # prevent UnboundLocalError

            if not selected_groq_model:
                st.error("Please select a Groq model.")
                return None

            # Create the model
            llm = ChatGroq(api_key=final_api_key, model=selected_groq_model)
            return llm

        except Exception as e:
            raise ValueError(f"Error occurred while loading Groq LLM: {e}")
