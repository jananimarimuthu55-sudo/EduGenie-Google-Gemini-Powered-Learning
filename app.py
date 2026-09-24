import os
import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="EduGenie - AI Learning Assistant",
    page_icon="🎓",
    layout="wide"
)

# Initialize Gemini API
# Ensure GEMINI_API_KEY is set in your environment or Streamlit secrets
api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API Key missing. Please set GEMINI_API_KEY in your environment or secrets.")
    st.stop()

genai.configure(api_key=api_key)

# Model setup
model = genai.GenerativeModel("gemini-1.5-flash")

# Header Section
st.title("🎓 EduGenie: Google Gemini Powered Learning Assistant")
st.write("Welcome! Choose an assistant tool below to supercharge your learning.")

# Sidebar Navigation
mode = st.sidebar.radio(
    "Choose a Feature:",
    ["Explain a Concept", "Summarize Notes", "Generate Practice Quiz"]
)

# Feature 1: Explain a Concept
if mode == "Explain a Concept":
    st.header("💡 Concept Explainer")
    topic = st.text_input("What concept or topic would you like explained?")
    level = st.selectbox("Select Target Audience Level:", ["Beginner / High School", "Undergraduate", "Advanced / Expert"])
    
    if st.button("Explain Concept"):
        if topic:
            prompt = f"Explain the concept of '{topic}' tailored for a {level} level. Use clear headings, bullet points, and an illustrative example."
            with st.spinner("Generating explanation..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
        else:
            st.warning("Please enter a topic.")

# Feature 2: Summarize Notes
elif mode == "Summarize Notes":
    st.header("📝 Note Summarizer")
    notes = st.text_area("Paste your study notes or text here:", height=200)
    
    if st.button("Summarize"):
        if notes:
            prompt = f"Provide a concise summary of the following notes. Highlight key terms and main takeaways:\n\n{notes}"
            with st.spinner("Summarizing..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
        else:
            st.warning("Please paste some text to summarize.")

# Feature 3: Generate Practice Quiz
elif mode == "Generate Practice Quiz":
    st.header("🧪 Quiz Generator")
    quiz_topic = st.text_input("Enter a subject or topic for the quiz:")
    num_q = st.slider("Number of questions:", 1, 5, 3)
    
    if st.button("Generate Quiz"):
        if quiz_topic:
            prompt = f"Create a {num_q}-question multiple-choice quiz about '{quiz_topic}'. Include answer choices (A, B, C, D) and hide the correct answers with explanations at the very bottom under an 'Answer Key' section."
            with st.spinner("Creating quiz..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
        else:
            st.warning("Please enter a quiz topic.")
