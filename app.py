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
        print(f"[VERIFY ATTEMPT] mode={mode} token={token} challenge={challenge}", flush=True)
        if mode == 'subscribe' and token == VERIFY_TOKEN and challenge:
            print(f"WEBHOOK VERIFIED OK challenge={challenge}", flush=True)
            response = make_response(challenge, 200)
            response.mimetype = "text/plain"
            return response
        else:
            print(f"VERIFY FAILED - Expected token {VERIFY_TOKEN} got {token}", flush=True)
            return 'Verification failed', 403

    if request.method == 'POST':
        try:
            data = request.get_json(force=True, silent=True)
            print(f"[POST RECEIVED] {data}", flush=True)
        except Exception as e:
            print(f"[POST ERROR] {e}", flush=True)
        return 'OK', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
