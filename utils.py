"""
Utility functions for the Movie Recap application.
Handles file operations, validation, and common tasks.
"""

import os
import re
from pathlib import Path
from typing import Optional, Tuple
import streamlit as st


def setup_directories() -> None:
    """Create necessary directories for temporary and output files."""
    temp_dir = Path("temp_files")
    output_dir = Path("output_files")
    
    temp_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)


def validate_file_size(file_size_bytes: int, max_size_mb: int = 500) -> bool:
    """
    Validate if uploaded file is within size limit.
    
    Args:
        file_size_bytes: Size of file in bytes
        max_size_mb: Maximum allowed size in MB
        
    Returns:
        True if file is within limit, False otherwise
    """
    max_size_bytes = max_size_mb * 1024 * 1024
    return file_size_bytes <= max_size_bytes


def get_file_extension(filename: str) -> str:
    """Extract file extension from filename."""
    return Path(filename).suffix.lower()


def is_valid_video_format(filename: str) -> bool:
    """Check if file has valid video format."""
    valid_formats = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm'}
    return get_file_extension(filename) in valid_formats


def is_valid_audio_format(filename: str) -> bool:
    """Check if file has valid audio format."""
    valid_formats = {'.mp3', '.wav', '.m4a', '.aac', '.flac', '.ogg'}
    return get_file_extension(filename) in valid_formats


def extract_youtube_video_id(url: str) -> Optional[str]:
    """
    Extract YouTube video ID from various URL formats.
    
    Args:
        url: YouTube URL
        
    Returns:
        Video ID if valid URL, None otherwise
    """
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
        r'youtube\.com\/watch\?.*v=([^&\n?#]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None


def format_duration(seconds: float) -> str:
    """Convert seconds to MM:SS format."""
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"


def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to specified length with ellipsis."""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


def clean_filename(filename: str) -> str:
    """Remove invalid characters from filename."""
    # Replace spaces and invalid characters with underscores
    filename = re.sub(r'[^\w\s.-]', '', filename)
    filename = re.sub(r'[\s]+', '_', filename)
    return filename


def get_recap_length_info(length_type: str) -> Tuple[int, int, str]:
    """
    Get recap length specifications.
    
    Args:
        length_type: 'short', 'medium', or 'long'
        
    Returns:
        Tuple of (min_words, max_words, description)
    """
    lengths = {
        'short': (150, 250, '1–2 minutes'),
        'medium': (400, 600, '3–5 minutes'),
        'long': (900, 1200, '8–10 minutes'),
    }
    return lengths.get(length_type, (400, 600, '3–5 minutes'))


def get_burmese_voice_info(voice_type: str) -> Tuple[str, str]:
    """
    Get Burmese TTS voice information.
    
    Args:
        voice_type: 'female' or 'male'
        
    Returns:
        Tuple of (voice_name, display_name)
    """
    voices = {
        'female': ('my-MM-NilarNeural', 'Female (Nilar)'),
        'male': ('my-MM-ThihaNeural', 'Male (Thiha)'),
    }
    return voices.get(voice_type, ('my-MM-NilarNeural', 'Female (Nilar)'))


def save_uploaded_file(uploaded_file, destination_dir: str = "temp_files") -> str:
    """
    Save uploaded file to destination directory.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        destination_dir: Directory to save file
        
    Returns:
        Path to saved file
    """
    Path(destination_dir).mkdir(exist_ok=True)
    file_path = os.path.join(destination_dir, uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path


def cleanup_temp_files(directory: str = "temp_files", keep_count: int = 5) -> None:
    """
    Clean up old temporary files, keeping only the most recent ones.
    
    Args:
        directory: Directory to clean
        keep_count: Number of recent files to keep
    """
    try:
        path = Path(directory)
        if not path.exists():
            return
        
        files = sorted(path.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True)
        
        for file in files[keep_count:]:
            if file.is_file():
                file.unlink()
    except Exception as e:
        print(f"Error cleaning up temp files: {e}")


def initialize_session_state() -> None:
    """Initialize Streamlit session state variables."""
    if 'generated_script' not in st.session_state:
        st.session_state.generated_script = None
    
    if 'audio_file_path' not in st.session_state:
        st.session_state.audio_file_path = None
    
    if 'transcript' not in st.session_state:
        st.session_state.transcript = None
    
    if 'processing' not in st.session_state:
        st.session_state.processing = False
    
    if 'error_message' not in st.session_state:
        st.session_state.error_message = None
    
    if 'success_message' not in st.session_state:
        st.session_state.success_message = None
