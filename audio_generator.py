"""
Module for text-to-speech audio generation using edge-tts.
Converts Burmese scripts into natural-sounding audio narration.
"""

import os
import asyncio
from pathlib import Path
from typing import Optional, Tuple
import streamlit as st

try:
    import edge_tts
    EDGE_TTS_AVAILABLE = True
except ImportError:
    EDGE_TTS_AVAILABLE = False


class AudioGenerator:
    """Handles text-to-speech audio generation using edge-tts."""
    
    # Available Burmese voices
    BURMESE_VOICES = {
        'female': 'my-MM-NilarNeural',
        'male': 'my-MM-ThihaNeural',
    }
    
    # Supported output formats
    SUPPORTED_FORMATS = ['mp3', 'wav']
    
    def __init__(self):
        """Initialize the audio generator."""
        if not EDGE_TTS_AVAILABLE:
            raise ImportError("edge-tts is not installed")
    
    def generate_audio(
        self,
        text: str,
        voice: str = 'female',
        output_format: str = 'mp3',
        output_path: Optional[str] = None,
        speech_rate: float = 1.0
    ) -> Tuple[str, Optional[str]]:
        """
        Generate audio from Burmese text using edge-tts.
        
        Args:
            text: Burmese text to convert to speech
            voice: 'female' or 'male'
            output_format: 'mp3' or 'wav'
            output_path: Path to save audio file (if None, uses temp directory)
            speech_rate: Speech rate multiplier (0.5 = half speed, 1.0 = normal, 2.0 = double speed)
            
        Returns:
            Tuple of (file_path, error_message)
            - file_path: Path to generated audio file
            - error_message: Error message if generation failed, None otherwise
        """
        try:
            # Validate inputs
            if not text or not text.strip():
                return None, "Text cannot be empty"
            
            if voice not in self.BURMESE_VOICES:
                return None, f"Invalid voice. Choose from: {', '.join(self.BURMESE_VOICES.keys())}"
            
            if output_format not in self.SUPPORTED_FORMATS:
                return None, f"Invalid format. Supported: {', '.join(self.SUPPORTED_FORMATS)}"
            
            if speech_rate < 0.5 or speech_rate > 2.0:
                return None, "Speech rate must be between 0.5 and 2.0"
            
            # Select voice
            voice_name = self.BURMESE_VOICES[voice]
            
            # Generate output path if not provided
            if output_path is None:
                Path("output_files").mkdir(exist_ok=True)
                output_path = f"output_files/recap_audio.{output_format}"
            
            # Convert format to edge-tts format
            if output_format == 'mp3':
                edge_format = "audio-16khz-32kbitrate-mono-mp3"
            else:  # wav
                edge_format = "audio-16khz-16bit-mono-pcm"
            
            # Adjust speech rate for edge-tts (format: +20% or -20%)
            rate_adjustment = f"{int((speech_rate - 1.0) * 100):+d}%"
            
            # Run async audio generation
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            try:
                loop.run_until_complete(
                    self._generate_audio_async(
                        text,
                        voice_name,
                        edge_format,
                        output_path,
                        rate_adjustment
                    )
                )
            finally:
                loop.close()
            
            # Verify file was created
            if os.path.exists(output_path):
                file_size = os.path.getsize(output_path)
                if file_size > 0:
                    return output_path, None
                else:
                    return None, "Generated audio file is empty"
            else:
                return None, "Failed to create audio file"
        
        except Exception as e:
            return None, f"Audio generation error: {str(e)}"
    
    async def _generate_audio_async(
        self,
        text: str,
        voice: str,
        audio_format: str,
        output_path: str,
        rate: str
    ) -> None:
        """
        Asynchronously generate audio using edge-tts.
        
        Args:
            text: Text to convert
            voice: Voice name
            audio_format: Audio format
            output_path: Output file path
            rate: Speech rate adjustment
        """
        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate=rate
        )
        
        await communicate.save(output_path)
    
    def get_audio_duration(self, file_path: str) -> Optional[float]:
        """
        Get duration of audio file in seconds.
        
        Args:
            file_path: Path to audio file
            
        Returns:
            Duration in seconds or None if unable to determine
        """
        try:
            from scipy.io import wavfile
            import numpy as np
            
            if file_path.endswith('.wav'):
                sample_rate, data = wavfile.read(file_path)
                duration = len(data) / sample_rate
                return duration
            
            elif file_path.endswith('.mp3'):
                # For MP3, we can use a simple estimation based on file size
                # MP3 typically uses 128 kbps, so: duration = file_size / (128000 / 8)
                file_size = os.path.getsize(file_path)
                estimated_duration = (file_size * 8) / 128000
                return estimated_duration
            
            return None
        
        except Exception as e:
            print(f"Error getting audio duration: {e}")
            return None
    
    def validate_text_for_audio(self, text: str) -> Tuple[bool, str]:
        """
        Validate text for audio generation.
        
        Args:
            text: Text to validate
            
        Returns:
            Tuple of (is_valid, message)
        """
        if not text or not text.strip():
            return False, "Text cannot be empty"
        
        if len(text) < 10:
            return False, "Text is too short (minimum 10 characters)"
        
        if len(text) > 10000:
            return False, "Text is too long (maximum 10000 characters)"
        
        return True, "Text is valid for audio generation"
    
    @staticmethod
    def get_available_voices() -> dict:
        """
        Get available Burmese voices.
        
        Returns:
            Dictionary of available voices
        """
        return {
            'female': {
                'name': 'my-MM-NilarNeural',
                'display_name': 'Female (Nilar)',
                'description': 'Friendly, positive female voice'
            },
            'male': {
                'name': 'my-MM-ThihaNeural',
                'display_name': 'Male (Thiha)',
                'description': 'Friendly, positive male voice'
            }
        }
