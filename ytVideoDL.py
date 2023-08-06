from pytube import YouTube

def Download(link):
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()
        print("Download concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")

link = input("Insira o URL do vídeo do YouTube: ")
Download(link)
