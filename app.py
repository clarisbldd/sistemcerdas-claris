from flask import Flask, request, render_template
import speech_recognition as sr

app = Flask(__name__)

# Membuat objek recognizer
recognizer = sr.Recognizer()

# Mendefinisikan fungsi untuk melakukan speech recognition
def recognize_speech():
    with sr.Microphone() as source:
        print("Silakan mulai berbicara...")
        recognizer.adjust_for_ambient_noise(source) # Adaptasi dengan lingkungan suara
        audio = recognizer.listen(source) # Mendengarkan audio dari mikrofon

    try:
        print("Memproses hasil speech recognition...")
        text = recognizer.recognize_google(audio, language="en-US") # Menggunakan Google Speech Recognition API untuk mengenali ucapan
        return text
    except sr.UnknownValueError:
        print("Maaf, tidak dapat mengenali ucapan.")
        return ""
    except sr.RequestError as e:
        print("Error saat memproses permintaan: ", str(e))
        return ""

# Route untuk halaman utama
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ambil teks dari form
        text = request.form['text']
        
        return render_template('index.html', text=text)
    
    return render_template('index.html', text=None)

# Route untuk speech recognition
@app.route('/speech_recognition', methods=['POST'])
def speech_recognition():
    recognized_text = recognize_speech()
    return render_template('index.html', text=recognized_text)

if __name__ == '_main_':
    app.run(debug=True)