from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running', 200

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == 'AmmarClinic2024':
            return request.args.get('hub.challenge'), 200
        return 'Forbidden', 403
    return 'OK', 200
