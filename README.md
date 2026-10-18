# 📰 AI News Summarizer – Agentic AI

An AI-powered news exploration and summarization application built using **Python, Streamlit, LangChain, LangGraph, and Large Language Models (LLMs)**.

The application helps users explore the latest AI news based on selected time frames and uses AI-powered workflows to generate useful summaries.

## 🚀 Project Overview

The AI News Summarizer is designed to simplify the process of keeping up with the latest developments in Artificial Intelligence.

Instead of manually reading multiple news articles, users can fetch recent AI-related news and use an LLM-powered workflow to understand important information more efficiently.

The application provides an interactive interface through Streamlit and integrates news retrieval and LLM capabilities.

## ✨ Key Features

- **AI News Explorer:** Explore the latest Artificial Intelligence news.
- **News Retrieval:** Fetch relevant news using Tavily Search API.
- **LLM Integration:** Connect with Groq and OpenAI integrations.
- **Model Selection:** Select an available LLM and model.
- **Time Frame Selection:** Choose a time frame such as Weekly.
- **AI-Powered Summarization:** Use LLMs to generate meaningful news summaries.
- **Interactive Interface:** User-friendly application developed with Streamlit.
- **Agentic AI Architecture:** Use LangGraph to structure stateful AI workflows.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | User interface |
| LangChain | LLM integration and application components |
| LangGraph | Stateful agentic AI workflows |
| Groq | LLM inference |
| OpenAI | LLM integration |
| Tavily | AI-powered news search |
| FAISS | Vector similarity search |

## 🏗️ Project Architecture

```text
             User
               |
               v
       Streamlit Interface
               |
               v
       Select LLM & Model
               |
               v
        Select Use Case
               |
               v
         AI News Explorer
               |
               v
        Tavily Search API
               |
               v
        Retrieve News Data
               |
               v
          LangGraph
       Agentic AI Workflow
               |
               v
          LangChain
               |
               v
        Groq / OpenAI LLM
               |
               v
       Generate News Summary
               |
               v
       Display Results in UI
```

*Note: This is a high-level conceptual architecture; the exact node structure depends on the implementation in the `src` directory.*

## 📂 Project Structure

```text
AI_News_Summarizer/
│
├── src/
│   └── langgraphagenticai/
│       └── ...
│
├── AINews/
│   └── ...
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sukreetdas/AI_News_Summarizer.git
```

### 2. Navigate to the Project Directory

```bash
cd AI_News_Summarizer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API Keys

The application requires API keys for the services enabled in the application.

- **Groq API Key:** Obtain it from https://console.groq.com/
- **Tavily API Key:** Obtain it from https://app.tavily.com/
- **OpenAI API Key:** Obtain it from https://platform.openai.com/api-keys/ if using the OpenAI integration.

Never upload API keys or other confidential credentials to GitHub.

### 7. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🖥️ Application Workflow

1. Launch the Streamlit application.
2. Select the desired LLM provider.
3. Select an available model.
4. Enter the required API key.
5. Select the AI News use case.
6. Enter the Tavily API key.
7. Select the desired news time frame.
8. Click **Fetch Latest AI News**.
9. View the retrieved news and AI-generated results.

## 🔐 Security

- Keep API keys confidential.
- Never commit API keys to GitHub.
- Use Streamlit Secrets or environment variables for server-side credentials.
- Add sensitive configuration files to `.gitignore`.

## 🌐 Deployment

The application can be deployed using Streamlit Community Cloud.

Deployment involves connecting the GitHub repository, selecting the application entry point (`app.py`), configuring the required dependencies, and securely setting the necessary API keys.

## 🎯 Project Objective

The main objective of this project is to explore how Agentic AI, Large Language Models, LangChain, and LangGraph can be combined to build an interactive AI-powered news exploration and summarization application.

## 👨‍💻 Author

**Sukreet Das**

GitHub: https://github.com/sukreetdas

---

⭐ If you find this project interesting, consider giving the repository a star!
