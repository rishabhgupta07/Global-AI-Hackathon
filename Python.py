system_instruction = """
You are a professional neutral text editor specializing in linguistic de-biasing. 
Your goal is to analyze text for five dimensions of bias: Political Leaning, Sensationalism, 
Subjectivity, Omission, and Aggressive Tone.

For any input text, you must return strictly valid JSON with the following keys:
1. "scores": An object with values from 0.0 to 1.0 for each of the 5 dimensions.
2. "neutral_text": The entire input text rewritten to be completely neutral and factual.
3. "justification": A one-sentence explanation of the primary bias found.
"""

import streamlit as st
from google import genai
import plotly.graph_objects as go
import json

# Page Config
st.set_page_config(layout="wide", page_title="NeutralizeAI")

# 1. Setup Client
client = genai.Client(api_key="AIzaSyBM1COWmsEXQw2oY_W73XuVIWE1iuC5ATc")

st.title("🛡️ NeutralizeAI: Debiasing Engine")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    user_input = st.text_area("Paste Article Paragraphs here:", height=300)
    process_btn = st.button("Analyze & Neutralize")

if process_btn and user_input:
    # 2. Call Gemini 2.5 Flash
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
        config={
            "system_instruction": system_instruction,
            "response_mime_type": "application/json"
        }
    )
    
    # 3. Parse JSON
    data = json.loads(response.text)
    
    with col2:
        st.subheader("Neutralized Version")
        st.write(data['neutral_text'])
        
        # 4. Generate the Radar Chart
        categories = list(data['scores'].keys())
        values = list(data['scores'].values())
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Bias Profile',
            line_color='red'
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
            showlegend=False,
            title="Bias Intensity Map"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.info(f"**Analysis:** {data['justification']}")