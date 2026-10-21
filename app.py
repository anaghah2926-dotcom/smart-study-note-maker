import os
# We use a popular open-source AI library called Hugging Face Transformers
from transformers import pipeline

def generate_study_notes(textual_content):
    print("\n🤖 Reading your text and generating open-source study notes...")
    
    # We use an open-source model optimized for summarizing and condensing text
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Generate the summary
    summary = summarizer(textual_content, max_length=150, min_length=50, do_sample=False)
    
    return summary[0]['summary_text']

if __name__ == "__main__":
    print("📚 --- Welcome to the Open-Source Smart Study-Note Maker --- 📚")
    
    # Paste your textbook chapter text or raw notes here
    user_input = input("\nPaste the textbook text you want to study: \n> ")
    
    if len(user_input).strip() < 20:
        print("Please enter a longer text to summarize!")
    else:
        notes = generate_study_notes(user_input)
        print("\n✨ YOUR CLEAN STUDY NOTES ✨")
        print(notes)
        print("\n🚀 Saved you time! Go be lazy and relax.")
