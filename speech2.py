import streamlit as st
import speech_recognition as sr
import os

def transcribe_speech(api_choice, language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        try:
            audio_text = r.listen(source, timeout=5)
            st.info("Transcribing...")
            
            if api_choice == "Google Speech Recognition":
                text = r.recognize_google(audio_text, language=language)
            elif api_choice == "Sphinx (offline)":
                text = r.recognize_sphinx(audio_text, language=language)
            else:
                return "Selected API is not supported yet."
            
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand the speech."
        except sr.RequestError:
            return "Could not request results, check your internet connection."
        except Exception as e:
            return f"An error occurred: {str(e)}"

def save_transcription(text):
    filename = "transcription.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return filename

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")
    
    api_choice = st.selectbox("Select Speech Recognition API:", ["Google Speech Recognition", "Sphinx (offline)"])
    language = st.text_input("Enter Language Code (e.g., 'en-US', 'fr-FR'):", value="en-US")
    
    if "is_recording" not in st.session_state:
        st.session_state.is_recording = False
    
    if st.button("Start Recording"):
        st.session_state.is_recording = True
        text = transcribe_speech(api_choice, language)
        st.write("Transcription: ", text)
        
        if st.button("Save Transcription"):
            filename = save_transcription(text)
            st.success(f"Transcription saved to {filename}")
    
    if st.button("Pause Recording"):
        st.session_state.is_recording = False
        st.write("Recording paused.")
    
    if st.button("Resume Recording"):
        st.session_state.is_recording = True
        text = transcribe_speech(api_choice, language)
        st.write("Transcription: ", text)
    
if __name__ == "__main__":
    main()
