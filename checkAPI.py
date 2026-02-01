from google import genai
import os

# 1. Setup your key (Replace with your actual key)
os.environ["GEMINI_API_KEY"] = "AIzaSyBM1COWmsEXQw2oY_W73XuVIWE1iuC5ATc"

def verify_gemini():
    try:
        # 2. Initialize the client
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        
        # 3. Test with a simple prompt
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents="Hello! Are you working?"
        )
        
        print("✅ API Key Verified!")
        print(f"Response: {response.text}")
        
    except Exception as e:
        print(f"❌ Verification Failed: {e}")

if __name__ == "__main__":
    verify_gemini()