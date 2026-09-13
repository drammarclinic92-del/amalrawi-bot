from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running - Amal Rawi Clinic', 200

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == 'AmmarClinic2024':
            return challenge, 200
        return 'Forbidden', 403
    if request.method == 'POST':
        print(request.get_json())
        return 'OK', 200
