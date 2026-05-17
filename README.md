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
