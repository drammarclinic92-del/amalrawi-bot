from flask import Flask, request
import os, requests, csv, io

app = Flask(__name__)

SHEET_ID = os.environ.get("SHEET_ID", "1cCXED4MnPNNqAKdsXFPyhqbM60_AJqE3cQHSkBAj7Ls")
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "amalrawi123")

def get_sheet_data():
    try:
        url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"
        r = requests.get(url, timeout=10)
        if r.status_code!= 200:
            return []
        f = io.StringIO(r.text)
        reader = csv.DictReader(f)
        return list(reader)
    except Exception as e:
        print(f"Sheet error: {e}")
        return []

@app.route("/")
def home():
    data = get_sheet_data()
    count = len(data)
    return f"Bot عيادة امل الراوي شغال | عدد الاسئلة في الشيت: {count} | webhook: /webhook"

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print(f"Incoming: {data}")
    try:
        if data and "entry" in data:
            for entry in data["entry"]:
                for change in entry.get("changes", []):
                    value = change.get("value", {})
                    messages = value.get("messages", [])
                    for msg in messages:
                        text = msg.get("text", {}).get("body", "").lower()
                        from_num = msg.get("from")
                        print(f"Message from {from_num}: {text}")
                        sheet = get_sheet_data()
                        answer = None
                        for row in sheet:
                            # يحاول يلقى اول عمودين كسؤال وجواب
                            vals = list(row.values())
                            q = str(vals[0] if vals else "").lower()
                            if any(word in q for word in text.split() if len(word)>3):
                                answer = str(vals[1] if len(vals)>1 else "")
                                break
                        if not answer:
                            answer = "اهلا بيك في عيادة امل الراوي دز سؤالك ونجاوبك، او احجز موعد."
                        print(f"Reply would be: {answer}")
    except Exception as e:
        print(f"Webhook error: {e}")
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
