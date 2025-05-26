import streamlit as st
from datetime import datetime
from knowledge_base_utility import GetContext, LLM
# import os
# import csv

# def log_interaction(user_input, ai_response):
#     log_file = "chat_logs.csv"
#     log_exists = os.path.isfile(log_file)
#     with open(log_file, mode="a", newline='', encoding="utf-8") as file:
#         writer = csv.writer(file)
#         if not log_exists:
#             writer.writerow(["timestamp", "user_input", "ai_response"])
#         writer.writerow([datetime.now().isoformat(), user_input, ai_response])

st.set_page_config(page_title="Virtual Tuhin", layout="wide",
                   initial_sidebar_state="expanded",)
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def init_llm():
    with st.spinner("Warming up the AI brain... This might take a few seconds."):
        context = GetContext()
        return LLM(context)

llm = init_llm()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🤖 Tuhin Kumar Dutta: Digitally Reimagined")
st.markdown("""🗨️ *Hi, I’m the virtual version of Tuhin Kumar Dutta — here to answer your questions about me or my areas of expertise! 🌱  
Please use me mindfully — each query consumes energy, so let’s reduce our carbon footprint and make every question count.  
Together, let’s stay curious and go green.*
""")

user_input = st.chat_input("Type your question...")

if user_input:
    with st.spinner("Thinking..."):
        ai_response = llm.query_llm(user_input)
        # log_interaction(user_input, ai_response)
        st.session_state.chat_history.append({
        "user": user_input,
        "ai": ai_response
    })
        

for msg in st.session_state.chat_history:
    st.chat_message("user").write(msg["user"])
    st.chat_message("ai").write(msg["ai"])