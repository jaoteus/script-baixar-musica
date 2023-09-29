from pytube import YouTube
import os

# Variáveis
loopPrincipal = True
loopEscolha = None
loopUrl = None
escolhaSair = True

########### Coloque o diretório do download completo nas variáveis abaixo ##############
caminhoDownloadMusica = "C:/Users/mateu/Downloads"
caminhoDownloadVideo = "C:/Users/mateu/ownloads"

while loopPrincipal == True:
    loopUrl = True
    loopEscolha = True

    def baixarAudio():
        global stream, escolhaSair
        escolhaSair = True
        try:
            stream = videoOuAudio.streams.get_audio_only()
            stream.download(output_path = caminhoDownloadMusica)
        except ConnectionError:
            print("Connection Error :(")
        else:
            print("Donwload completo!")
            pass
        while escolhaSair == True:
            global escolha, loopPrincipal, loopEscolha, loopUrl
            escolha = input(str("S - Sair\nContinuar - ENTER\nDigite: "))
            if escolha == "S" or escolha == "s":
                os.system("cls")
                print("Saindo...")
                loopPrincipal = False
                loopEscolha = False
                loopUrl = False
                break

            elif escolha == "":
                os.system("cls")
                escolhaSair = False
                pass
            else:
                os.system("cls")
                escolhaSair = False
                pass

    def baixarVideo():
        global stream, escolhaSair
        escolhaSair = True
        try:
            stream = videoOuAudio.streams.get_highest_resolution()
            stream.download(output_path = caminhoDownloadVideo)
        except ConnectionError:
            print("Connection Error :(")
        else:
            print("Donwload completo!")
            pass
            while escolhaSair == True:
                global escolha, loopPrincipal, loopEscolha, loopUrl
                escolha = input(str("S - Sair\nContinuar - ENTER\nDigite: "))
                if escolha == "S" or escolha == "s":
                    os.system("cls")
                    print("Saindo...")
                    loopPrincipal = False
                    loopEscolha = False
                    loopUrl = False
                    break
                elif escolha == "":
                    escolhaSair = False
                    pass
                else:
                    escolhaSair = False
                    pass

    while loopUrl:
        try:
            url = input(str("URL: "))
            videoOuAudio = YouTube(url)
        except:
            os.system("cls")
            print("Coloque a URL completa!")
            continue
        else:
            os.system("cls")
            loopUrl = False
            pass
    while loopEscolha == True:
        escolha = input(str("A - Audio\nV - Vídeo\nDigite: "))
        if escolha == "A" or escolha == "a":
            baixarAudio()
            loopEscolha = False
        elif escolha == "v" or escolha == "V":
            baixarVideo()
            loopEscolha = False
        else:
            os.system("cls")
            print("Digite um dos dois!")
            continue
