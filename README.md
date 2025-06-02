# 🤖 Virtual Tuhin Kumar Dutta — Your AI Digital Twin
Welcome to Virtual Tuhin Kumar Dutta, an intelligent Retrieval-Augmented Generation (RAG) chatbot that embodies the digital essence of Tuhin Kumar Dutta. This AI-powered assistant is designed to answer your questions about Tuhin's expertise, background, and digital footprint — bringing his knowledge and persona to life interactively.

## 📌 Overview
In an era where personalized AI is transforming how we connect and consume information, this project offers a sophisticated yet user-friendly chatbot that serves as a virtual extension of Tuhin Kumar Dutta. Combining state-of-the-art NLP models, vector search, and large language models, the chatbot retrieves relevant knowledge dynamically to deliver precise and contextual responses.

## 🚀 Key Features
- **RAG-Based Architecture**: Seamlessly blends document retrieval with generative AI to provide accurate, context-aware answers.
- **Sentence Embeddings**: Utilizes the `all-mpnet-base-v2` model to convert textual knowledge into dense vector representations for efficient semantic search.
- **Vector Database**: Powered by FAISS to perform lightning-fast similarity search on large knowledge bases.
- **Large Language Model**: Integrates the powerful `llama-3.3-70b-versatile` LLM, enabling rich, coherent, and human-like conversations.
- **Streamlit UI**: A sleek, interactive

## ⚙️ Technology Stack
<table>
  <tr>
    <th>Component</th>
    <th>Details</th>
  </tr>
  <tr>
    <td>Embedding Model</td>
    <td>all-mpnet-base-v2 Sentence Transformer</td>
  </tr>
  <tr>
    <td>Vector Database</td>
    <td>FAISS (Facebook AI Similarity Search)</td>
  </tr>
  <tr>
    <td>Language Model</td>
    <td>LLaMA 3.3 70B Versatile</td>
  </tr>
  <tr>
    <td>Frontend UI</td>
    <td>Streamlit App</td>
  </tr>
  <tr>
    <td>Deployment Platform</td>
    <td>Hugging Face Spaces</td>
  </tr>
</table>


## 📤 Key Deployment Highlights
This project is deployed on Hugging Face Spaces using a custom Docker container, enabling complete control over dependencies, performance optimization, and caching.
- **Dockerized Streamlit App**: The application is containerized to ensure consistent behavior across environments and to allow custom configurations not possible in standard Spaces runtime.
- **Base Image and Setup**: Uses the lightweight `python:3.9-slim` image, along with essential build tools and Git to support package compilation and version control.
- **Efficient Caching**: Environment variables such as `HF_HOME`, `TRANSFORMERS_CACHE`, and `SENTENCE_TRANSFORMERS_HOME` are explicitly defined and pointed to a shared cache directory with full read/write permissions to optimize model loading and reduce cold starts.
- **Groq LLM API Integration**: The chatbot utilizes the `LLaMA 3.3 70B Versatile` model served through Groq’s ultra-low-latency inference engine. The Groq API key is securely integrated during runtime, making responses lightning-fast while keeping the deployment architecture lean.
- **Health Monitoring**: A HEALTHCHECK directive pings the Streamlit server to confirm successful boot and uptime — useful for debugging issues within the Hugging Face Space.
- **Port and Entry Point**: The container exposes port `8501`, and the entry point starts the Streamlit app with proper network bindings, making it fully accessible once deployed.

## 🛠️ How It Works
1. **User Query**: The user submits a question via the chatbot interface.
2. **Embedding**: The query is transformed into an embedding vector using all-mpnet-base-v2.
3. **Search**: FAISS searches the vector database for relevant knowledge snippets.
4. **Context Assembly**: Retrieved knowledge is combined with the query.
5. **Generation**: The assembled context is sent to the LLaMA model to generate a natural, context-rich response.
6. **Response Delivery**: The chatbot displays the response to the user in an intuitive conversational style.

## 🧪 Usage
1. Visit [Virtual Tuhin Kumar Dutta](https://virtual.tuhindutta.com/) to interact with the chatbot.
2. Ask any questions related to Tuhin Kumar Dutta’s professional background, expertise, projects, or other related areas.
3. Keep in mind the eco-friendly spirit: minimize unnecessary queries to reduce computational resource consumption.

## 🔮 Future Enhancements
- Integrate multi-modal inputs (voice, images).
- Expand knowledge base dynamically with new documents.
- Optimize inference speed and reduce latency.
- Add user analytics and feedback collection.

## 🤝 Contributing
Contributions and suggestions are welcome! Feel free to open issues or submit pull requests. For more details and updates, visit the [HuggingFace Spaces Repository](https://huggingface.co/spaces/tkdutta/virtual_tkd/tree/main).
