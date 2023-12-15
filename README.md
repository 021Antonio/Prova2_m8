# Prova2_m8

## Como rodoar

O repositorio presenta 2 codigos:

```bash
traducap.py
tts.py
``` 
O Codigo `traducao.py` utiliza a api do google para uma facil tradução sendo limitada apenas de um audio em portugues para o ingles. 
Por ser uma api do google, não utliza um grande processamento, sendo tambem, o principal requisito para uso, uma rede estavel de internet.
Acredito que por usar pouco processamento, é valido a utilização em smartphones e em sistemas embarcados.

Ja o `tts.py`, é o codigo usado para a trascrição de texto para audio. 
A utilização deste script não é capaz de atender todos os publicos, tendo em vista que pessoas com aspectos autistas apresentam diferentes condições, sendo elas dificuldades na fala e em outras pessoas apresentam dificuldade de manoseio e entendimento da escrita.

Para rodar o projeto, é necessario rodar o comando:

```bash
pip install git+https://github.com/suno-ai/bark.git
pip install simpleaudio

``` 
Esse codigo é para instalar a biblioteca que o sistema utiliza para a trascrição da frase apra a fala. 

```bash
pip install pip install SpeechRecognition googletrans gtts
```
Este é para a trdução, utilizando a api do google.

Como são 2 codigos diferente, não é possivel ter uma interação com eles, sendo assim, Caso o usuario deseje usar o tradutor, é necessario rodar apenas o tradutor, utilizando um audio em formato `.wav` e o sistema iŕa gerar um audio ja traduzido.

Para isso, utilize 
```bash
python3 traducao.py
```

Ja o `tts`, ao rodar, abre uma interface de comando que permite o usuario escrever uma frase e o sistema gera um audio sobre a fala. 

Para isso, utilize o camando 

```bash
python3 tts.py
```

**IMPORTANTE**

O modelo de `tts` não é recomendado usar localmente. É necessario um grande poder computacional onde os smartphones e aparelhos embarcados, não suportam.
Mas, o tradutor consegue :)