# API Reference - Movie Recap AI

Complete API documentation for all modules and functions.

## Table of Contents

1. [utils.py](#utilspy)
2. [transcript_extractor.py](#transcript_extractorpy)
3. [ai_processor.py](#ai_processorpy)
4. [audio_generator.py](#audio_generatorpy)

---

## utils.py

Utility functions for file operations, validation, and session management.

### Functions

#### `setup_directories()`

Creates necessary directories for temporary and output files.

```python
from utils import setup_directories

setup_directories()
```

**Parameters:** None

**Returns:** None

**Raises:** OSError if directory creation fails

---

#### `validate_file_size(file_size_bytes: int, max_size_mb: int = 500) -> bool`

Validates if uploaded file is within size limit.

```python
from utils import validate_file_size

is_valid = validate_file_size(file_size_bytes=104857600, max_size_mb=500)
# Returns: True (100MB is within 500MB limit)
```

**Parameters:**
- `file_size_bytes` (int): Size of file in bytes
- `max_size_mb` (int, optional): Maximum allowed size in MB (default: 500)

**Returns:** bool - True if file is within limit, False otherwise

---

#### `validate_file_size(file_size_bytes: int, max_size_mb: int = 500) -> bool`

Validates if uploaded file is within size limit.

**Parameters:**
- `file_size_bytes` (int): Size of file in bytes
- `max_size_mb` (int, optional): Maximum allowed size in MB (default: 500)

**Returns:** bool

---

#### `get_file_extension(filename: str) -> str`

Extract file extension from filename.

```python
ext = get_file_extension("movie.mp4")
# Returns: ".mp4"
```

**Parameters:**
- `filename` (str): Filename to extract extension from

**Returns:** str - File extension including the dot

---

#### `is_valid_video_format(filename: str) -> bool`

Check if file has valid video format.

```python
is_valid = is_valid_video_format("movie.mp4")
# Returns: True
```

**Supported formats:** .mp4, .mov, .avi, .mkv, .flv, .wmv, .webm

**Parameters:**
- `filename` (str): Filename to validate

**Returns:** bool

---

#### `is_valid_audio_format(filename: str) -> bool`

Check if file has valid audio format.

```python
is_valid = is_valid_audio_format("audio.mp3")
# Returns: True
```

**Supported formats:** .mp3, .wav, .m4a, .aac, .flac, .ogg

**Parameters:**
- `filename` (str): Filename to validate

**Returns:** bool

---

#### `extract_youtube_video_id(url: str) -> Optional[str]`

Extract YouTube video ID from various URL formats.

```python
from utils import extract_youtube_video_id

video_id = extract_youtube_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# Returns: "dQw4w9WgXcQ"
```

**Supported URL formats:**
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`

**Parameters:**
- `url` (str): YouTube URL

**Returns:** Optional[str] - Video ID if valid URL, None otherwise

---

#### `format_duration(seconds: float) -> str`

Convert seconds to MM:SS format.

```python
duration = format_duration(125.5)
# Returns: "02:05"
```

**Parameters:**
- `seconds` (float): Duration in seconds

**Returns:** str - Formatted duration (MM:SS)

---

#### `get_recap_length_info(length_type: str) -> Tuple[int, int, str]`

Get recap length specifications.

```python
min_words, max_words, description = get_recap_length_info('medium')
# Returns: (400, 600, '3–5 minutes')
```

**Parameters:**
- `length_type` (str): 'short', 'medium', or 'long'

**Returns:** Tuple[int, int, str] - (min_words, max_words, description)

---

#### `get_burmese_voice_info(voice_type: str) -> Tuple[str, str]`

Get Burmese TTS voice information.

```python
voice_name, display_name = get_burmese_voice_info('female')
# Returns: ('my-MM-NilarNeural', 'Female (Nilar)')
```

**Parameters:**
- `voice_type` (str): 'female' or 'male'

**Returns:** Tuple[str, str] - (voice_name, display_name)

---

#### `save_uploaded_file(uploaded_file, destination_dir: str = "temp_files") -> str`

Save uploaded file to destination directory.

```python
file_path = save_uploaded_file(uploaded_file, "temp_files")
# Returns: "temp_files/movie.mp4"
```

**Parameters:**
- `uploaded_file`: Streamlit UploadedFile object
- `destination_dir` (str, optional): Directory to save file (default: "temp_files")

**Returns:** str - Path to saved file

---

#### `initialize_session_state() -> None`

Initialize Streamlit session state variables.

```python
from utils import initialize_session_state

initialize_session_state()
```

**Initializes:**
- `generated_script`: None
- `audio_file_path`: None
- `transcript`: None
- `processing`: False
- `error_message`: None
- `success_message`: None

---

## transcript_extractor.py

Module for extracting transcripts from various sources.

### Class: TranscriptExtractor

Main class for transcript extraction operations.

#### `__init__()`

Initialize the transcript extractor.

```python
from transcript_extractor import TranscriptExtractor

extractor = TranscriptExtractor()
```

---

#### `extract_from_youtube(video_id: str, language: str = 'my') -> Optional[str]`

Extract transcript from YouTube video.

```python
transcript = extractor.extract_from_youtube('dQw4w9WgXcQ')
# Returns: "Transcript text..."
```

**Parameters:**
- `video_id` (str): YouTube video ID
- `language` (str, optional): Language code (default: 'my' for Burmese)

**Returns:** Optional[str] - Transcript text or None if extraction fails

**Raises:** Exception if extraction fails

---

#### `extract_from_video_file(file_path: str) -> Optional[str]`

Extract audio from video file and transcribe using Whisper.

```python
transcript = extractor.extract_from_video_file('movie.mp4')
# Returns: "Transcribed text..."
```

**Parameters:**
- `file_path` (str): Path to video file

**Returns:** Optional[str] - Transcribed text or None if extraction fails

**Raises:** Exception if extraction fails

**Note:** First run downloads Whisper model (~1.4GB)

---

#### `extract_from_audio_file(file_path: str) -> Optional[str]`

Transcribe audio file using Whisper.

```python
transcript = extractor.extract_from_audio_file('audio.mp3')
# Returns: "Transcribed text..."
```

**Parameters:**
- `file_path` (str): Path to audio file

**Returns:** Optional[str] - Transcribed text or None if extraction fails

**Raises:** Exception if extraction fails

---

#### `extract_transcript(source_type: str, source_value: str, file_path: Optional[str] = None) -> Optional[str]`

Extract transcript from various sources.

```python
# From YouTube
transcript = extractor.extract_transcript('youtube', 'dQw4w9WgXcQ')

# From video file
transcript = extractor.extract_transcript('video', None, 'movie.mp4')

# From audio file
transcript = extractor.extract_transcript('audio', None, 'audio.mp3')
```

**Parameters:**
- `source_type` (str): 'youtube', 'video', or 'audio'
- `source_value` (str): YouTube URL or video ID (for YouTube), or None for file
- `file_path` (str, optional): Path to video/audio file

**Returns:** Optional[str] - Transcript text or None if extraction fails

**Raises:** ValueError if parameters are invalid

---

## ai_processor.py

Module for AI-powered script generation using Gemini API.

### Class: AIScriptGenerator

Main class for script generation operations.

#### `__init__(api_key: Optional[str] = None)`

Initialize the AI script generator.

```python
from ai_processor import AIScriptGenerator

generator = AIScriptGenerator(api_key="your_gemini_api_key")
# Or use environment variable GEMINI_API_KEY
generator = AIScriptGenerator()
```

**Parameters:**
- `api_key` (str, optional): Gemini API key (uses GEMINI_API_KEY env var if not provided)

**Raises:** ImportError if google-generativeai is not installed
**Raises:** ValueError if API key is not provided

---

#### `generate_recap_script(transcript: str, recap_length: str = 'medium', language: str = 'Burmese') -> Optional[str]`

Generate a movie recap script from transcript using Gemini AI.

```python
script = generator.generate_recap_script(
    transcript="Movie transcript here...",
    recap_length="medium",
    language="Burmese"
)
# Returns: "Generated Burmese movie recap script..."
```

**Parameters:**
- `transcript` (str): Movie transcript or description
- `recap_length` (str, optional): 'short', 'medium', or 'long' (default: 'medium')
- `language` (str, optional): Output language (default: 'Burmese')

**Returns:** Optional[str] - Generated script or None if generation fails

**Raises:** Exception if generation fails

**Recap Length Specifications:**
- short: 150–250 words (1–2 minutes)
- medium: 400–600 words (3–5 minutes)
- long: 900–1,200 words (8–10 minutes)

---

#### `refine_script(script: str, refinement_request: str, language: str = 'Burmese') -> Optional[str]`

Refine an existing script based on user feedback.

```python
refined_script = generator.refine_script(
    script="Original script...",
    refinement_request="Make it more dramatic",
    language="Burmese"
)
# Returns: "Refined Burmese movie recap script..."
```

**Parameters:**
- `script` (str): Original script to refine
- `refinement_request` (str): User's refinement request
- `language` (str, optional): Script language (default: 'Burmese')

**Returns:** Optional[str] - Refined script or None if refinement fails

**Raises:** Exception if refinement fails

---

#### `validate_script(script: str) -> dict`

Validate the generated script for quality and completeness.

```python
validation = generator.validate_script(script)
# Returns: {
#     'word_count': 450,
#     'character_count': 2500,
#     'line_count': 15,
#     'has_content': True,
#     'is_valid': True
# }
```

**Parameters:**
- `script` (str): Script to validate

**Returns:** dict - Validation results with keys:
- `word_count` (int): Number of words
- `character_count` (int): Number of characters
- `line_count` (int): Number of lines
- `has_content` (bool): Whether script has content
- `is_valid` (bool): Whether script is valid (>50 words)

---

## audio_generator.py

Module for text-to-speech audio generation using edge-tts.

### Class: AudioGenerator

Main class for audio generation operations.

#### `__init__()`

Initialize the audio generator.

```python
from audio_generator import AudioGenerator

generator = AudioGenerator()
```

**Raises:** ImportError if edge-tts is not installed

---

#### `generate_audio(text: str, voice: str = 'female', output_format: str = 'mp3', output_path: Optional[str] = None, speech_rate: float = 1.0) -> Tuple[str, Optional[str]]`

Generate audio from Burmese text using edge-tts.

```python
file_path, error = generator.generate_audio(
    text="Burmese text here...",
    voice="female",
    output_format="mp3",
    speech_rate=1.0
)

if error:
    print(f"Error: {error}")
else:
    print(f"Audio saved to: {file_path}")
```

**Parameters:**
- `text` (str): Burmese text to convert to speech
- `voice` (str, optional): 'female' or 'male' (default: 'female')
- `output_format` (str, optional): 'mp3' or 'wav' (default: 'mp3')
- `output_path` (str, optional): Path to save audio file (uses temp directory if None)
- `speech_rate` (float, optional): Speech rate multiplier 0.5–2.0 (default: 1.0)

**Returns:** Tuple[str, Optional[str]] - (file_path, error_message)
- file_path: Path to generated audio file
- error_message: Error message if generation failed, None otherwise

**Available Voices:**
- female: my-MM-NilarNeural (Friendly, positive)
- male: my-MM-ThihaNeural (Friendly, positive)

---

#### `get_audio_duration(file_path: str) -> Optional[float]`

Get duration of audio file in seconds.

```python
duration = generator.get_audio_duration('output.mp3')
# Returns: 125.5 (seconds)
```

**Parameters:**
- `file_path` (str): Path to audio file

**Returns:** Optional[float] - Duration in seconds or None if unable to determine

---

#### `validate_text_for_audio(text: str) -> Tuple[bool, str]`

Validate text for audio generation.

```python
is_valid, message = generator.validate_text_for_audio(text)

if is_valid:
    print("Text is ready for audio generation")
else:
    print(f"Validation failed: {message}")
```

**Parameters:**
- `text` (str): Text to validate

**Returns:** Tuple[bool, str] - (is_valid, message)

**Validation Rules:**
- Text cannot be empty
- Minimum 10 characters
- Maximum 10,000 characters

---

#### `get_available_voices() -> dict` (Static Method)

Get available Burmese voices.

```python
voices = AudioGenerator.get_available_voices()
# Returns: {
#     'female': {
#         'name': 'my-MM-NilarNeural',
#         'display_name': 'Female (Nilar)',
#         'description': 'Friendly, positive female voice'
#     },
#     'male': {
#         'name': 'my-MM-ThihaNeural',
#         'display_name': 'Male (Thiha)',
#         'description': 'Friendly, positive male voice'
#     }
# }
```

**Returns:** dict - Available voices with metadata

---

## Usage Examples

### Complete Workflow Example

```python
import os
from dotenv import load_dotenv
from transcript_extractor import TranscriptExtractor
from ai_processor import AIScriptGenerator
from audio_generator import AudioGenerator

# Load environment variables
load_dotenv()

# 1. Extract transcript from YouTube
extractor = TranscriptExtractor()
transcript = extractor.extract_from_youtube('dQw4w9WgXcQ')

# 2. Generate movie recap script
generator = AIScriptGenerator()
script = generator.generate_recap_script(
    transcript=transcript,
    recap_length='medium',
    language='Burmese'
)

# 3. Generate audio narration
audio_gen = AudioGenerator()
audio_path, error = audio_gen.generate_audio(
    text=script,
    voice='female',
    output_format='mp3',
    speech_rate=1.0
)

if error:
    print(f"Error generating audio: {error}")
else:
    print(f"Audio saved to: {audio_path}")
    duration = audio_gen.get_audio_duration(audio_path)
    print(f"Audio duration: {duration} seconds")
```

---

## Error Handling

All modules include comprehensive error handling. Common exceptions:

| Exception | Module | Cause | Solution |
|-----------|--------|-------|----------|
| ImportError | Any | Missing dependency | Install required package |
| ValueError | transcript_extractor | Invalid parameters | Check parameter types |
| Exception | ai_processor | API error | Check API key and internet |
| Exception | audio_generator | TTS error | Check internet connection |

---

## Performance Notes

- **Whisper Model:** ~1.4GB download on first use
- **Script Generation:** 30–60 seconds (depends on transcript length)
- **Audio Generation:** 10–30 seconds (depends on script length)
- **Memory Usage:** 2–4GB recommended

---

## Version

API Reference Version: 1.0.0
Last Updated: March 31, 2026
