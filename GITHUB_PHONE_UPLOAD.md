# ဖုန်းမှ GitHub သို့ Code Upload လုပ်ခြင်း (Option C)

## အကျဉ်းချုပ်

ဖုန်းတွင် GitHub website မှ တိုက်ရိုက် upload လုပ်နိုင်သည်။ Terminal commands မလိုအပ်ပါ။

---

## အဆင့် ၁: GitHub Repository Create လုပ်ခြင်း

### 1.1 GitHub Website ကို ဖုန်းတွင် ဖွင့်ခြင်း

1. ဖုန်းတွင် browser ကို ဖွင့်ပါ (Chrome, Safari, Firefox စသည်)
2. [github.com](https://github.com) သို့ သွားပါ
3. အညာဖက်ခြင်း၌ **"Sign in"** ကို နှိပ်ပါ
4. သင်၏ GitHub username နှင့် password ကို ထည့်သွင်းပါ
5. **"Sign in"** ကို နှိပ်ပါ

### 1.2 New Repository Create လုပ်ခြင်း

1. GitHub homepage တွင် အညာဖက်ခြင်း၌ **"+"** icon ကို နှိပ်ပါ
2. **"New repository"** ကို ရွေးချယ်ပါ
3. အောက်ပါ အချက်အလက်များကို ဖြည့်ပါ:

| အချက်အလက် | အဖြေ |
|----------|------|
| Repository name | `movie_recap_streamlit` |
| Description | `AI-powered Movie Recap Generator` |
| Visibility | **Public** ကို ရွေးချယ်ပါ |
| Initialize with README | **မ ရွေးချယ်ပါနှင့်** |

4. **"Create repository"** ကို နှိပ်ပါ

### 1.3 Repository အောင်မြင်ခြင်း

Repository create ပြီးသည့်နောက် အောက်ပါ page မြင်ရမည်:

```
movie_recap_streamlit
Your repository is empty.
```

---

## အဆင့် ၂: Files များကို Upload လုပ်ခြင်း

### 2.1 Upload Interface ကို ဖွင့်ခြင်း

1. Repository page တွင် အလယ်ခြင်း၌ **"uploading an existing file"** link ကို နှိပ်ပါ
2. သို့မဟုတ် **"Add file"** dropdown ကို နှိပ်ပြီး **"Upload files"** ကို ရွေးချယ်ပါ

### 2.2 Files များကို Select လုပ်ခြင်း

1. **"Choose your files"** ကို နှိပ်ပါ
2. အောက်ပါ files များကို select လုပ်ပါ:

```
✓ app.py
✓ utils.py
✓ transcript_extractor.py
✓ ai_processor.py
✓ audio_generator.py
✓ requirements.txt
✓ .env.example
✓ .gitignore
✓ README.md
✓ QUICKSTART.md
✓ API_REFERENCE.md
✓ setup.sh
✓ setup.bat
✓ Dockerfile
✓ docker-compose.yml
✓ .dockerignore
✓ DEPLOYMENT_GUIDE.md
✓ RAILWAY_DEPLOYMENT_STEPS.md
```

**မှတ်ချက်:** ဖုန်းတွင် multiple files select လုပ်ရန်:
- ပထမ file ကို နှိပ်ပါ
- "Select multiple" သို့မဟုတ် "Select all" ကို နှိပ်ပါ
- အခြား files များကို ရွေးချယ်ပါ

### 2.3 Files များကို Upload လုပ်ခြင်း

1. အားလုံး files select ပြီးသည့်နောက် **"Open"** သို့မဟုတ် **"Upload"** ကို နှိပ်ပါ
2. Upload process စတင်မည်ဖြစ်သည်
3. Progress bar ကြည့်ပါ

---

## အဆင့် ၃: Commit လုပ်ခြင်း

### 3.1 Commit Message ကို ထည့်သွင်းခြင်း

Upload ပြီးသည့်နောက် commit page မြင်ရမည်:

1. **"Commit message"** field တွင် အောက်ပါ text ကို ထည့်သွင်းပါ:

```
Initial commit: Movie Recap AI Streamlit app
```

2. (Optional) **"Extended description"** တွင် အောက်ပါ ထည့်သွင်းနိုင်သည်:

```
Add complete Movie Recap AI application with:
- YouTube transcript extraction
- Video/audio file upload
- Gemini AI script generation
- Edge-TTS audio narration
- Docker configuration
- Deployment guides
```

### 3.2 Commit လုပ်ခြင်း

1. **"Commit changes"** ကို နှိပ်ပါ
2. GitHub သည် files များကို process လုပ်မည်ဖြစ်သည်
3. အောင်မြင်ပြီးသည့်နောက် repository page သို့ ပြန်သွားမည်

---

## အဆင့် ၄: Repository အောင်မြင်ခြင်း

### 4.1 Repository ကို ကြည့်ခြင်း

Repository page တွင် အောက်ပါ အရာများ မြင်ရမည်:

```
movie_recap_streamlit

✓ Initial commit: Movie Recap AI Streamlit app

Files:
- app.py
- utils.py
- transcript_extractor.py
- ai_processor.py
- audio_generator.py
- requirements.txt
- README.md
- Dockerfile
- docker-compose.yml
- ... (အခြား files များ)
```

### 4.2 Repository URL ကို ရယူခြင်း

1. **"Code"** ကို နှိပ်ပါ
2. **"HTTPS"** ကို ရွေးချယ်ပါ
3. URL ကို copy လုပ်ပါ:

```
https://github.com/YOUR_USERNAME/movie_recap_streamlit.git
```

---

## အဆင့် ၅: Railway သို့ Deploy လုပ်ခြင်း

### 5.1 Railway Website ကို ဖွင့်ခြင်း

1. ဖုန်းတွင် [railway.app](https://railway.app) သွားပါ
2. **"Login with GitHub"** ကို နှိပ်ပါ
3. သင်၏ GitHub account ဖြင့် login လုပ်ပါ

### 5.2 New Project Create လုပ်ခြင်း

1. Railway dashboard တွင် **"Create New Project"** ကို နှိပ်ပါ
2. **"Deploy from GitHub repo"** ကို ရွေးချယ်ပါ
3. သင်၏ `movie_recap_streamlit` repository ကို ရွေးချယ်ပါ
4. **"Deploy"** ကို နှိပ်ပါ

### 5.3 Environment Variables ထည့်သွင်းခြင်း

1. Railway dashboard တွင် **"Variables"** tab သွားပါ
2. အောက်ပါ variables များကို ထည့်သွင်းပါ:

```
GEMINI_API_KEY = (သင်ရယူထားသည့် API key)
MAX_FILE_SIZE_MB = 500
```

### 5.4 Deployment စောင့်ခြင်း

1. **"Deployments"** tab သွားပါ
2. Build process ကို စောင့်ပါ (5-10 minutes)
3. Status ကြည့်ပါ:
   - 🟡 **Building**
   - 🟢 **Deployed** ✓

---

## အဆင့်ခြင်းအဆင့် ကျဉ်းချုပ်

| အဆင့် | လုပ်ဆောင်ချက် | အချိန် |
|------|-------------|------|
| 1 | GitHub repository create | 2 min |
| 2 | Files များကို upload | 3-5 min |
| 3 | Commit လုပ်ခြင်း | 1 min |
| 4 | Repository အောင်မြင်ခြင်း | အလိုအလျောက် |
| 5 | Railway deploy | 5-10 min |
| **စုစုပေါင်း** | | **11-18 min** |

---

## အကျပ်အတည်းများ နှင့် ဖြေရှင်းချက်

### Q: Upload လုပ်ရန် အချိန်ကြာလွန်းသည်

**A:** အောက်ပါ အရာများ ကြည့်ပါ:
- Internet connection ကို ကြည့်ပါ
- ဖုန်း၏ storage ကို ကြည့်ပါ
- အနည်းငယ် files များကို အစ ခွဲခြားပြီး upload လုပ်ကြည့်ပါ

### Q: "File too large" error ရှိသည်

**A:** GitHub သည် single file အတွက် 100MB limit ရှိသည်။
- အကြီးဆုံး files များကို ခွဲခြားပြီး upload လုပ်ပါ
- သို့မဟုတ် `.gitignore` ကို အသုံးပြုပြီး အကြီးဆုံး files များကို exclude လုပ်ပါ

### Q: Repository မြင်ရမည်ဖြစ်သည်

**A:** အောက်ပါ အရာများ ကြည့်ပါ:
- GitHub သို့ login ခြင်းကို ကြည့်ပါ
- Repository visibility ကို "Public" အဖြစ် ရွေးချယ်ထားသည်ကို ကြည့်ပါ
- Browser cache ကို clear လုပ်ကြည့်ပါ

### Q: Railway deploy fail ဖြစ်သည်

**A:** အောက်ပါ အရာများ ကြည့်ပါ:
- GEMINI_API_KEY ကို ရှင်းလင်းစွာ ထည့်သွင်းထားသည်ကို ကြည့်ပါ
- Railway Logs tab တွင် error message ကို ဖတ်ပါ
- ကျွန်ုပ်ထံ error message ပေးပါ

---

## အောင်မြင်ခြင်း!

အဆင့်များ အားလုံး အောင်မြင်ပြီးသည့်နောက်:

✅ GitHub တွင် သင်၏ code ရှိသည်
✅ Railway တွင် application deploy ဖြစ်သည်
✅ Live URL ရရှိသည်

```
https://movie-recap-ai-production.up.railway.app
```

---

## နောက်လည်ခြင်း

1. Live URL ကို test လုပ်ပါ
2. Gemini API key ထည့်သွင်းထားသည်ကို သိသာစွာ ကြည့်ပါ
3. Application ကို အသုံးပြုကြည့်ပါ
4. အကျပ်အတည်းမျိုး ရှိပါက ကျွန်ုပ်ထံ ကူညီတောင်းခံပါ

---

## အကူအညီ

- **GitHub Help:** [docs.github.com](https://docs.github.com)
- **Railway Help:** [docs.railway.app](https://docs.railway.app)
- **Gemini API:** [aistudio.google.com](https://aistudio.google.com)

**ကျေးဇူးတင်ပါသည်! အောင်မြင်ပါ!** 🎉

---

**Last Updated:** March 31, 2026
