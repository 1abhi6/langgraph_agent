import streamlit as st


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == "Basic Chatbot":
            for event in graph.stream({"messages": ("user", user_message)}):
                print("*"*30)
                # print("Event ki value", event.values())
                for value in event.values():
                    # print("*"*30)
                    # print("Value ka message", value["messages"])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        if "messages" in value and value["messages"]:
                            st.write(value["messages"][0].content)
                        else:
                            st.write("No response from assistant.")
                            
                        # st.write(value["messages"][0].content)
