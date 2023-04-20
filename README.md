Transformar áudio em texto usando Python;

Para usar este código, primeiro deve-se instalar os módulos 'pyaudio' e 'SpeechRecognition'. Execute os comandos 'pip install pyaudio' e 'pip install SpeechRecognition' no terminal;

A biblioteca PyAudio é uma biblioteca de processamento de áudio em Python que permite aos desenvolvedores reproduzir e gravar áudio em tempo real em diferentes plataformas. Ela fornece uma interface de programação de aplicativo (API) para acessar as funcionalidades de áudio do sistema operacional do computador, permitindo a gravação e reprodução de áudio por meio de microfones e alto-falantes conectados ao computador. E suporta vários formatos de áudio, incluindo WAV, AIFF, AU e outros, e permite que os desenvolvedores controlem várias configurações de áudio, como taxa de amostragem, tamanho do buffer e número de canais.

A biblioteca SpeechRecognition é uma biblioteca de reconhecimento de fala em Python, que permite aos desenvolvedores reconhecer e transcrever fala em texto a partir de arquivos de áudio ou dispositivos de entrada de fala, como microfones. É especialmente útil para aplicações que requerem entrada de voz, como sistemas de controle de voz e pode ser usada em uma variedade de plataformas, incluindo Windows, Linux e macOS;

Ao executar o código, a mensagem "Diga alguma coisa:" é exibida no terminal, demonstrando que o microfone está atividado. E ao reconhecer uma fala, a mensagem 
"Você disse: " junto com o que foi dito é exibida logo em seguida.
