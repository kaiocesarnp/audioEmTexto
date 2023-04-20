import speech_recognition as sr

r = sr.Recognizer()

# Inicializa o mic
with sr.Microphone() as source:
    print("Diga alguma coisa:")
    audio = r.listen(source)

try:
    # Tenta reconhecer o áudio usando o google speech recognition
    text = r.recognize_google(audio, language='pt-BR')
    print(f"Você disse: {text}")
except sr.UnknowValueError:
    print("Não entendi o que você disse!")
except sr.ResquestError as e:
    print("Erro de requisição; {0}".format(e))


# Explicação de cada linha:

# import speech_recognition as sr: importa a biblioteca SpeechRecognition e a renomeia para sr, para facilitar a referência;

# r = sr.Recognizer(): Cria uma nova instância da classe Recognizer da biblioteca SpeechRecognition, que é usada para reconhecer o áudio capturado.












