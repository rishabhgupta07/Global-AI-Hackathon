#!/bin/bash

# Professional Setup Script for NeutralizeAI
echo "🚀 Starting environment setup..."

# 1. Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "✅ Virtual environment created."
else
    echo "ℹ️  Virtual environment already exists."
fi

# 2. Activate and install dependencies
echo "📦 Installing packages from requirements.txt..."
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 3. Final verification
echo "🔍 Verifying Streamlit installation..."
if python -c "import streamlit" &> /dev/null; then
    echo "✅ Setup Complete! To start your app, run:"
    echo "   source .venv/bin/activate"
    echo "   streamlit run app.py"
else
    echo "❌ Setup failed. Please check your internet connection."
fi