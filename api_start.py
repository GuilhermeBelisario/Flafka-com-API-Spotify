import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials

# Substitua pelos seus próprios Client ID e Client Secret
client_id = 'aee7093a67304079a515f10a05bca257'
client_secret = '5a7c494baa0c4946b86da0e4a619715b'

# Configurando a autenticação
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

class ArtistSP:
    #Criando o começo dos arquivos ordenados sobre artista/genero
    # que serão salvos como json
    def __init__(self, artist_name):
        self.artist_name = artist_name

    def __str__ (self):
        return f'{self.artist_name}'

bandas = open('bandas.txt', mode='r', encoding='utf-8' )
bandas = list(bandas)
bandas_sem_espaço= [elemento.strip() for elemento in bandas]

for banda_nome in bandas_sem_espaço:
    band = ArtistSP(banda_nome)
    result = sp.search(q=band, type='artist')
    artist = result['artists']['items'][0]
    # Obtendo as top tracks do artista
    artist_id = artist['id']
    artist_genres = artist['genres']
    top_tracks = sp.artist_top_tracks(artist_id)

    #Mostrando os valores o ranking final
    print(band)
    print(artist_genres)

    for idc, track in enumerate(top_tracks['tracks']):
        print(f"{idc + 1}. {track['name']} - {track['popularity']}")
    
    time.sleep(5)
    
