# Speech Recognition Web App

A simple web application that performs speech recognition using Flask and the Google Speech Recognition API.

## Features

- **Speech Recognition**: Convert spoken words into text using a microphone.
- **Web Interface**: Input text manually or through speech recognition.
- **Flask Backend**: Handle requests and render templates.

## Requirements

- Python 3.x
- Flask
- SpeechRecognition

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```sh
    python app.py
    ```

2. **Open your browser** and go to `http://127.0.0.1:5000/`.

3. **Use the web interface** to input text manually or perform speech recognition.

## Code Overview

### `app.py`

```python
from flask import Flask, request, render_template
import speech_recognition as sr

app = Flask(__name__)

# Create a recognizer object
recognizer = sr.Recognizer()

# Define a function for speech recognition
def recognize_speech():
    with sr.Microphone() as source:
        print("Please start speaking...")
        recognizer.adjust_for_ambient_noise(source)  # Adapt to ambient noise
        audio = recognizer.listen(source)  # Listen to the audio from the microphone

    try:
        print("Processing speech recognition result...")
        text = recognizer.recognize_google(audio, language="en-US")  # Use Google Speech Recognition API to recognize speech
        return text
    except sr.UnknownValueError:
        print("Sorry, could not recognize speech.")
        return ""
    except sr.RequestError as e:
        print("Error processing request: ", str(e))
        return ""

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get text from form
        text = request.form['text']
        
        return render_template('index.html', text=text)
    
    return render_template('index.html', text=None)

# Route for speech recognition
@app.route('/speech_recognition', methods=['POST'])
def speech_recognition():
    recognized_text = recognize_speech()
    return render_template('index.html', text=recognized_text)

if __name__ == '__main__':
    app.run(debug=True)
