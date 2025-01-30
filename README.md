# Nacenia Chatbot

## Prerequisites
Before running this application, ensure the following tools are installed on your system:

1. **Python 3.10.16 or later**
2. **pip** (Python package manager)
3. **Ollama** (for model execution)

### Installing Ollama on Ubuntu
To install Ollama on Linux, run the following command:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

After installation, download the model by running:
```bash
ollama run deepseek-r1
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/foyez-hub/nascenia_chat_bot.git
cd nascenia_chat_bot
```

### 2. Create a Python Virtual Environment
To isolate dependencies, it's recommended to use a virtual environment:
```bash
python3 -m venv venv
```

Activate the virtual environment:
- On Linux/Mac:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Configure the Application
Ensure the `ollama` CLI tool is correctly installed and available in your system's PATH. You can verify this by running:
```bash
ollama --help
```

### 5. Update API Endpoint
Before running `app.py`, update the API endpoint in `static/script.js`:

Locate the following code in `static/script.js`:
```javascript
    const response = await fetch('https://your_server_domain/generate_chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: message })
    });
```
Replace `'your_server_domain'` with your actual domain or localhost if running locally.

### 6. Run the Flask Application
Start the Flask application by running:
```bash
python app.py
```
By default, the app will run on `http://127.0.0.1:5001`.

### 7. Access the Application
- If running locally, open your browser and navigate to:
  ```
  http://127.0.0.1:5001/chat
  ```
- If running from a server, open your browser and navigate to:
  ```
  https://your_server_domain/chat
  ```

---

## File Structure
```
.
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # Frontend template for chat interface
├── static/
│   └── script.js           # JavaScript for handling chat interactions
├── requirements.txt        # Python dependencies
├── README.md               # Documentation (this file)
└── venv/                   # Virtual environment (created during setup)
```

---

## Notes
- Ensure that Ollama is running before starting the chatbot.
- If deploying online, update the API endpoint in `script.js` accordingly.
- If encountering permission issues, use `chmod +x` on the installation script.

Happy Coding! 🚀

