/div><div>66</div><div>67</div><div>68</div><div>69</div><div>70</div><div>71</div><div>72</div><div>73</div><div>74</div><div>75</div><div>76</div><div>77</div><div>78</div><div>79</div><div>80</div><div>81</div><div>82</div><div>83</div><div>84</div><div>85</div><div>86</div><div>87</div><div>88</div><div>89</div><div>90</div><div>91</div><div>92</div><div>93</div><div>94</div><div>95</div><div>96</div><div>97</div><div>98</div><div>99</div><div>100</div><div>101</div><div>102</div><div>103</div><div>104</div><div>105</div><div>106</div><div>107</div><div>108</div><div>109</div></div><code class="block min-w-0 flex-1 overflow-x-auto whitespace-pre"><pre class="shiki shiki-themes github-light github-dark" style="--shiki-light:#24292e;--shiki-dark:#e1e4e8;--shiki-light-bg:#fff;--shiki-dark-bg:#24292e" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">import</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> os</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">import</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> requests</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">from</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> flask </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">import</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> Flask, request</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">app </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> Flask(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">__name__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">SHEET_ID</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> =</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> os.getenv(</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"SHEET_ID"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"1cCXED4MnPNNqAKdsXFPyhqbM60_AJqE3cQHSkBAj7Ls"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">WHATSAPP_TOKEN</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> =</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> os.getenv(</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"WHATSAPP_TOKEN"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">""</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">PHONE_NUMBER_ID</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> =</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> os.getenv(</span><span style="--shiki-light:#032F62;--from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot عيادة امل الراوي شغال ✅"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)iki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> {</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"Authorization"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">f</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"Bearer </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">{GROQ_API_KEY}</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"Content-Type"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"application/json"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">}</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">        data </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> {</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">            "model"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"llama-3.1-8b-instant"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">,</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">            "messages"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: [</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">                {</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"role"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"system"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"content"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: prompt},</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">                {</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"role"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"user"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"content"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: user_msg}</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">            ],</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">            "temperature"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">0.3</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">        }</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">        r </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> requests.post(url, </span><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70">headers</span><span style="--sdef build_dynamic_prompt():
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
