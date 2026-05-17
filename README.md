
# Stdio-AI

Stdio-AI is a lightweight, efficient interface designed to connect large language models (LLMs) and AI agents directly to local environments using standard input/output (`stdio`) streams. Operating via JSON-RPC or newline-delimited stream communication, it enables seamless execution of local system tools, file operations, and context injection for AI workflows without the overhead of heavy HTTP or WebSocket servers.

Optimized for integration with Model Context Protocol (MCP) clients like Claude Desktop, Cursor, and custom agent architectures.

## 🚀 Features

- **Stdio Transport Layer:** Direct, low-latency communication over `stdin` and `stdout` using asynchronous streams.
- **Robust Error Handling:** Intercepts system exceptions and routes internal logs safely to `stderr` to keep the standard output line clean for data exchange.
- **Agent Interactivity:** Enables external LLMs to execute structural tools, search local directories, and run system tasks.
- **Secure & Lightweight:** Zero-dependency or light footprint execution designed to be run locally or via container environments.

## 📦 Prerequisites

Ensure you have the required runtime environment set up based on your project configuration:

- **Python:** `python 3.10+`
- **Node.js:** `node 18+` (if utilizing npm/npx wrappers)

## 🔧 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Rhythamtech/Stdio-AI.git](https://github.com/Rhythamtech/Stdio-AI.git)
   cd Stdio-AI

```

2. **Environment Configuration:**
Depending on your underlying architecture, install dependencies:
*For Python backends:*
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

```


*For Node.js backends:*
```bash
npm install

```



## 🛠 Usage & Integration

### Running the Server Locally

To spin up the `stdio` communication loop directly from your command line:

```bash
python main.py
# or if using Node/TypeScript
npm start

```

### Integrating with Claude Desktop / Cursor (MCP Config)

To connect **Stdio-AI** as a local tool provider for development agents, add the server execution command to your local configuration file (e.g., `mcp.json` or your client configuration):

```json
{
  "mcpServers": {
    "stdio-ai": {
      "command": "python",
      "args": ["/absolute/path/to/Stdio-AI/main.py"],
      "env": {
        "DEBUG": "true"
      }
    }
  }
}

```

## 📊 Communication Protocol

This project follows strict input/output streaming standards:

* **`stdin`:** Receives structured payloads/JSON-RPC instructions from the AI coordinator.
* **`stdout`:** Flushes response values back to the client. No unstructured code logs should be printed here.
* **`stderr`:** Used exclusively for runtime debugging logs, info dumps, and connection traces.

## 🤝 Contributing

Contributions are welcome! Please follow these steps to propose changes:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
