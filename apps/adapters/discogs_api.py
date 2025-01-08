import requests
from apps.domain.entities import Artist, Album, Track
from typing import List, Optional

from decouple import config


class DiscogsAPI:
    BASE_URL = config("BASE_URL")
    HEADERS = {"Authorization": f"Discogs token={config('TOKEN')}"}

    def __init__(self, token: str):
        self.token = token

    def search_artists_by_release_genre(self, genre, limit=10):
        endpoint = f"{self.BASE_URL}/database/search"
        params = {
            "genre": genre,
            "type": "release",
            "per_page": limit,
            "page": 1,
        }
        response = requests.get(endpoint, headers=self.HEADERS, params=params)
        if response.status_code == 200:
            results = response.json().get("results", [])
            artists = set()
            for release in results:
                artist_name = release.get("title", "").split(" - ")[0].strip("*")  # Nome do artista está antes de " - "
                if artist_name:
                    artists.add(artist_name)
            
            if artists:
                print(f"Artistas associados ao gênero '{genre}':")
                for artist in artists:
                    print(f"- {artist}")
                return list(artists)
            else:
                print(f"Nenhum artista encontrado para o gênero '{genre}'.")
                return []
        else:
            print(f"Erro ao buscar lançamentos: {response.status_code} - {response.text}")
            return []

    def search_artist(self, artist_name: str):
        endpoint = f"{self.BASE_URL}/database/search"
        params = {"q": artist_name, "type": "artist", "per_page": 1}
        response = requests.get(endpoint, headers=self.HEADERS, params=params)
        if response.status_code == 200:
            results = response.json().get("results", [])
            if results:
                artist_data = results[0]
                print(f"Artista encontrado: {artist_data.get('title')}")
                return artist_data.get("resource_url"), artist_data.get("id")
            else:
                print("Artista não encontrado.")
                return None, None
        else:
            print(f"Erro na busca: {response.status_code}")
            return None, None

    def get_artist_details(self, resource_url: str, albums: list):
        response = requests.get(resource_url, headers=self.HEADERS)
        if response.status_code == 200:
            artist_details = response.json()

            name = artist_details.get("name")
            genre = artist_details.get("genres", ["Desconhecido"])[0]
            members = [member.get("name") for member in artist_details.get("members", [])]
            websites = artist_details.get("urls", [])

            return Artist(
                name=name,
                genre=genre,
                members=members,
                websites=websites,
                albums=albums
            )
        else:
            print(f"Erro ao obter detalhes do artista: {response.status_code}")
            return None

    def get_album_details(self, artist_name: str):
        params = {
            "artist": artist_name,
            "type": "release",
            "per_page": 5,
            "page": 1
        }

        response = requests.get("https://api.discogs.com/database/search", headers=self.HEADERS, params=params)
        if response.status_code == 200:
            album_details = response.json().get("results", [])
            albums = []

            for result in album_details:
                title = result.get("title")
                year = result.get("year", "Desconhecido")
                label = result.get("label", ["Desconhecida"])[0]
                styles = result.get("style", [])
                resource_url = result.get("resource_url")

                track_response = requests.get(resource_url, headers=self.HEADERS)
                if track_response.status_code == 200:
                    track_data = track_response.json()
                    tracklist = track_data.get("tracklist", [])
                    tracks = [
                        Track(
                            number=i + 1,
                            title=track.get("title", "Sem título"),
                            duration=track.get("duration", "Desconhecido")
                        )
                        for i, track in enumerate(tracklist)
                    ]
                else:
                    tracks = []

                albums.append(
                    Album(
                        name=title,
                        year=year,
                        label=label,
                        styles=styles,
                        tracks=tracks
                    )
                )

            return albums
        else:
            print(f"Erro ao obter detalhes do álbum: {response.status_code}")
            return None
