# Gemini API Key ရယူခြင်း - အသေးစိတ် လမ်းညွှန်

## အကျဉ်းချုပ်

Google Gemini API သည် free ဖြစ်သည်။ အဆင့်များ အောက်ပါအတိုင်း လုပ်ဆောင်ပါ။

---

## အဆင့် ၁: Google Account ကို ကြည့်ခြင်း

### အရှိန်အဟုန်

Gemini API key ရယူရန် Google account လိုအပ်သည်။

**သင်ရှိပြီးသည်ကို ကြည့်ပါ:**
- Gmail account
- Google account

အကယ်၍ မရှိပါက [accounts.google.com](https://accounts.google.com) တွင် create လုပ်ပါ။

---

## အဆင့် ၂: Google AI Studio သို့ သွားခြင်း

### 2.1 Website ကို ဖွင့်ခြင်း

1. ဖုန်းတွင် browser ကို ဖွင့်ပါ
2. အောက်ပါ URL သို့ သွားပါ:

```
https://aistudio.google.com
```

သို့မဟုတ် Google မှ "Google AI Studio" ကို search လုပ်ပါ။

### 2.2 Website မြင်ရခြင်း

Website ကို ဖွင့်ပြီးသည့်နောက် အောက်ပါ page မြင်ရမည်:

```
Google AI Studio
Try Gemini API for free
```

---

## အဆင့် ၃: API Key ရယူခြင်း

### 3.1 "Get API Key" ကို နှိပ်ခြင်း

1. Page တွင် **"Get API Key"** button ကို ရွေးချယ်ပါ
2. သို့မဟုတ် အညာဖက်ခြင်း၌ **"API Key"** ကို ရွေးချယ်ပါ

### 3.2 API Key Create လုပ်ခြင်း

အောက်ပါ options များ မြင်ရမည်:

```
Create API Key
├── Create API Key in new project
└── Create API Key in existing project
```

**"Create API Key in new project"** ကို ရွေးချယ်ပါ။

### 3.3 Project Create လုပ်ခြင်း

1. Google သည် new project ကို အလိုအလျောက် create လုပ်မည်
2. အချိန် ၁-၂ စက္ကန့်ကြာမည်
3. API key ကို မြင်ရမည်

---

## အဆင့် ၄: API Key ကို Copy လုပ်ခြင်း

### 4.1 API Key ကို မြင်ခြင်း

အောက်ပါ format ရှိသည့် API key မြင်ရမည်:

```
AIzaSyD_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 4.2 Copy လုပ်ခြင်း

1. API key ကို နှိပ်ပါ
2. သို့မဟုတ် **"Copy"** button ကို နှိပ်ပါ
3. API key ကို clipboard သို့ copy ဖြစ်သည်

### 4.3 API Key ကို သိမ်းဆည်းခြင်း

API key ကို လုံခြုံသည့် နေရာတွင် သိမ်းဆည်းပါ:

```
AIzaSyD_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## အဆင့် ၅: API Key ကို အသုံးပြုခြင်း

### 5.1 Railway တွင် ထည့်သွင်းခြင်း

Deploy အတွက် Railway တွင် အောက်ပါအတိုင်း ထည့်သွင်းပါ:

```
GEMINI_API_KEY = AIzaSyD_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5.2 Local Testing အတွက်

Local machine တွင် test လုပ်ရန် `.env` file တွင် ထည့်သွင်းပါ:

```
GEMINI_API_KEY=AIzaSyD_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## အဆင့် ၆: API Key အောင်မြင်ခြင်း

### 6.1 API Key ကို ကြည့်ခြင်း

Google AI Studio dashboard တွင် သင်၏ API keys ကို ကြည့်နိုင်သည်:

```
My API Keys
├── AIzaSyD_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx (Active)
```

### 6.2 API Key ကို Restrict လုပ်ခြင်း (Optional)

Security အတွက် API key ကို restrict လုပ်နိုင်သည်:

1. API key ကို နှိပ်ပါ
2. **"Restrict Key"** ကို ရွေးချယ်ပါ
3. Allowed APIs: **"Generative Language API"** ကို ရွေးချယ်ပါ
4. Save လုပ်ပါ

---

## အဆင့် ၇: API Key အသုံးပြုခြင်း

### 7.1 Application တွင် အသုံးပြုခြင်း

Movie Recap AI application သည် အလိုအလျောက် API key ကို အသုံးပြုမည်:

```python
# ai_processor.py တွင်
import os
api_key = os.getenv("GEMINI_API_KEY")
```

### 7.2 API Quota ကြည့်ခြင်း

Google AI Studio dashboard တွင် API usage ကို ကြည့်နိုင်သည်:

```
Usage
├── Requests: X/60 per minute
├── Tokens: X/1,000,000 per day
```

---

## အကျပ်အတည်းများ နှင့် ဖြေရှင်းချက်

### Q: "Create API Key in new project" button မမြင်ရ

**A:** အောက်ပါ အရာများ ကြည့်ပါ:

1. [aistudio.google.com](https://aistudio.google.com) သွားပါ
2. Google account သို့ login လုပ်ထားသည်ကို ကြည့်ပါ
3. Browser cache ကို clear လုပ်ကြည့်ပါ
4. အခြား browser ကို သုံးကြည့်ပါ

### Q: "API Key မရယူနိုင်ပါ" error ရှိသည်

**A:** အောက်ပါ အရာများ ကြည့်ပါ:

1. Google account သည် active ဖြစ်သည်ကို ကြည့်ပါ
2. Google Billing account ကို ရှင်းလင်းစွာ ကြည့်ပါ
3. VPN သို့မဟုတ် Proxy ကို ဖြုတ်ကြည့်ပါ
4. အခြား device တွင် ကြည့်ကြည့်ပါ

### Q: API Key မှားသည်

**A:** အောက်ပါ အရာများ ကြည့်ပါ:

1. API key ကို ပြည့်စုံစွာ copy လုပ်ထားသည်ကို ကြည့်ပါ
2. API key တွင် extra spaces မရှိသည်ကို ကြည့်ပါ
3. API key သည် `AIzaSyD_` ဖြင့် စတင်သည်ကို ကြည့်ပါ
4. API key ကို revoke လုပ်ပြီး new key ရယူကြည့်ပါ

### Q: API Key အလုပ်မလုပ်ပါ

**A:** အောက်ပါ အရာများ ကြည့်ပါ:

1. API key သည် active ဖြစ်သည်ကို ကြည့်ပါ
2. Generative Language API သည် enable ဖြစ်သည်ကို ကြည့်ပါ
3. API quota သည် ကျန်သည်ကို ကြည့်ပါ
4. Internet connection ကို ကြည့်ပါ

---

## အသုံးပြုခွင့်ပြုချက် (Quota)

Google Gemini API သည် free ဖြစ်သည်။ Quota အောက်ပါအတိုင်း:

| အချက်အလက် | Quota |
|----------|-------|
| Requests per minute | 60 |
| Tokens per day | 1,000,000 |
| Cost | FREE |

**မှတ်ချက်:** Quota သည် လစ်စဉ် reset ဖြစ်သည်။

---

## နောက်လည်ခြင်း

API key ရယူပြီးသည့်နောက်:

1. API key ကို ကျွန်ုပ်ထံ ပေးပါ
2. ကျွန်ုပ်သည် deployment script ကို ဖန်တီးပါ
3. အလိုအလျောက် deploy ဖြစ်သည်
4. Live URL ရရှိသည်

---

## အကူအညီ

- **Google AI Studio:** [aistudio.google.com](https://aistudio.google.com)
- **Gemini API Docs:** [ai.google.dev](https://ai.google.dev)
- **Pricing:** [ai.google.dev/pricing](https://ai.google.dev/pricing)

---

**Last Updated:** March 31, 2026
