"""
بوت واتساب عيادة الدكتور عمار - نسخة مرتبطة بـ Google Sheet
الشيت: https://docs.google.com/spreadsheets/d/1cCXED4MnPNNqAKdsXFPyhqbM60_AJqE3cQHSkBAj7Ls/edit
ايميل: drammarclinic92@gmail.com
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

SHEET_ID = "1cCXED4MnPNNqAKdsXFPyhqbM60_AJqE3cQHSkBAj7Ls"
WHATSAPP_TOKEN = "ضع_التوكن_هنا"
PHONE_NUMBER_ID = "ضع_ID_رقم_الواتساب_هنا"
AI_API_KEY = "ضع_مفتاح_Groq_هنا"
VERIFY_TOKEN = "ammar_clinic_2026"

# ============ دالة تقرا الاعدادات من الشيت مباشرة ============
def get_clinic_data_from_sheet():
    """
    هذه الدالة تقرا كلشي من الشيت اللي رفعته
    اي تعديل تسويه بالشيت، البوت يفهمه فوراً
    """
    try:
        # تقرا من Google Sheets كـ CSV (بدون ما تحتاج OAuth معقد)
        # الخدمات
        services_url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=Services_الخدمات"
        settings_url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=Settings_الاعدادات"
        
        services_csv = requests.get(services_url).text
        settings_csv = requests.get(settings_url).text
        
        return services_csv, settings_csv
    except Exception as e:
        print(e)
        return None, None

def build_dynamic_prompt():
    services, settings = get_clinic_data_from_sheet()
    
    base_prompt = f"""
أنت موظف استقبال ذكي لعيادة الدكتور عمار حسين الراوي.
تتحدث عراقي مهذب.

معلومات حية من Google Sheet (ID: {SHEET_ID}):
الخدمات والاسعار:
{services}

الاعدادات:
{settings}

قواعد:
1. ابدأ بـ: أهلاً وسهلاً بيك في عيادة الدكتور عمار حسين الراوي 🌿
2. اذا سأل عن سعر، خذه من الخدمات اعلاه
3. اذا سأل عن دوام او تواجد الدكاترة، خذه من الاعدادات اعلاه
4. لا تشخص طبيا ابدا
5. عند الحجز اطلب الاسم والوقت واحفظه
6. انهي بـ: دوامنا من 15:30-22:00 - الجمعة عطلة - 0780540459
"""
    return base_prompt

# ============ ارسال رسالة واتساب ============
def send_whatsapp(to, text):
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}", "Content-Type": "application/json"}
    payload = {"messaging_product": "whatsapp", "to": to, "type": "text", "text": {"body": text}}
    requests.post(url, headers=headers, json=payload)

# ============ الذكاء الاصطناعي ============
def ask_ai(user_message):
    prompt = build_dynamic_prompt()
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {AI_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "llama-3.1-70b-versatile",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.3
    }
    try:
        r = requests.post(url, headers=headers, json=data, timeout=20)
        return r.json()['choices'][0]['message']['content']
    except:
        return "أهلاً وسهلاً بيك 🌿 صار خلل بسيط، تكدر تتواصل على 0780540459 - دوامنا 3:30 عصراً للـ 10 مساءً"

# ============ حفظ الحجز في الشيت عن طريق Google Forms / Apps Script ============
# ضع هنا رابط الـ Web App اللي طلعلك من Apps Script
APPS_SCRIPT_WEBAPP_URL = "ضع_رابط_الويب_آب_هنا"

def save_booking_to_sheet(name, phone, time, service):
    import datetime
    data = {
        "date": str(datetime.date.today()),
        "time": time,
        "name": name,
        "phone": phone,
        "service": service,
        "doctor": "د. عمار"
    }
    try:
        requests.post(APPS_SCRIPT_WEBAPP_URL, json=data)
    except:
        pass

# مثال للتجربة المحلية
if __name__ == "__main__":
    print("البوت مربوط بالشيت:")
    print(f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit")
    print("\nجرب سؤال:")
    print(ask_ai("شكد سعر زراعة السن؟"))
