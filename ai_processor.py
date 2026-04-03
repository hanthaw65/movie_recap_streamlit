"""
Module for AI-powered script generation using Google Gemini API.
Converts transcripts into engaging Burmese movie recap scripts.
"""

import os
from typing import Optional
import streamlit as st

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


class AIScriptGenerator:
    """Handles AI-powered script generation using Gemini API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the AI script generator.
        
        Args:
            api_key: Gemini API key (if not provided, uses environment variable)
        """
        if not GEMINI_AVAILABLE:
            raise ImportError("google-generativeai is not installed")
        
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "Gemini API key not found. "
                "Please set GEMINI_API_KEY environment variable or pass it as argument."
            )
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_recap_script(
        self,
        transcript: str,
        recap_length: str = 'medium',
        language: str = 'Burmese'
    ) -> Optional[str]:
        """
        Generate a movie recap script from transcript using Gemini AI.
        
        Args:
            transcript: Movie transcript or description
            recap_length: 'short' (1-2 min), 'medium' (3-5 min), or 'long' (8-10 min)
            language: Output language (default: Burmese)
            
        Returns:
            Generated recap script or None if generation fails
        """
        try:
            # Define length specifications
            length_specs = {
                'short': {
                    'words': '150-250 words',
                    'duration': '1-2 minutes',
                    'sentences': 'short, punchy sentences'
                },
                'medium': {
                    'words': '400-600 words',
                    'duration': '3-5 minutes',
                    'sentences': 'engaging, dynamic sentences'
                },
                'long': {
                    'words': '900-1200 words',
                    'duration': '8-10 minutes',
                    'sentences': 'detailed, immersive sentences'
                }
            }
            
            spec = length_specs.get(recap_length, length_specs['medium'])
            
            # Create detailed prompt for Gemini
            prompt = f"""
You are an expert movie narrator and script writer. Your task is to create an engaging, dramatic movie recap script in {language}.

TRANSCRIPT/MOVIE DESCRIPTION:
{transcript}

REQUIREMENTS:
1. Language: Write the entire script in {language}
2. Length: {spec['words']} ({spec['duration']} when read aloud)
3. Tone: Exciting, dramatic, and engaging - like a professional movie trailer narrator
4. Structure: Follow this exact structure:
   - Opening Hook (grab attention immediately)
   - Beginning (introduce main characters and setting)
   - Conflict (build tension with main plot points)
   - Climax (the most dramatic moment)
   - Ending (conclusion and emotional impact)
5. Sentence Style: Use {spec['sentences']}
6. Pacing: Add dramatic pauses (indicated by "..." or line breaks) for effect
7. Emotional Expressions: Include emotional language and dramatic expressions where appropriate
8. Narration Style: Write for audio narration - make it sound natural when read aloud

IMPORTANT:
- Do NOT include stage directions or actions in brackets
- Do NOT include character names in quotation marks
- Write only the narration script that will be read aloud
- Make every word count - no filler content
- Use vivid, descriptive language
- Create a sense of urgency and excitement

Generate the movie recap script now:
"""
            
            # Generate script using Gemini
            response = self.model.generate_content(prompt)
            
            if response and response.text:
                return response.text.strip()
            else:
                raise Exception("No response from Gemini API")
        
        except Exception as e:
            raise Exception(f"Failed to generate recap script: {str(e)}")
    
    def refine_script(
        self,
        script: str,
        refinement_request: str,
        language: str = 'Burmese'
    ) -> Optional[str]:
        """
        Refine an existing script based on user feedback.
        
        Args:
            script: Original script to refine
            refinement_request: User's refinement request
            language: Script language
            
        Returns:
            Refined script or None if refinement fails
        """
        try:
            prompt = f"""
You are an expert movie narrator and script writer. Your task is to refine an existing movie recap script in {language}.

ORIGINAL SCRIPT:
{script}

REFINEMENT REQUEST:
{refinement_request}

Please refine the script according to the user's request while maintaining:
1. The original structure and flow
2. The dramatic, engaging tone
3. Suitability for audio narration
4. The {language} language

Provide only the refined script without any explanations.
"""
            
            response = self.model.generate_content(prompt)
            
            if response and response.text:
                return response.text.strip()
            else:
                raise Exception("No response from Gemini API")
        
        except Exception as e:
            raise Exception(f"Failed to refine script: {str(e)}")
    
    def validate_script(self, script: str) -> dict:
        """
        Validate the generated script for quality and completeness.
        
        Args:
            script: Script to validate
            
        Returns:
            Dictionary with validation results
        """
        results = {
            'word_count': len(script.split()),
            'character_count': len(script),
            'line_count': len(script.split('\n')),
            'has_content': bool(script.strip()),
            'is_valid': bool(script.strip() and len(script.split()) > 50)
        }
        
        return results
