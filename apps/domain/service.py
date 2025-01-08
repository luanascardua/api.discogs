from apps.adapters.discogs_api import DiscogsAPI
from apps.adapters.file_storage import FileStorage


class ArtistService:
    def __init__(self, discogs_api: DiscogsAPI, file_storage: FileStorage):
        self.discogs_api = discogs_api
        self.file_storage = file_storage

    def fetch_and_save_artist_data(self, genre: str, filename: str):
        artists = self.discogs_api.search_artists_by_release_genre("rock")
        data = []

        for artist_name in artists:
            albums = self.discogs_api.get_album_details(artist_name)
            artist_resource_url, artist_id = self.discogs_api.search_artist(artist_name)
            if not artist_resource_url:
                continue
            artist_details = self.discogs_api.get_artist_details(artist_resource_url, albums)
            if artist_details:
                data.append(artist_details.to_dict())

        self.file_storage.save_to_json(filename, data)
