# Movie Recap AI - Streamlit Application

**Transform movie transcripts into engaging Burmese movie recap scripts with AI-powered narration.**

## Overview

Movie Recap AI is a comprehensive Streamlit application that automates the creation of professional movie recap content. The application accepts movie transcripts from multiple sources—including YouTube videos, uploaded video files, and audio files—then uses Google's Gemini AI to generate dramatic, engaging Burmese-language scripts. Finally, it synthesizes these scripts into natural-sounding audio narration using Microsoft Edge's text-to-speech technology.

The application is designed for content creators, film enthusiasts, and anyone who wants to create compelling movie recap content without manual scripting or expensive narration services.

## Features

### Core Functionality

**Input Flexibility:** The application supports four distinct input methods to accommodate different user workflows:

- **Direct Transcript Input:** Users can paste movie transcripts or descriptions directly into the application
- **YouTube Integration:** Extract transcripts automatically from YouTube videos using the YouTube Transcript API
- **Video File Upload:** Upload local video files (MP4, MOV, AVI, MKV, FLV, WMV, WebM) up to 500MB, with automatic audio extraction and transcription using OpenAI's Whisper model
- **Audio File Upload:** Upload audio files (MP3, WAV, M4A, AAC, FLAC, OGG) directly for transcription

**AI-Powered Script Generation:** The Gemini API generates movie recap scripts with the following characteristics:

- **Dramatic Tone:** Scripts are written in an exciting, engaging style suitable for professional movie trailers and recaps
- **Customizable Length:** Users can select from three recap lengths:
  - Short: 1–2 minutes (150–250 words)
  - Medium: 3–5 minutes (400–600 words)
  - Long: 8–10 minutes (900–1,200 words)
- **Structured Narrative:** Scripts follow a proven storytelling structure: Opening Hook → Beginning → Conflict → Climax → Ending
- **Burmese Language:** All scripts are generated in Burmese (Myanmar language) with proper linguistic nuance

**Professional Audio Narration:** The application generates high-quality audio narration with these capabilities:

- **Burmese Voices:** Two natural-sounding Burmese voices are available:
  - Female: Nilar (my-MM-NilarNeural)
  - Male: Thiha (my-MM-ThihaNeural)
- **Adjustable Speech Rate:** Users can control narration speed from 0.5x (half speed) to 2.0x (double speed)
- **Multiple Formats:** Audio can be exported as MP3 or WAV files
- **Audio Preview:** Built-in player for immediate playback and quality verification

### User Interface Features

- **Intuitive Layout:** Clean, organized interface with clear sections for each workflow step
- **Real-time Feedback:** Loading spinners, success messages, and error handling throughout the process
- **Script Management:** Copy scripts to clipboard, download as text files, or regenerate with different settings
- **Audio Management:** Download audio files, view duration, and adjust playback settings
- **Sidebar Utilities:** Help documentation, API setup guide, troubleshooting tips, and settings management
- **Session State Management:** Application remembers transcripts, scripts, and audio files during the session
- **Statistics Panel:** Real-time word counts and file size metrics

## Installation & Setup

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.8 or higher:** The application requires Python 3.8+ for compatibility with all dependencies
- **pip or pip3:** Python package manager for installing dependencies
- **FFmpeg:** Required by MoviePy for video processing. Install via:
  - **Ubuntu/Debian:** `sudo apt-get install ffmpeg`
  - **macOS:** `brew install ffmpeg`
  - **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### Step 1: Clone or Download the Project

```bash
# Navigate to your desired directory
cd /path/to/projects

# Clone the repository (if using git)
git clone <repository-url> movie_recap_streamlit
cd movie_recap_streamlit

# Or download and extract the ZIP file, then navigate to the directory
```

### Step 2: Create a Virtual Environment

Creating a virtual environment isolates project dependencies and prevents conflicts with system packages:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip to latest version
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

**Note:** The first installation may take several minutes as it downloads large models (particularly Whisper's base model, approximately 1.4GB).

### Step 4: Configure API Keys

**Gemini API Setup:**

1. Visit [Google AI Studio](https://aistudio.google.com)
2. Click "Get API Key" and create a new API key
3. Copy the API key

**Create `.env` file:**

```bash
# In the project root directory, create a file named .env
# Add the following content:
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here  # Optional, for advanced features
MAX_FILE_SIZE_MB=500
TEMP_DIR=./temp_files
OUTPUT_DIR=./output_files
```

**Alternative: Set Environment Variable Directly**

```bash
# Linux/macOS
export GEMINI_API_KEY="your_gemini_api_key_here"

# Windows (Command Prompt)
set GEMINI_API_KEY=your_gemini_api_key_here

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_gemini_api_key_here"
```

### Step 5: Run the Application

```bash
# Make sure your virtual environment is activated
# Then run:
streamlit run app.py

# The application will open in your default browser at http://localhost:8501
```

## Usage Guide

### Workflow: Creating a Movie Recap

**Step 1: Provide Input**

Choose one of four input methods:

- **Paste Transcript:** Copy-paste a movie transcript or description directly
- **YouTube Video:** Enter a YouTube URL or video ID to extract the transcript automatically
- **Upload Video:** Select a video file from your computer (supports MP4, MOV, AVI, MKV, FLV, WMV, WebM)
- **Upload Audio:** Select an audio file from your computer (supports MP3, WAV, M4A, AAC, FLAC, OGG)

For YouTube and uploaded files, click the extraction button to process the content. The application will display the extracted transcript for verification.

**Step 2: Configure Settings**

In the "AI Processing Settings" section, configure the following:

- **Recap Length:** Select Short (1–2 min), Medium (3–5 min), or Long (8–10 min) based on your needs
- **Narrator Voice:** Choose Female (Nilar) or Male (Thiha) for the audio narration
- **Speech Rate:** Adjust from 0.5x to 2.0x to control narration speed
- **Audio Format:** Select MP3 for smaller file sizes or WAV for higher quality

**Step 3: Generate Script**

Click the "✨ Generate Movie Recap Script" button. The AI will:

1. Analyze the transcript
2. Extract key plot points and emotional beats
3. Generate a dramatic, engaging script in Burmese
4. Format the script for audio narration

The generated script will appear in the "Generated Movie Recap Script" section. Review the script and make any necessary adjustments using the available options.

**Step 4: Generate Audio**

Click the "🎵 Generate Audio Narration" button. The application will:

1. Validate the script
2. Synthesize audio using the selected voice and speech rate
3. Generate the audio file in your chosen format

Once complete, an audio player will appear for immediate playback. You can verify the quality before downloading.

**Step 5: Download and Use**

Download both the script (as a text file) and audio file using the download buttons. Use these files for:

- YouTube video descriptions and scripts
- Podcast episodes
- Social media content
- Educational materials
- Entertainment websites

### Tips for Best Results

**Transcript Quality:** Provide clear, well-punctuated transcripts for better script generation. If using automatic extraction from video, ensure the audio is clear and the video has captions available.

**Recap Length Selection:** Choose the length based on your platform:
- Short: Social media clips (TikTok, Instagram Reels)
- Medium: YouTube Shorts, podcast segments
- Long: Full YouTube videos, detailed recaps

**Voice Selection:** Test both voices to determine which suits your content style. Female voices often work well for dramatic narratives, while male voices can add authority to recaps.

**Speech Rate Adjustment:** Start with 1.0x (normal speed). Increase to 1.2–1.5x for energetic recaps or decrease to 0.8–0.9x for dramatic, slower-paced content.

## Project Structure

```
movie_recap_streamlit/
├── app.py                      # Main Streamlit application
├── utils.py                    # Utility functions (file handling, validation)
├── transcript_extractor.py     # Transcript extraction from various sources
├── ai_processor.py             # Gemini API integration for script generation
├── audio_generator.py          # Edge-TTS integration for audio narration
├── requirements.txt            # Python dependencies
├── .env.example               # Example environment variables
├── README.md                  # This file
└── temp_files/                # Temporary storage for uploaded files
    output_files/              # Generated scripts and audio files
```

### Module Descriptions

**app.py:** The main Streamlit application file containing the user interface, workflow orchestration, and session state management. This file handles all user interactions and coordinates between other modules.

**utils.py:** Provides utility functions for file operations, validation, session state initialization, and helper functions used throughout the application.

**transcript_extractor.py:** Handles transcript extraction from YouTube videos, video files, and audio files using the YouTube Transcript API and OpenAI's Whisper model.

**ai_processor.py:** Integrates with Google's Gemini API to generate movie recap scripts. Includes prompt engineering for optimal script quality and refinement capabilities.

**audio_generator.py:** Manages text-to-speech audio generation using Microsoft Edge's TTS service. Handles voice selection, format conversion, and audio validation.

## Dependencies

The application relies on the following Python packages:

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.40.2 | Web application framework |
| google-generativeai | 0.8.3 | Gemini API integration |
| edge-tts | 7.2.8 | Text-to-speech synthesis |
| moviepy | 1.0.3 | Video file processing |
| youtube-transcript-api | 0.6.2 | YouTube transcript extraction |
| openai-whisper | 20240930 | Audio transcription |
| pydub | 0.25.1 | Audio processing |
| python-dotenv | 1.0.1 | Environment variable management |
| requests | 2.32.3 | HTTP requests |
| Pillow | 11.0.0 | Image processing |
| scipy | 1.14.1 | Audio analysis |

## Troubleshooting

### Issue: "Gemini API key not found"

**Solution:** Ensure the `.env` file exists in the project root directory with the correct API key:

```bash
# Verify the .env file exists
ls -la .env

# Check the content (should contain your API key)
cat .env
```

If the file doesn't exist, create it with your API key as shown in the setup section.

### Issue: "FFmpeg not found"

**Solution:** Install FFmpeg on your system:

- **Ubuntu/Debian:** `sudo apt-get install ffmpeg`
- **macOS:** `brew install ffmpeg`
- **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

### Issue: "File size exceeds 500MB limit"

**Solution:** The application has a 500MB file size limit to prevent memory issues. If your video is larger, compress it using:

```bash
# Using FFmpeg to compress video
ffmpeg -i input_video.mp4 -vcodec libx264 -crf 28 output_video.mp4
```

### Issue: "Whisper model download fails"

**Solution:** The Whisper model (~1.4GB) downloads automatically on first use. Ensure you have:

- Stable internet connection
- At least 2GB of free disk space
- Sufficient time for download (may take 5–10 minutes)

You can pre-download the model:

```bash
python3 -c "import whisper; whisper.load_model('base')"
```

### Issue: "Audio generation fails or takes too long"

**Solution:** Edge-TTS requires an internet connection. Verify:

- Internet connection is stable
- No firewall blocking access to edge-tts servers
- Try with a shorter script first to test connectivity

### Issue: "YouTube transcript extraction fails"

**Solution:** Not all YouTube videos have transcripts available. Verify:

- The video has captions enabled (check YouTube video page)
- The URL is correct and the video is public
- Try using the video upload option instead

### Issue: "Application runs slowly"

**Solution:** Performance depends on:

- **First run:** Whisper model downloads (~1.4GB) - this is normal
- **Script generation:** Gemini API calls may take 30–60 seconds
- **Audio generation:** Depends on script length (typically 10–30 seconds)

To improve performance:

- Use shorter recap lengths
- Close other applications to free up memory
- Ensure stable internet connection

## Advanced Configuration

### Custom Model Settings

To use different Whisper models, edit `transcript_extractor.py`:

```python
# Change from 'base' to 'small', 'medium', 'large'
self.whisper_model = whisper.load_model("small")  # More accurate but slower
```

### Adjusting File Size Limits

Edit `.env` to change the maximum file size:

```bash
MAX_FILE_SIZE_MB=1000  # Increase to 1GB
```

### Custom Output Directory

Change where files are saved by editing `.env`:

```bash
OUTPUT_DIR=/path/to/custom/directory
TEMP_DIR=/path/to/temp/directory
```

## Performance Considerations

**Memory Usage:** The application requires approximately 2–4GB of RAM for optimal performance, particularly when processing video files with Whisper transcription.

**Processing Time:** Typical processing times are:

- YouTube transcript extraction: 5–10 seconds
- Video transcription (Whisper): 2–5 minutes (depends on video length)
- Script generation (Gemini): 30–60 seconds
- Audio generation (Edge-TTS): 10–30 seconds (depends on script length)

**Internet Bandwidth:** The application requires internet connectivity for:

- Gemini API calls
- Edge-TTS audio generation
- YouTube transcript extraction
- Model downloads (first run only)

## Limitations

- **File Size:** Maximum 500MB for video/audio uploads
- **Transcript Length:** Optimal performance with transcripts up to 5,000 words
- **Language:** Currently optimized for Burmese (Myanmar) language output
- **API Rate Limits:** Subject to Gemini API rate limits (check Google's documentation)
- **Audio Duration:** Generated audio files typically range from 1–10 minutes

## Security & Privacy

- **API Keys:** Never commit `.env` files to version control. Add to `.gitignore`
- **Temporary Files:** The application stores temporary files in `temp_files/` directory. These are not automatically deleted; use the "Clean Temporary Files" button in the sidebar
- **Data Storage:** Generated scripts and audio files are stored locally in `output_files/` directory
- **No Data Transmission:** Except for API calls to Gemini and Edge-TTS, no data is sent to external servers

## Future Enhancements

Potential improvements for future versions include:

- Support for additional languages beyond Burmese
- Background music integration for audio narration
- Custom voice training and cloning
- Batch processing for multiple videos
- Integration with YouTube upload automation
- Advanced script refinement with user feedback loops
- Support for multiple narrator voices in a single script
- Video generation with synchronized subtitles

## Contributing

To contribute improvements to this project:

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes and test thoroughly
3. Commit with clear messages: `git commit -m "Add feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request with detailed description

## License

This project is provided as-is for educational and commercial use. Modify and distribute as needed.

## Support & Feedback

For issues, questions, or feature requests:

1. Check the Troubleshooting section above
2. Review the Help documentation in the application sidebar
3. Check error messages and logs for specific issues
4. Verify API keys and internet connectivity

## Changelog

**Version 1.0.0 (Initial Release)**

- Core functionality for transcript extraction from multiple sources
- AI-powered script generation using Gemini API
- Text-to-speech audio generation with Burmese voice support
- Streamlit-based user interface with comprehensive features
- Full documentation and troubleshooting guide

## Author

**Manus AI** - AI-powered application development platform

---

**Last Updated:** March 31, 2026

For the latest version and updates, visit the project repository.
