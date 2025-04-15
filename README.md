 🗣️ Speech Recognition App

This is a simple yet powerful Streamlit-based application that allows users to record their voice, transcribe speech to text using speech recognition APIs, and optionally save the transcription to a `.txt` file.


 🎯 Features

- 🎤 Record speech using your system's microphone
- 🧠 Choose between:
  - **Google Speech Recognition API**
  - **CMU Sphinx (offline)**
- 🌍 Support for custom language codes (e.g., `en-US`, `fr-FR`, etc.)
- 💾 Save transcriptions locally as text files
- ✅ Simple and intuitive web interface built with Streamlit



 ⚙️ Installation

```bash
git clone https://github.com/your-username/speech-recognition-app.git
cd speech-recognition-app
pip install -r requirements.txt
📦 Requirements
Ensure your requirements.txt includes:

nginx
Copy
Edit
streamlit
speechrecognition
pyaudio
Note: On Mac or Linux, you might need to install portaudio before installing pyaudio.
On macOS:

bash
Copy
Edit
brew install portaudio
pip install pyaudio
🚀 Running the App
bash
Copy
Edit
streamlit run app.py
⚠️ This app requires microphone access and must be run locally (not on Streamlit Cloud or other web platforms).



📁 Output
When you click "Save Transcription", the result is saved as:

Copy
Edit
transcription.txt
👤 Author
Ziggy Greg
GitHub • Instagram

📝 License
This project is open source and free to use under the MIT License.
