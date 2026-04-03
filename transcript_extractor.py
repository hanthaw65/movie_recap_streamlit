"""
Module for extracting transcripts from various sources.
Supports YouTube videos and local video/audio files.
"""

import os
import tempfile
from pathlib import Path
from typing import Optional, Tuple
import streamlit as st

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    YOUTUBE_API_AVAILABLE = True
except ImportError:
    YOUTUBE_API_AVAILABLE = False

try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False

try:
    from moviepy.editor import VideoFileClip
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False


class TranscriptExtractor:
    """Handles transcript extraction from various sources."""
    
    def __init__(self):
        """Initialize the transcript extractor."""
        self.whisper_model = None
    
    def extract_from_youtube(self, video_id: str, language: str = 'my') -> Optional[str]:
        """
        Extract transcript from YouTube video.
        
        Args:
            video_id: YouTube video ID
            language: Language code (default: 'my' for Burmese)
            
        Returns:
            Transcript text or None if extraction fails
        """
        if not YOUTUBE_API_AVAILABLE:
            raise ImportError("youtube-transcript-api is not installed")
        
        try:
            # Try to get transcript in specified language
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
            
            # Combine all transcript entries into single text
            transcript = ' '.join([entry['text'] for entry in transcript_list])
            return transcript
        
        except Exception as e:
            # Try to get available transcripts
            try:
                transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                
                # Get first available transcript
                if transcript_list.manually_created_transcripts:
                    transcript = transcript_list.manually_created_transcripts[0].fetch()
                elif transcript_list.generated_transcripts:
                    transcript = transcript_list.generated_transcripts[0].fetch()
                else:
                    return None
                
                transcript_text = ' '.join([entry['text'] for entry in transcript])
                return transcript_text
            
            except Exception as inner_e:
                raise Exception(f"Failed to extract YouTube transcript: {str(inner_e)}")
    
    def extract_from_video_file(self, file_path: str) -> Optional[str]:
        """
        Extract audio from video file and transcribe using Whisper.
        
        Args:
            file_path: Path to video file
            
        Returns:
            Transcribed text or None if extraction fails
        """
        if not MOVIEPY_AVAILABLE:
            raise ImportError("moviepy is not installed")
        
        if not WHISPER_AVAILABLE:
            raise ImportError("openai-whisper is not installed")
        
        try:
            # Load Whisper model if not already loaded
            if self.whisper_model is None:
                st.info("Loading Whisper model (this may take a moment on first run)...")
                self.whisper_model = whisper.load_model("base")
            
            # Extract audio from video
            st.info("Extracting audio from video...")
            video = VideoFileClip(file_path)
            
            # Create temporary audio file
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_audio:
                temp_audio_path = temp_audio.name
            
            try:
                video.audio.write_audiofile(
                    temp_audio_path,
                    verbose=False,
                    logger=None
                )
                
                # Transcribe audio
                st.info("Transcribing audio (this may take a few minutes)...")
                result = self.whisper_model.transcribe(temp_audio_path)
                transcript = result['text']
                
                return transcript
            
            finally:
                # Clean up temporary audio file
                if os.path.exists(temp_audio_path):
                    os.remove(temp_audio_path)
                video.close()
        
        except Exception as e:
            raise Exception(f"Failed to extract transcript from video: {str(e)}")
    
    def extract_from_audio_file(self, file_path: str) -> Optional[str]:
        """
        Transcribe audio file using Whisper.
        
        Args:
            file_path: Path to audio file
            
        Returns:
            Transcribed text or None if extraction fails
        """
        if not WHISPER_AVAILABLE:
            raise ImportError("openai-whisper is not installed")
        
        try:
            # Load Whisper model if not already loaded
            if self.whisper_model is None:
                st.info("Loading Whisper model (this may take a moment on first run)...")
                self.whisper_model = whisper.load_model("base")
            
            # Transcribe audio
            st.info("Transcribing audio (this may take a few minutes)...")
            result = self.whisper_model.transcribe(file_path)
            transcript = result['text']
            
            return transcript
        
        except Exception as e:
            raise Exception(f"Failed to transcribe audio file: {str(e)}")
    
    def extract_transcript(
        self,
        source_type: str,
        source_value: str,
        file_path: Optional[str] = None
    ) -> Optional[str]:
        """
        Extract transcript from various sources.
        
        Args:
            source_type: 'youtube', 'video', or 'audio'
            source_value: YouTube URL or video ID (for YouTube), or None for file
            file_path: Path to video/audio file (for 'video' or 'audio' types)
            
        Returns:
            Transcript text or None if extraction fails
        """
        if source_type == 'youtube':
            return self.extract_from_youtube(source_value)
        
        elif source_type == 'video':
            if not file_path:
                raise ValueError("file_path required for video source")
            return self.extract_from_video_file(file_path)
        
        elif source_type == 'audio':
            if not file_path:
                raise ValueError("file_path required for audio source")
            return self.extract_from_audio_file(file_path)
        
        else:
            raise ValueError(f"Unknown source type: {source_type}")
