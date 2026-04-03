#!/bin/bash

# Movie Recap AI - Setup Script
# This script automates the installation and setup process

set -e  # Exit on error

echo "================================"
echo "Movie Recap AI - Setup Script"
echo "================================"
echo ""

# Check Python version
echo "✓ Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "✗ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo "  Found Python $PYTHON_VERSION"

# Check FFmpeg
echo ""
echo "✓ Checking FFmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠ FFmpeg is not installed. Installing FFmpeg..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update
        sudo apt-get install -y ffmpeg
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew &> /dev/null; then
            echo "✗ Homebrew is not installed. Please install Homebrew first."
            exit 1
        fi
        brew install ffmpeg
    else
        echo "⚠ Please install FFmpeg manually for your OS"
    fi
else
    FFMPEG_VERSION=$(ffmpeg -version | head -n 1)
    echo "  Found: $FFMPEG_VERSION"
fi

# Create virtual environment
echo ""
echo "✓ Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "  Virtual environment created"
else
    echo "  Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "✓ Activating virtual environment..."
source venv/bin/activate
echo "  Virtual environment activated"

# Upgrade pip
echo ""
echo "✓ Upgrading pip..."
pip install --upgrade pip --quiet

# Install dependencies
echo ""
echo "✓ Installing dependencies..."
echo "  This may take several minutes..."
pip install -r requirements.txt --quiet

# Create .env file if it doesn't exist
echo ""
echo "✓ Checking configuration..."
if [ ! -f ".env" ]; then
    echo "  Creating .env file from template..."
    cp .env.example .env
    echo "  ⚠ Please edit .env and add your Gemini API key"
else
    echo "  .env file already exists"
fi

# Create necessary directories
echo ""
echo "✓ Creating directories..."
mkdir -p temp_files output_files
echo "  Directories created"

# Final message
echo ""
echo "================================"
echo "✓ Setup Complete!"
echo "================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your Gemini API key:"
echo "   nano .env"
echo ""
echo "2. Run the application:"
echo "   streamlit run app.py"
echo ""
echo "3. Open your browser to http://localhost:8501"
echo ""
echo "For more information, see README.md or QUICKSTART.md"
echo ""
