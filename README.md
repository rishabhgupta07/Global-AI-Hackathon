# 🛡️ NeutralizeAI: The News Debiasing Engine

**NeutralizeAI** is a high-speed linguistic analysis tool built for the **Global AI Hackathon 2026**. It leverages Gemini 2.5 Flash to identify, quantify, and neutralize ideological bias in real-time news reporting.

---

## 🚀 The Venture Pitch
Traditional news is often framed with selective language that distorts objective reality. **NeutralizeAI** provides a "Linguistic Fingerprint" of any article, allowing researchers, corporate intelligence teams, and casual readers to strip away the "noise" and focus on the facts.

## ✨ Key Features
* **AI-Powered Debiasing:** Uses Gemini 2.5 Flash to rewrite biased narratives into neutral prose.
* **Bias Fingerprinting:** A Radar Chart visualization that measures Political Leaning, Sensationalism, Subjectivity, Omission, and Tone.
* **Streamlined Workflow:** A professional dashboard for side-by-side analysis.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Framework:** [Streamlit](https://streamlit.io/)
* **AI Model:** Google Gemini 2.5 Flash
* **Visualization:** [Plotly](https://plotly.com/)

## ⚙️ Getting Started

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
GEMINI_API_KEY = "your_api_key_here" hehe
```

4. **Launch the app:**
```bash
source .venv/bin/activate
python -m streamlit run app.py
```


### 💡 Summary Table for Your Project Files
| File | Purpose | Professional Tip |
| :--- | :--- | :--- |
| **`.gitignore`** | Keeps repo clean. | Never commit `secrets.toml` or `.venv/`. |
| **`setup.sh`** | Automates setup. | Makes your project "one-click" for the judges. |
| **`README.md`** | Project manual. | Use it to explain the **"why"** behind your project. |
| **`.streamlit/secrets.toml`** | Stores API keys. | This is the standard way to handle keys in Streamlit. |

[Build a professional Streamlit dashboard](https://www.youtube.com/watch?v=09Uf_9-9p_o)
This video is relevant because it shows how to design and organize a professional-looking dashboard in Streamlit, which will help you make a great impression during the hackathon.