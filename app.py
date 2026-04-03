"""
Movie Recap AI - Streamlit Application
Convert YouTube transcripts or video files into engaging Burmese movie recap scripts with audio narration.

Author: Manus AI
Version: 1.0.0
"""

import os
import sys
import base64
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

# Import custom modules
from utils import (
    setup_directories,
    validate_file_size,
    is_valid_video_format,
    is_valid_audio_format,
    extract_youtube_video_id,
    format_duration,
    truncate_text,
    clean_filename,
    get_recap_length_info,
    get_burmese_voice_info,
    save_uploaded_file,
    cleanup_temp_files,
    initialize_session_state
)
from transcript_extractor import TranscriptExtractor
from ai_processor import AIScriptGenerator
from audio_generator import AudioGenerator


# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Movie Recap AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Header styling */
    .header-container {
        text-align: center;
        margin-bottom: 2rem;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        color: white;
    }
    
    .header-container h1 {
        margin: 0;
        font-size: 2.5rem;
    }
    
    .header-container p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Section styling */
    .section-container {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        border-left: 4px solid #667eea;
    }
    
    .section-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 1rem;
    }
    
    /* Status messages */
    .status-success {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .status-error {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .status-info {
        background: #d1ecf1;
        color: #0c5460;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        padding: 0.75rem;
        font-weight: 600;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    
    /* Script display */
    .script-container {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin: 1rem 0;
        max-height: 400px;
        overflow-y: auto;
    }
    
    /* Audio player container */
    .audio-container {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin: 1rem 0;
    }
    
    /* Loading spinner */
    .loading-spinner {
        text-align: center;
        padding: 2rem;
    }
    
    /* Sidebar styling */
    .sidebar-section {
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


def display_header():
    """Display application header."""
    st.markdown("""
    <div class="header-container">
        <h1>🎬 Movie Recap AI</h1>
        <p>Transform transcripts into engaging Burmese movie recaps with AI-powered narration</p>
    </div>
    """, unsafe_allow_html=True)


def display_input_section():
    """Display input options section."""
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📝 Input Options</h2>', unsafe_allow_html=True)
    
    input_type = st.radio(
        "Choose input method:",
        ["Paste Transcript", "YouTube Video", "Upload Video File", "Upload Audio File"],
        horizontal=True
    )
    
    transcript = None
    
    if input_type == "Paste Transcript":
        st.markdown("**Paste your movie transcript or description below:**")
        transcript = st.text_area(
            "Transcript",
            height=150,
            placeholder="Paste the movie transcript or description here...",
            label_visibility="collapsed"
        )
    
    elif input_type == "YouTube Video":
        st.markdown("**Enter YouTube video URL or ID:**")
        youtube_input = st.text_input(
            "YouTube URL or Video ID",
            placeholder="https://www.youtube.com/watch?v=... or video_id",
            label_visibility="collapsed"
        )
        
        if youtube_input:
            if st.button("🔗 Extract Transcript from YouTube"):
                try:
                    with st.spinner("Extracting transcript from YouTube..."):
                        extractor = TranscriptExtractor()
                        video_id = extract_youtube_video_id(youtube_input) or youtube_input
                        transcript = extractor.extract_from_youtube(video_id)
                        
                        if transcript:
                            st.session_state.transcript = transcript
                            st.success("✅ Transcript extracted successfully!")
                            st.session_state.success_message = "Transcript extracted successfully!"
                        else:
                            st.error("❌ Could not extract transcript. Please check the URL.")
                
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.session_state.error_message = str(e)
    
    elif input_type == "Upload Video File":
        st.markdown("**Upload a video file (MP4, MOV, AVI, MKV - max 500MB):**")
        uploaded_video = st.file_uploader(
            "Video file",
            type=['mp4', 'mov', 'avi', 'mkv', 'flv', 'wmv', 'webm'],
            label_visibility="collapsed"
        )
        
        if uploaded_video:
            if validate_file_size(uploaded_video.size):
                if st.button("🎥 Extract Transcript from Video"):
                    try:
                        with st.spinner("Processing video file..."):
                            file_path = save_uploaded_file(uploaded_video)
                            extractor = TranscriptExtractor()
                            transcript = extractor.extract_from_video_file(file_path)
                            
                            if transcript:
                                st.session_state.transcript = transcript
                                st.success("✅ Transcript extracted successfully!")
                                st.session_state.success_message = "Transcript extracted successfully!"
                            else:
                                st.error("❌ Could not extract transcript from video.")
                    
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        st.session_state.error_message = str(e)
            else:
                st.error(f"❌ File size exceeds 500MB limit. Current size: {uploaded_video.size / (1024*1024):.2f}MB")
    
    elif input_type == "Upload Audio File":
        st.markdown("**Upload an audio file (MP3, WAV, M4A, AAC, FLAC - max 500MB):**")
        uploaded_audio = st.file_uploader(
            "Audio file",
            type=['mp3', 'wav', 'm4a', 'aac', 'flac', 'ogg'],
            label_visibility="collapsed"
        )
        
        if uploaded_audio:
            if validate_file_size(uploaded_audio.size):
                if st.button("🎵 Extract Transcript from Audio"):
                    try:
                        with st.spinner("Processing audio file..."):
                            file_path = save_uploaded_file(uploaded_audio)
                            extractor = TranscriptExtractor()
                            transcript = extractor.extract_from_audio_file(file_path)
                            
                            if transcript:
                                st.session_state.transcript = transcript
                                st.success("✅ Transcript extracted successfully!")
                                st.session_state.success_message = "Transcript extracted successfully!"
                            else:
                                st.error("❌ Could not extract transcript from audio.")
                    
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        st.session_state.error_message = str(e)
            else:
                st.error(f"❌ File size exceeds 500MB limit. Current size: {uploaded_audio.size / (1024*1024):.2f}MB")
    
    # Display current transcript
    if st.session_state.transcript:
        st.markdown("---")
        with st.expander("📄 View Current Transcript"):
            st.text_area(
                "Current Transcript",
                value=st.session_state.transcript,
                height=150,
                disabled=True,
                label_visibility="collapsed"
            )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return transcript or st.session_state.transcript


def display_processing_section(transcript):
    """Display AI processing section."""
    if not transcript:
        st.info("👆 Please provide a transcript first to generate a recap script.")
        return None
    
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">⚙️ AI Processing Settings</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        recap_length = st.selectbox(
            "Recap Length",
            ["short", "medium", "long"],
            format_func=lambda x: {
                "short": "📹 Short (1-2 minutes)",
                "medium": "📹 Medium (3-5 minutes)",
                "long": "📹 Long (8-10 minutes)"
            }[x]
        )
    
    with col2:
        voice_choice = st.selectbox(
            "Narrator Voice",
            ["female", "male"],
            format_func=lambda x: {
                "female": "👩 Female (Nilar)",
                "male": "👨 Male (Thiha)"
            }[x]
        )
    
    st.markdown("---")
    st.markdown("**Advanced Options:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        speech_rate = st.slider(
            "Speech Rate",
            min_value=0.5,
            max_value=2.0,
            value=1.0,
            step=0.1,
            help="0.5 = Half speed, 1.0 = Normal, 2.0 = Double speed"
        )
    
    with col2:
        audio_format = st.selectbox(
            "Audio Format",
            ["mp3", "wav"],
            format_func=lambda x: f"🔊 {x.upper()}"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Generate script button
    if st.button("✨ Generate Movie Recap Script", use_container_width=True, type="primary"):
        try:
            st.session_state.processing = True
            
            with st.spinner("🤖 Generating script using AI..."):
                api_key = os.getenv('GEMINI_API_KEY')
                if not api_key:
                    st.error("❌ Gemini API key not found. Please set GEMINI_API_KEY environment variable.")
                    return None
                
                generator = AIScriptGenerator(api_key)
                script = generator.generate_recap_script(
                    transcript,
                    recap_length=recap_length,
                    language='Burmese'
                )
                
                if script:
                    st.session_state.generated_script = script
                    st.session_state.success_message = "✅ Script generated successfully!"
                    st.success("✅ Script generated successfully!")
                else:
                    st.error("❌ Failed to generate script.")
                    st.session_state.error_message = "Failed to generate script."
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.session_state.error_message = str(e)
        
        finally:
            st.session_state.processing = False
    
    return recap_length, voice_choice, speech_rate, audio_format


def display_script_section():
    """Display generated script section."""
    if not st.session_state.generated_script:
        return
    
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📖 Generated Movie Recap Script</h2>', unsafe_allow_html=True)
    
    # Display script
    with st.container(border=True):
        st.markdown("**Burmese Movie Recap Script:**")
        st.text_area(
            "Script",
            value=st.session_state.generated_script,
            height=250,
            disabled=True,
            label_visibility="collapsed"
        )
    
    # Script actions
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📋 Copy Script to Clipboard", use_container_width=True):
            st.write("✅ Script copied! (Use Ctrl+V or Cmd+V to paste)")
            # Note: Streamlit doesn't have native clipboard support, but this message helps
    
    with col2:
        script_filename = f"movie_recap_{clean_filename('script')}.txt"
        st.download_button(
            label="⬇️ Download Script",
            data=st.session_state.generated_script,
            file_name=script_filename,
            mime="text/plain",
            use_container_width=True
        )
    
    with col3:
        if st.button("🔄 Regenerate Script", use_container_width=True):
            st.session_state.generated_script = None
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)


def display_audio_section(recap_length, voice_choice, speech_rate, audio_format):
    """Display audio generation section."""
    if not st.session_state.generated_script:
        return
    
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🎙️ Audio Generation</h2>', unsafe_allow_html=True)
    
    if st.button("🎵 Generate Audio Narration", use_container_width=True, type="primary"):
        try:
            with st.spinner("🎙️ Generating audio narration..."):
                generator = AudioGenerator()
                
                # Validate text
                is_valid, message = generator.validate_text_for_audio(st.session_state.generated_script)
                if not is_valid:
                    st.error(f"❌ {message}")
                    return
                
                # Generate audio
                output_path, error = generator.generate_audio(
                    text=st.session_state.generated_script,
                    voice=voice_choice,
                    output_format=audio_format,
                    speech_rate=speech_rate
                )
                
                if error:
                    st.error(f"❌ {error}")
                    st.session_state.error_message = error
                else:
                    st.session_state.audio_file_path = output_path
                    st.success("✅ Audio generated successfully!")
                    st.session_state.success_message = "Audio generated successfully!"
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.session_state.error_message = str(e)
    
    # Display audio player if available
    if st.session_state.audio_file_path and os.path.exists(st.session_state.audio_file_path):
        st.markdown("---")
        st.markdown("**Audio Player:**")
        
        with open(st.session_state.audio_file_path, 'rb') as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format=f"audio/{st.session_state.audio_file_path.split('.')[-1]}")
        
        # Audio download button
        audio_filename = f"movie_recap_{clean_filename('audio')}.{st.session_state.audio_file_path.split('.')[-1]}"
        st.download_button(
            label="⬇️ Download Audio",
            data=audio_bytes,
            file_name=audio_filename,
            mime=f"audio/{st.session_state.audio_file_path.split('.')[-1]}",
            use_container_width=True
        )
        
        # Get audio duration
        generator = AudioGenerator()
        duration = generator.get_audio_duration(st.session_state.audio_file_path)
        if duration:
            st.info(f"⏱️ Audio Duration: {format_duration(duration)}")
    
    st.markdown('</div>', unsafe_allow_html=True)


def display_sidebar():
    """Display sidebar information and settings."""
    with st.sidebar:
        st.markdown("### 📚 About")
        st.markdown("""
        **Movie Recap AI** converts movie transcripts into engaging Burmese movie recap scripts 
        with natural-sounding audio narration.
        
        **Features:**
        - 🎬 Extract transcripts from YouTube videos
        - 📹 Upload video/audio files for transcription
        - 🤖 AI-powered script generation using Gemini
        - 🎙️ Natural Burmese text-to-speech narration
        - 📥 Download scripts and audio files
        """)
        
        st.markdown("---")
        st.markdown("### ⚙️ Settings")
        
        # Dark mode toggle
        dark_mode = st.checkbox("🌙 Dark Mode", value=False)
        
        # Cleanup option
        if st.button("🗑️ Clean Temporary Files"):
            cleanup_temp_files()
            st.success("✅ Temporary files cleaned!")
        
        st.markdown("---")
        st.markdown("### 📖 Help")
        
        with st.expander("❓ How to use"):
            st.markdown("""
            1. **Choose Input Method:**
               - Paste a transcript directly
               - Enter a YouTube video URL
               - Upload a video file (MP4, MOV, etc.)
               - Upload an audio file (MP3, WAV, etc.)
            
            2. **Configure Settings:**
               - Select recap length (short/medium/long)
               - Choose narrator voice (female/male)
               - Adjust speech rate if needed
            
            3. **Generate Script:**
               - Click "Generate Movie Recap Script"
               - Wait for AI to create the script
            
            4. **Generate Audio:**
               - Click "Generate Audio Narration"
               - Listen to the preview
               - Download the audio file
            """)
        
        with st.expander("🔑 API Setup"):
            st.markdown("""
            **Required:**
            - Gemini API Key (from Google AI Studio)
            
            **Setup:**
            1. Get your Gemini API key from [Google AI Studio](https://aistudio.google.com)
            2. Create a `.env` file in the project directory
            3. Add: `GEMINI_API_KEY=your_key_here`
            4. Restart the Streamlit app
            """)
        
        with st.expander("⚠️ Troubleshooting"):
            st.markdown("""
            **Issue:** API key not found
            - Solution: Create `.env` file with `GEMINI_API_KEY=your_key`
            
            **Issue:** Video too large
            - Solution: Maximum file size is 500MB
            
            **Issue:** Transcription taking too long
            - Solution: Whisper model downloads on first use (~1.4GB)
            
            **Issue:** Audio generation fails
            - Solution: Check internet connection (edge-tts requires online access)
            """)


def main():
    """Main application function."""
    # Setup
    setup_directories()
    initialize_session_state()
    
    # Display header
    display_header()
    
    # Display sidebar
    display_sidebar()
    
    # Main content
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Input section
        transcript = display_input_section()
        
        # Processing section
        if transcript:
            processing_results = display_processing_section(transcript)
            
            if processing_results:
                recap_length, voice_choice, speech_rate, audio_format = processing_results
                
                # Script section
                display_script_section()
                
                # Audio section
                display_audio_section(recap_length, voice_choice, speech_rate, audio_format)
    
    with col2:
        st.markdown("### 📊 Stats")
        
        if st.session_state.transcript:
            word_count = len(st.session_state.transcript.split())
            st.metric("Transcript Words", word_count)
        
        if st.session_state.generated_script:
            word_count = len(st.session_state.generated_script.split())
            st.metric("Script Words", word_count)
        
        if st.session_state.audio_file_path and os.path.exists(st.session_state.audio_file_path):
            file_size = os.path.getsize(st.session_state.audio_file_path) / (1024 * 1024)
            st.metric("Audio Size (MB)", f"{file_size:.2f}")


if __name__ == "__main__":
    main()
