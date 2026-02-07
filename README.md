# AntibiasAI: The Debiasing Engine

**AntibiasAI** is a high-speed linguistic analysis tool built for the **Global AI Hackathon 2026** organized by MIT. It leverages Gemini 2.5 Flash to identify, quantify, and neutralize ideological bias.

## The Venture Pitch
Traditional news/articles is often framed with selective language that distorts objective reality. **AntibiasAI** provides a "Linguistic Fingerprint" of any article, allowing researchers, corporate intelligence teams, and casual readers to strip away the "noise" and focus on the facts.

## Key Features
* **AI-Powered Debiasing:** Uses Gemini 2.5 Flash to rewrite biased narratives into neutral prose.
* **Bias Fingerprinting:** A Radar Chart visualization that measures Political Leaning, Sensationalism, Subjectivity, Omission, and Tone.
* **Streamlined Workflow:** A professional dashboard for side-by-side analysis.

## Tech Stack
* **Language:** Python 3.9+
* **Framework:** [Streamlit](https://streamlit.io/)
* **AI Model:** Google Gemini 2.5 Flash
* **Visualization:** [Plotly](https://plotly.com/)

## Getting Started

### Prerequisites
* Python installed on your Mac.
* A Gemini API Key from [Google AI Studio](https://aistudio.google.com/).

### Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/Global-AI-Hackathon.git](https://github.com/your-username/Global-AI-Hackathon.git)
   cd Global-AI-Hackathon
   ```

2. **Run the setup script:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Add your API Key:**
   ```bash
   Create a file at .streamlit/secrets.toml and add:
   GEMINI_API_KEY = "your_api_key_here"
   ```

4. **Launch the app:**
   ```bash
   source .venv/bin/activate
   python -m streamlit run app.py
   ```
