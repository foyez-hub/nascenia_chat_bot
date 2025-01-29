from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/chat')
def home():
    return render_template('index.html')  


@app.route('/generate_chat', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")
        
        if not prompt:
            return jsonify({"error": "Prompt is missing"}), 400
            
        process = subprocess.run(
            ["ollama", "run", "deepseek-r1:1.5b"],
            input=prompt.encode(), 
            capture_output=True
        )
        
        response = process.stdout.decode("utf-8").strip()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5001, debug=True)