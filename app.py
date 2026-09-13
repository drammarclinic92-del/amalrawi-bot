import os
from flask import Flask, request, make_response
app = Flask(__name__)
VERIFY_TOKEN = "AmmarClinic2024"
@app.route('/')
def home():
    return 'Amal Rawi Clinic Bot is LIVE', 200
@app.route('/webhook', methods=['GET', 'POST'])
@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        print(f"[VERIFY] mode={mode} token={token} challenge={challenge}", flush=True)
        if mode == 'subscribe' and token == VERIFY_TOKEN and challenge:
            print(f"WEBHOOK VERIFIED OK", flush=True)
            resp = make_response(challenge, 200)
            resp.mimetype = "text/plain"
            return resp
        return 'Verification failed', 403
    if request.method == 'POST':
        print(f"[POST] {request.get_json(force=True, silent=True)}", flush=True)
        return 'OK', 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
