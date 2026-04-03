# Movie Recap AI - Quick Start Guide

Get started with Movie Recap AI in just 5 minutes!

## Installation (5 minutes)

### 1. Install Python Dependencies

```bash
# Navigate to project directory
cd movie_recap_streamlit

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Get Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com)
2. Click "Get API Key"
3. Create a new API key
4. Copy the key

### 3. Configure API Key

Create a `.env` file in the project directory:

```bash
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## First Run: Create Your First Movie Recap (10 minutes)

### Method 1: Paste a Transcript

1. Select "Paste Transcript" from input options
2. Paste your movie transcript
3. Click "Generate Movie Recap Script"
4. Click "Generate Audio Narration"
5. Download your files!

### Method 2: Use a YouTube Video

1. Select "YouTube Video"
2. Paste a YouTube URL
3. Click "Extract Transcript from YouTube"
4. Click "Generate Movie Recap Script"
5. Click "Generate Audio Narration"
6. Download your files!

### Method 3: Upload a Video File

1. Select "Upload Video File"
2. Choose an MP4, MOV, or other video file
3. Click "Extract Transcript from Video"
4. Click "Generate Movie Recap Script"
5. Click "Generate Audio Narration"
6. Download your files!

---

## Configuration Options

### Recap Length
- **Short:** 1–2 minutes (perfect for social media)
- **Medium:** 3–5 minutes (YouTube Shorts, podcasts)
- **Long:** 8–10 minutes (full YouTube videos)

### Narrator Voice
- **Female (Nilar):** Friendly, engaging tone
- **Male (Thiha):** Authoritative, dramatic tone

### Speech Rate
- **0.5x:** Slow, dramatic delivery
- **1.0x:** Normal speed (recommended)
- **2.0x:** Fast, energetic delivery

### Audio Format
- **MP3:** Smaller file size, widely compatible
- **WAV:** Higher quality, larger file size

---

## Common Workflows

### Create a TikTok/Instagram Reel
1. Select "Short" recap length
2. Choose female voice for engaging tone
3. Set speech rate to 1.2x for energy
4. Generate and download MP3
5. Edit with background music in video editor

### Create a Podcast Episode
1. Select "Medium" or "Long" recap length
2. Choose male voice for authority
3. Set speech rate to 0.9x for clarity
4. Generate and download WAV for quality
5. Upload to podcast platform

### Create a YouTube Video
1. Select "Long" recap length
2. Choose your preferred voice
3. Generate script and audio
4. Download both files
5. Add visuals and upload to YouTube

---

## Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| "API key not found" | Create `.env` file with your Gemini API key |
| "FFmpeg not found" | Install FFmpeg: `sudo apt-get install ffmpeg` (Linux) or `brew install ffmpeg` (Mac) |
| "File too large" | Maximum 500MB; compress video using FFmpeg |
| "Slow performance" | First run downloads Whisper model (~1.4GB); this is normal |
| "YouTube extraction fails" | Verify video has captions enabled |

---

## Tips for Best Results

✅ **Do:**
- Use clear, well-punctuated transcripts
- Test different voice options
- Start with medium recap length
- Use normal speech rate (1.0x) initially
- Download both script and audio files

❌ **Don't:**
- Use extremely long transcripts (>5,000 words)
- Upload files larger than 500MB
- Forget to set your API key
- Close the app during processing

---

## Next Steps

1. Create your first movie recap
2. Download the script and audio
3. Edit in your preferred video editor
4. Add background music and visuals
5. Upload to your platform!

---

## Need Help?

- Check the **Help** section in the app sidebar
- Read the full [README.md](README.md) for detailed documentation
- Review the **Troubleshooting** section in the sidebar

---

**Happy recap creating! 🎬**
