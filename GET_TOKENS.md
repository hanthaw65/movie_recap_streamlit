# GitHub နှင့် Railway Tokens ရယူခြင်း

## အကျဉ်းချုပ်

Automated deployment အတွက် tokens (၂) ခု လိုအပ်သည်:
1. GitHub Personal Access Token
2. Railway API Token

---

## Token 1: GitHub Personal Access Token ရယူခြင်း

### အဆင့် ၁: GitHub Settings သို့ သွားခြင်း

1. ဖုန်းတွင် [github.com](https://github.com) သွားပါ
2. အညာဖက်ခြင်း၌ သင်၏ **profile picture** ကို နှိပ်ပါ
3. **"Settings"** ကို ရွေးချယ်ပါ

### အဆင့် ၂: Developer Settings သို့ သွားခြင်း

1. Settings page တွင် အဆုံးဖက်ခြင်း၌ **"Developer settings"** ကို နှိပ်ပါ
2. **"Personal access tokens"** ကို ရွေးချယ်ပါ
3. **"Tokens (classic)"** ကို ရွေးချယ်ပါ

### အဆင့် ၃: New Token Create လုပ်ခြင်း

1. **"Generate new token"** ကို နှိပ်ပါ
2. **"Generate new token (classic)"** ကို ရွေးချယ်ပါ

### အဆင့် ၄: Token Configuration

အောက်ပါ အချက်အလက်များကို ဖြည့်ပါ:

| အချက်အလက် | အဖြေ |
|----------|------|
| Token name | `movie-recap-deploy` |
| Expiration | 90 days (သို့မဟုတ် No expiration) |

### အဆင့် ၅: Scopes ရွေးချယ်ခြင်း

အောက်ပါ scopes များကို ရွေးချယ်ပါ:

```
✓ repo (အားလုံး)
  ✓ repo:status
  ✓ repo_deployment
  ✓ public_repo
  ✓ repo:invite
  ✓ security_events

✓ workflow

✓ write:packages
✓ read:packages
```

**အလွယ်ဆုံးနည်း:** `repo` နှင့် `workflow` ကို ရွေးချယ်ပါ။

### အဆင့် ၆: Token Generate လုပ်ခြင်း

1. အဆုံးဖက်ခြင်း၌ **"Generate token"** ကို နှိပ်ပါ
2. Generated token ကို မြင်ရမည်

### အဆင့် ၇: Token ကို Copy လုပ်ခြင်း

**အရေးကြီးသည်:** Token ကို ကျွန်ုပ်ထံ ပေးမီ copy လုပ်ပါ။ ၎င်းကို ထပ်မံ မြင်ရမည်မဟုတ်ပါ။

```
ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**ဒီ token ကို ကျွန်ုပ်ထံ ပေးပါ။**

---

## Token 2: Railway API Token ရယူခြင်း

### အဆင့် ၁: Railway Account Create လုပ်ခြင်း

1. ဖုန်းတွင် [railway.app](https://railway.app) သွားပါ
2. **"Login with GitHub"** ကို နှိပ်ပါ
3. သင်၏ GitHub account ဖြင့် login လုပ်ပါ

### အဆင့် ၂: Railway Settings သို့ သွားခြင်း

1. Railway dashboard တွင် အညာဖက်ခြင်း၌ သင်၏ **profile icon** ကို နှိပ်ပါ
2. **"Account"** သို့မဟုတ် **"Settings"** ကို ရွေးချယ်ပါ

### အဆင့် ၃: API Tokens Section သို့ သွားခြင်း

1. Settings page တွင် **"API Tokens"** သို့မဟုတ် **"Tokens"** ကို ရွေးချယ်ပါ
2. **"Create New Token"** ကို နှိပ်ပါ

### အဆင့် ၄: Token Name ထည့်သွင်းခြင်း

Token name ကို အောက်ပါအတိုင်း ထည့်သွင်းပါ:

```
movie-recap-deploy
```

### အဆင့် ၅: Token Generate လုပ်ခြင်း

1. **"Generate"** သို့မဟုတ် **"Create"** ကို နှိပ်ပါ
2. Generated token ကို မြင်ရမည်

### အဆင့် ၆: Token ကို Copy လုပ်ခြင်း

**အရေးကြီးသည်:** Token ကို ကျွန်ုပ်ထံ ပေးမီ copy လုပ်ပါ။

```
rw_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**ဒီ token ကို ကျွန်ုပ်ထံ ပေးပါ။**

---

## အဆုံးအဖြတ်

ကျွန်ုပ်ထံ အောက်ပါ အရာများ ပေးပါ:

```
GitHub Personal Access Token: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Railway API Token: rw_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Gemini API Key: (သင်ရှိပြီးသည့်)
```

ဒါပြီးလျှင် ကျွန်ုပ်သည် အလိုအလျောက် deploy လုပ်ပေးနိုင်သည်။

---

## ⚠️ လုံခြုံမှု သတိပေးချက်

**အရေးကြီးသည်:**

1. ဒီ tokens များကို အများသူငါ မမျှဝေပါနှင့်
2. ကျွန်ုပ်သည် ဒီ tokens များကို deploy အတွက်သာ အသုံးပြုမည်
3. Deploy ပြီးသည့်နောက် ကျွန်ုပ်သည် ဒီ tokens များကို delete လုပ်မည်
4. သင်သည် Railway dashboard တွင် tokens ကို revoke လုပ်နိုင်သည်

---

## နောက်လည်ခြင်း

Tokens ရယူပြီးသည့်နောက်:

1. ကျွန်ုပ်ထံ tokens (၂) ခု ပေးပါ
2. ကျွန်ုပ်သည် deployment script ကို ဖန်တီးပါ
3. ကျွန်ုပ်သည် script ကို run လုပ်ပါ
4. အလိုအလျောက် deploy ဖြစ်သည်
5. Live URL ရရှိသည်

---

**Last Updated:** March 31, 2026
