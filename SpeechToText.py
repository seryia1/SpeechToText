import streamlit as st
import speech_recognition as sr

def transcribe_audio_file(audio_file):
    # Initialize recognizer class
    r = sr.Recognizer()
    # Use the uploaded audio file as source
    with sr.AudioFile(audio_file) as source:
        st.info("Processing audio...")
        audio_text = r.record(source)
        st.info("Transcribing...")

        try:
            # using Google Speech Recognition
            text = r.recognize_google(audio_text)
            return text
        except:
            return "Sorry, I could not transcribe the audio."

def main():
    st.title("Speech Recognition App")
    st.write("Upload an audio file (wav, mp3, flac) to transcribe:")

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "flac"])
    if uploaded_file is not None:
        text = transcribe_audio_file(uploaded_file)
        st.write("Transcription:")
        st.success(text)

if __name__ == "__main__":
    main()
