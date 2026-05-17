
# Stdio-AI

Stdio-AI is an intuitive, web-based AI workstation built on **Streamlit**. It acts as a bridge between powerful Large Language Models (LLMs) and local environments, offering a rich UI to monitor, test, and interact with AI workflows, autonomous data pipelines, or Model Context Protocol (MCP) toolkits.

By utilizing Streamlit, **Stdio-AI** transforms raw standard input/output streams into dynamic, user-friendly dashboards, execution logs, and conversational playgrounds.

## 🚀 Features

- **Interactive UI/UX:** Built entirely with Streamlit for clean, responsive, and real-time visualization of AI operations.
- **Session State Tracking:** Seamlessly manage prompt history, chat contexts, and intermediate agent reasoning states.
- **Live Stream Monitoring:** Inspect payload data, token usage, or back-and-forth tool parameters directly in the web UI.
- **Plug-and-Play Configuration:** Easily adjust system prompts, model endpoints, and API parameters via a reactive sidebar dashboard.

## 📦 Prerequisites

Before running the application, make sure you have the following installed:

- **Python:** `python 3.10+`
- **Package Manager:** `pip`

## 🔧 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Rhythamtech/Stdio-AI.git
   cd Stdio-AI

```

2. **Set Up a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install Dependencies:**
Make sure you install `streamlit` alongside any model connectors or helper libraries:
```bash
pip install -r requirements.txt

```


4. **Environment Variables:**
If your application uses specific API keys (such as OpenAI, Anthropic, or local LLM endpoints), create a `.env` file or configure a local Streamlit secret file (`.streamlit/secrets.toml`):
```env
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here

```



## 🛠 Usage & Execution

To launch the web interface locally, execute the standard Streamlit run command:

```bash
streamlit run app.py

```

*(Replace `app.py` with your repository's primary entrypoint file if named differently, e.g., `main.py`).*

Once executed, your browser will automatically open the interface at:
👉 **`http://localhost:8501`**

## 📂 Project Structure

```text
├── .streamlit/          # Streamlit specific configurations (themes, secrets)
├── assets/              # UI components, images, or styling resources
├── src/                 # Main logic modules (agent loops, RAG pipelines, or utilities)
├── app.py               # The main Streamlit entrypoint file
├── requirements.txt     # Python package dependencies
└── README.md            # Project documentation

```

## 🤝 Contributing

Contributions are welcome! If you want to enhance the UI, optimize component states, or add new features:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingUIFeature`).
3. Commit your Changes (`git commit -m 'Add some UI component'`).
4. Push to the Branch (`git push origin feature/AmazingUIFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
