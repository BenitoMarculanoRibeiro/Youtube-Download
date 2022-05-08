from pytube import YouTube, Playlist


def download_video(video_url):
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    video.download()


def teste(video_url, path, qualidade):
    yt = YouTube(video_url)
    video = yt.streams.get_by_resolution(qualidade)
    video.download(output_path=path)


def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    for url in playlist:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path='playlist')


def download_audio(video_url):
    yt = YouTube(video_url)
    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()


video_url = input('Insira o link do video: ')
path = input('Insira a pasta de destino: ')
qualidade = input('Insira a qualidade: ')
# D:\GitHubDesktop\Youtube-Download\Videos\Teste1
teste(video_url, path, qualidade)
'''
1 - Baixar 1 video.
2 - Baixar mais de 1 video, sem ser uma playlist, formato de inserção: link1, link2, ...
3 - Baixar 1 playlist.
4 - Baixar maid de 1 playlist, formato de inserção: playlist1, playlist2, ...
5 - Mudar configurações de video, qualidade e legendas.
'''

'''
Selecione uma qualidade
'''
