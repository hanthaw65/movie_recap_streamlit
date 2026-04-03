# Railway Deployment - Step-by-Step Guide

## အကျဉ်းချုပ် (Summary)
Railway သို့ deploy လုပ်ရန် အဆင့် (၅) ခု လိုအပ်ပါသည်။ အချိန် ၅-၁၀ မိနစ်ကြာမည်ဖြစ်သည်။

---

## Step 1: GitHub Account ကို ပြင်ဆင်ခြင်း

### 1.1 GitHub Repository ကို Create လုပ်ခြင်း

1. [github.com](https://github.com) သို့ သွားပါ
2. အညာဖက်ခြင်း၌ **"+"** icon ကို နှိပ်ပါ
3. **"New repository"** ကို ရွေးချယ်ပါ
4. အောက်ပါ အချက်အလက်များကို ဖြည့်ပါ:

| အချက်အလက် | အဖြေ |
|----------|------|
| Repository name | `movie_recap_streamlit` |
| Description | `AI-powered Movie Recap Generator in Burmese` |
| Visibility | Public |
| Initialize with README | မ ရွေးချယ်ပါနှင့် |

5. **"Create repository"** ကို နှိပ်ပါ

### 1.2 Local Computer တွင် Git ကို ပြင်ဆင်ခြင်း

Terminal/Command Prompt ကို ဖွင့်ပြီး အောက်ပါ commands များကို အစီအစဉ်အတိုင်း လုပ်ဆောင်ပါ:

```bash
# Step 1: movie_recap_streamlit ဖိုလ်ဒါသို့ သွားပါ
cd /home/ubuntu/movie_recap_streamlit

# Step 2: Git repository ကို initialize လုပ်ပါ
git init

# Step 3: အားလုံးဖိုင်များကို add လုပ်ပါ
git add .

# Step 4: First commit ကို create လုပ်ပါ
git commit -m "Initial commit: Movie Recap AI Streamlit app"

# Step 5: GitHub repository ကို remote အဖြစ်ထည့်သွင်းပါ
# (YOUR_USERNAME ကို သင်၏ GitHub username ဖြင့် အစားထိုးပါ)
git remote add origin https://github.com/YOUR_USERNAME/movie_recap_streamlit.git

# Step 6: Main branch ကို rename လုပ်ပါ
git branch -M main

# Step 7: Code ကို GitHub သို့ push လုပ်ပါ
git push -u origin main
```

**မှတ်ချက်:** GitHub သည် သင်၏ username နှင့် password (သို့မဟုတ် personal access token) ကို တောင်းခံမည်ဖြစ်သည်။

---

## Step 2: Railway Account ကို Create လုပ်ခြင်း

1. [railway.app](https://railway.app) သို့ သွားပါ
2. **"Login with GitHub"** ကို နှိပ်ပါ
3. သင်၏ GitHub account ဖြင့် login လုပ်ပါ
4. Railway သည် သင်၏ GitHub account ကို access လုပ်ရန် permission တောင်းခံမည်ဖြစ်သည် - **"Authorize"** ကို နှိပ်ပါ

---

## Step 3: Railway တွင် Project ကို Create လုပ်ခြင်း

### 3.1 New Project ကို Create လုပ်ခြင်း

1. Railway dashboard တွင် **"Create New Project"** ကို နှိပ်ပါ
2. အောက်ပါ options များ ကြည့်ရှုပါ:
   - **"Deploy from GitHub repo"** ကို ရွေးချယ်ပါ

### 3.2 GitHub Repository ကို ချိတ်ဆက်ခြင်း

1. **"Configure GitHub App"** ကို နှိပ်ပါ
2. သင်၏ GitHub repository များ ကြည့်ရှုခွင့်ပြုပါ
3. `movie_recap_streamlit` repository ကို ရွေးချယ်ပါ
4. **"Install & Continue"** ကို နှိပ်ပါ

### 3.3 Repository ကို ရွေးချယ်ခြင်း

1. သင်၏ `movie_recap_streamlit` repository ကို ရွေးချယ်ပါ
2. Railway သည် အလိုအလျောက် Dockerfile ကို detect လုပ်မည်ဖြစ်သည်
3. **"Deploy"** ကို နှိပ်ပါ

---

## Step 4: Environment Variables ကို ထည့်သွင်းခြင်း

### 4.1 Gemini API Key ကို ရယူခြင်း

1. [Google AI Studio](https://aistudio.google.com) သို့ သွားပါ
2. **"Get API Key"** ကို နှိပ်ပါ
3. **"Create API Key in new project"** ကို နှိပ်ပါ
4. Generated API key ကို copy လုပ်ပါ (ဒီ key ကို လုံခြုံစွာ ထိန်းသိမ်းပါ)

### 4.2 Railway တွင် Environment Variables ကို ထည့်သွင်းခြင်း

1. Railway dashboard တွင် သင်၏ project ကို ရွေးချယ်ပါ
2. **"Variables"** tab ကို နှိပ်ပါ
3. အောက်ပါ variables များကို ထည့်သွင်းပါ:

| Variable Name | Value |
|---------------|-------|
| GEMINI_API_KEY | (သင်ရယူထားသည့် API key) |
| OPENAI_API_KEY | (optional - လိုအပ်ပါက) |
| MAX_FILE_SIZE_MB | 500 |

**ထည့်သွင်းနည်း:**
- Variable name ကို type လုပ်ပါ
- Value ကို paste လုပ်ပါ
- **"Add"** ကို နှိပ်ပါ

---

## Step 5: Deployment ကို စောင့်ခြင်း

### 5.1 Build Process ကို စောင့်ခြင်း

1. Railway dashboard တွင် **"Deployments"** tab ကို နှိပ်ပါ
2. Build process ကို စောင့်ပါ (အချိန် ၅-၁၀ မိနစ်ကြာမည်)
3. Status မြင်ရမည်:
   - 🟡 **Building** - Docker image ကို build လုပ်နေသည်
   - 🟢 **Deployed** - အောင်မြင်သည်!

### 5.2 Live URL ကို ရယူခြင်း

1. Build အောင်မြင်ပြီးသည့်နောက် **"Deployments"** tab တွင် ကြည့်ပါ
2. **"View Deployment"** ကို နှိပ်ပါ
3. သင်၏ live URL ကို မြင်ရမည်:
   ```
   https://movie-recap-ai-production.up.railway.app
   ```

---

## အဆင့်ခြင်းအဆင့် ကျဉ်းချုပ်

| အဆင့် | လုပ်ဆောင်ချက် | အချိန် |
|------|-------------|------|
| 1 | GitHub repository create & push | 2-3 min |
| 2 | Railway account create | 1 min |
| 3 | Railway project create | 2 min |
| 4 | Environment variables ထည့်သွင်း | 1 min |
| 5 | Build & deployment စောင့်ခြင်း | 5-10 min |
| **စုစုပေါင်း** | | **11-17 min** |

---

## အဆင့်တစ်ခုချင်းစီ၏ အသေးစိတ်

### အဆင့် 1: GitHub Setup

```bash
# Terminal တွင် အောက်ပါ commands များကို လုပ်ဆောင်ပါ
cd /home/ubuntu/movie_recap_streamlit
git init
git add .
git commit -m "Initial commit: Movie Recap AI"
git remote add origin https://github.com/YOUR_USERNAME/movie_recap_streamlit.git
git branch -M main
git push -u origin main
```

**ရလဒ်:** GitHub တွင် သင်၏ code အားလုံး ရှိသည်

---

### အဆင့် 2: Railway Account

1. [railway.app](https://railway.app) သွားပါ
2. GitHub ဖြင့် login လုပ်ပါ
3. Permission ပြုလုပ်ပါ

**ရလဒ်:** Railway account ကို သင် အသုံးပြုနိုင်သည်

---

### အဆင့် 3: Project Creation

Railway dashboard တွင်:
1. "Create New Project" နှိပ်ပါ
2. "Deploy from GitHub repo" ရွေးချယ်ပါ
3. `movie_recap_streamlit` ရွေးချယ်ပါ
4. Deploy နှိပ်ပါ

**ရလဒ်:** Railway သည် အလိုအလျောက် build စတင်မည်

---

### အဆင့် 4: Environment Variables

Railway dashboard Variables tab တွင်:

```
GEMINI_API_KEY = your_api_key_here
MAX_FILE_SIZE_MB = 500
```

**ရလဒ်:** Application သည် API key ကို အသုံးပြုနိုင်သည်

---

### အဆင့် 5: Wait for Deployment

Build process:
- 🟡 Building (5-10 min)
- 🟢 Deployed ✓

**ရလဒ်:** Live URL ရရှိသည်!

---

## အဖြေများ (FAQ)

### Q: GitHub push လုပ်ရန် password မည်သည်ကို အသုံးပြုရမည်နည်း?

**A:** GitHub သည် personal access token ကို အသုံးပြုရန် အကြံပြုသည်။ အောက်ပါ အတိုင်း လုပ်ပါ:

1. GitHub settings သို့ သွားပါ (Settings > Developer settings > Personal access tokens)
2. "Generate new token" ကို နှိပ်ပါ
3. `repo` scope ကို ရွေးချယ်ပါ
4. Token ကို copy လုပ်ပါ
5. Git push လုပ်ရန် password အနေဖြင့် အသုံးပြုပါ

---

### Q: Railway တွင် build fail ဖြစ်ပါက?

**A:** အောက်ပါ ကျေးဇူးပြုပြီး ကြည့်ပါ:

1. Railway dashboard တွင် **"Logs"** tab သွားပါ
2. Error message ကို ဖတ်ပါ
3. အဆိုပါ error message ကို ကျွန်ုပ်ထံ ပေးပါ
4. ကျွန်ုပ်သည် ကူညီပေးမည်

---

### Q: Application run ဖြစ်ပြီးသည့်နောက် အဆင်မြန်ပါက?

**A:** အောက်ပါ အရာများ ကြည့်ပါ:

1. Railway dashboard တွင် **"Logs"** ကြည့်ပါ
2. GEMINI_API_KEY ကို ရှင်းလင်းစွာ ထည့်သွင်းထားသည်ကို သိသာစွာ ကြည့်ပါ
3. Whisper model သည် ပထမအကြိမ် download ဖြစ်ရန် အချိန်ကြာမည်

---

## အကူအညီ (Support)

အကျပ်အတည်းမျိုးအကျပ်အတည်းမျိုး ရှိပါက:

1. Railway documentation: [docs.railway.app](https://docs.railway.app)
2. Railway support: [Railway Discord](https://discord.gg/railway)
3. ကျွန်ုပ်ထံ ကျေးဇူးပြုပြီး ကူညီတောင်းခံပါ

---

## အောင်မြင်ခြင်း!

အဆင့်များ အားလုံး အောင်မြင်ပြီးသည့်နောက်:

✅ သင်၏ Movie Recap AI application သည် live ဖြစ်သည်
✅ သင်သည် live URL ကို ရယူသည်
✅ အသုံးပြုသူများသည် ၎င်းကို အသုံးပြုနိုင်သည်

---

## နောက်လည်ခြင်း

1. Application ကို test လုပ်ပါ
2. Live URL ကို သူများထံ မျှဝေပါ
3. Feedback ရယူပါ
4. လိုအပ်ပါက အဆင့်မြှင့်တင်ပါ

**ကျေးဇူးတင်ပါသည်!** 🎉

---

## ဆက်စပ်သည့် အချက်အလက်များ

- **Railway Pricing:** [railway.app/pricing](https://railway.app/pricing)
- **Gemini API:** [aistudio.google.com](https://aistudio.google.com)
- **Streamlit Docs:** [docs.streamlit.io](https://docs.streamlit.io)

**Last Updated:** March 31, 2026
