from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "message": "API OK"})

@app.route('/api/implants')
def implants():
    return jsonify([
        {"id": 1, "name": "aditya-bot", "ip": "1.1.1.1", "status": "online"}
    ])

@app.route('/api/command', methods=['POST', 'GET'])
def command():
    try:
        if request.method == 'POST':
            data = request.get_json() or {}
        else:
            data = request.args.to_dict()
        
        target = data.get('target', 'test')
        method = data.get('method', 'udp')
        duration = data.get('duration', '30')
        
        return jsonify({
            "success": True,
            "message": f"Attack: {target} {method} {duration}s",
            "target": target
        })
    except:
        return jsonify({"success": True, "message": "Command OK"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
