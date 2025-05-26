from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os
import requests
import datetime

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set")


class GetContext():

    def __init__(self):
        knowledge_base_dir = './knowledge_base_data'
        self.__embedding_model = SentenceTransformer('all-mpnet-base-v2')
        self.__index = faiss.read_index(os.path.join(knowledge_base_dir, "knowledge_index.faiss"))
        with open(os.path.join(knowledge_base_dir, "knowledge_texts.pkl"), "rb") as f:
            self.__knowledge_chunks = pickle.load(f)
        self.k = 5

    def retrieve_relevant_chunks(self, query):
        query_embedding = self.__embedding_model.encode([query], convert_to_numpy=True)
        distances, indices = self.__index.search(query_embedding, self.k)
        retrieved_texts = [self.__knowledge_chunks[i].strip() for i in indices[0]]
        return '\n\n'.join(retrieved_texts)




class LLM:

    def __init__(self, context:GetContext):
        self.__context = context

    def build_prompt(self, user_input, formatted_chat_history=''):
        today_date = str(datetime.datetime.now().strftime('%B %d, %Y'))
        formatted_chat_history = formatted_chat_history+'\n\n' if formatted_chat_history!='' else formatted_chat_history
        context_text = self.__context.retrieve_relevant_chunks(user_input)
        system_prompt = f"""You are Virtual Tuhin Kumar Dutta — a helpful, knowledgeable AI representation of Tuhin Kumar Dutta. 
Answer user questions clearly, concisely, and professionally. Do not exaggerate or fabricate any information regarding Tuhin Kumar Dutta.
If the context does not provide sufficient information to answer a question about Tuhin Kumar Dutta, respond with "I don't have enough information to answer that.".
You may answer unrelated questions only if you are confident in your response.
Date: {today_date}
Use the following context to answer queries:

{context_text}
"""
        messages = [{"role": "system", "content": system_prompt}]
        # messages.append({'history': chat_history})
        messages.append({"role": "user", "content": formatted_chat_history + user_input})
        return messages

    def query_llm(self, user_input, formatted_chat_history=''):
        url = "https://api.groq.com/openai/v1/chat/completions"
        messages = self.build_prompt(user_input, formatted_chat_history)
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }       
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": messages,
            "temperature": 0.3,
            # "max_tokens": 800          
        }
        response = requests.post(url, headers=headers, json=payload)
        output = response.json()['choices'][0]['message']['content'].strip()
        return output