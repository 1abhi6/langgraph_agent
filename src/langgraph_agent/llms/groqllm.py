from langchain_groq import ChatGroq
import streamlit as st
import os


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            # Get API key from UI input or env var
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "Nahi aaya API Key Mere paas").strip()
            # env_api_key = os.getenv("GROQ_API_KEY", "").strip()
            selected_groq_model = self.user_controls_input.get("selected_groq_model_option", "Nhi hai mere paas bhi API key").strip()

            # Decide which key to use
            # final_api_key = groq_api_key if groq_api_key else env_api_key
            print("Yahi API Mila muje dekh lo: ", groq_api_key)

            if not groq_api_key:
                st.error("Please provide a Groq API Key (via UI or environment variable).")
                return "Nhi aaya bhai API mere paas to None hi return karuga na"  # prevent UnboundLocalError

            if not selected_groq_model:
                st.error("Please select a Groq model.")
                return None

            # Create the model
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
            return llm

        except Exception as e:
            raise ValueError(f"Error occurred while loading Groq LLM: {e}")
