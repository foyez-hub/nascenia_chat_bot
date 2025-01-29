

# Nacenia Chatbot


## Prerequisites
Before running this application, ensure the following tools are installed on your system:
1. **Python 3.6 or later**
2. **pip** (Python package manager)
3. **`ollama` CLI** (Make sure this tool is installed and functional on your server)

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

### 5. Run the Flask Application
Start the Flask application by running:
```bash
python app.py
```

By default, the app will run on `http://127.0.0.1:5001`.

### 6. Access the Application
- Open your browser and navigate to:  
  `http://127.0.0.1:5001/chat`

---



## File Structure
```
.
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # Frontend template for chat interface
├── requirements.txt        # Python dependencies
├── README.md               # Documentation (this file)
└── venv/                   # Virtual environment (created during setup)
```

---

