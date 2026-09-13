import os
import json
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# === إعدادات عيادة الدكتور عمار ===
PHONE_NUMBER_ID = "481608268378548"
WABA_ID = "5014646897203511"
ACCESS_TOKEN = os.environ.get("WHATSAPP_TOKEN", "PUT_YOUR_TOKEN_HERE")
VERIFY_TOKEN = "ammar_clinic_verify_2024"

# ردود باللهجة العراقية
RESPONSES = {
    "greeting": """مرحبا حبيبي 🌸
أنا مساعد عيادة الدكتور عمار حسين الراوي للتجميل

شنو تحتاج؟
1️⃣ حجز موعد
2️⃣ استفسار عن الخدمات (فيلر، بوتوكس، ليزر)
3️⃣ موقع العيادة
4️⃣ التحدث مع الموظف

دزلي رقم الخدمة""",
    "booking": """تمام للحجز 🗓️
دزلي:
- اسمك الثلاثي
- الخدمة المطلوبة
- اليوم اللي يناسبك

مثال: عمار حسين - فيلر - باجر العصر""",
    "services": """خدماتنا في عيادة الدكتور عمار 💉✨:

💎 فيلر شفايف وخدود
💎 بوتوكس
💎 بلازما للشعر والبشرة
💎 ليزر إزالة شعر
💎 تنظيف بشرة عميق
💎 ميزوثيرابي

أي خدمة تريد تفاصيل عنها؟""",
    "location": """📍 موقعنا:
الرمادي - شارع الأطباء - مجمع الأمل الطبي
أوقات الدوام: 4 عصراً - 9 مساءً
للتواصل: 07800540459

تحب احجزلك موعد؟"""
}

def send_whatsapp(to, text):
    url = f"https://graph.facebook.com/v21.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    try:
        r = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"SEND {to} -> {r.status_code}: {r.text[:500]}")
        return r.json()
    except Exception as e:
        print(f"SEND ERROR: {e}")
        return {"error": str(e)}

@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    print(f"VERIFY attempt token={token} challenge={challenge}")
    if token == VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        print(f"WEBHOOK IN: {json.dumps(data, ensure_ascii=False)[:2000]}")
        if not data:
            return jsonify({"status": "no data"}), 200

        entry = data.get("entry", [{}])[0]
        changes = entry.get("changes", [{}])[0]
        value = changes.get("value", {})

        if "messages" in value:
            msg = value["messages"][0]
            from_number = msg.get("from")
            msg_type = msg.get("type")

            if msg_type == "text":
                text = msg.get("text", {}).get("body", "").lower()
            else:
                text = ""

            print(f"FROM {from_number}: {text}")

            if any(w in text for w in ["مرحبا", "هلا", "سلام", "hi", "hello", "السلام"]):
                reply = RESPONSES["greeting"]
            elif "1" in text or "حجز" in text or "موعد" in text:
                reply = RESPONSES["booking"]
            elif "2" in text or "خدمة" in text or "فيلر" in text or "بوتوكس" in text:
                reply = RESPONSES["services"]
            elif "3" in text or "موقع" in text or "عنوان" in text:
                reply = RESPONSES["location"]
            elif "4" in text or "موظف" in text:
                reply = "تمام راح احولك على الموظف، انتظر لحظة 🙏\nراح يتواصل وياك على نفس الرقم"
            else:
                reply = RESPONSES["greeting"]

            if from_number:
                send_whatsapp(from_number, reply)

    except Exception as e:
        print(f"WEBHOOK ERROR: {e}")
        import traceback
        traceback.print_exc()

    return jsonify({"status": "ok"}), 200

@app.route("/")
def home():
    token_set = "✅" if os.environ.get("WHATSAPP_TOKEN") else "❌ ماكو توكن"
    return f"Bot running {PHONE_NUMBER_ID} - عيادة الدكتور عمار {token_set} - Token: {ACCESS_TOKEN[:20]}..."

@app.route("/test")
def test():
    to = request.args.get("to")
    if not to:
        return "Add?to=9647xxxxxxxx"
    send_whatsapp(to, "تجربة البوت - عيادة الدكتور عمار ✅")
    return f"Sent to {to}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
