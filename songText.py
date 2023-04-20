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

# with sr.Microphone() as source:: Abre o microfone do computador como uma fonte de áudio para o reconhecimento de voz. O bloco de código dentro do with será executado enquanto o microfone estiver aberto.

# print("Diga alguma coisa:"): Exibe uma mensagem para solicitar que o usuário fale alguma coisa.

# audio = r.listen(source): Grava o áudio a partir da fonte especificada e armazena-o na variável audio.

# try:: Inicia um bloco try-except, que tenta executar o código dentro do bloco try.

# text = r.recognize_google(audio, language='pt-BR'): Tenta reconhecer o áudio gravado usando o serviço de reconhecimento de fala do Google (recognize_google) fornecido pela biblioteca SpeechRecognition. O resultado do reconhecimento é armazenado na variável text.

# print(f"Você disse: {text}"): Imprime o texto reconhecido na linha anterior na tela.

# except sr.UnknownValueError:: Se ocorrer um erro de reconhecimento de voz, como não ser possível entender o que foi dito, este bloco except será executado e imprimirá uma mensagem de erro.

# except sr.RequestError as e:: Se ocorrer um erro durante a chamada do serviço de reconhecimento de fala do Google, este bloco except será executado e imprimirá uma mensagem de erro com o código de erro fornecido pelo serviço.










