import os
from apps.adapters.discogs_api import DiscogsAPI
from apps.adapters.file_storage import FileStorage
from apps.domain.service import ArtistService

from decouple import config


def main():
    genre = "rock"
    output_file = "artists.json"

    api = DiscogsAPI(config("TOKEN"))
    storage = FileStorage()
    service = ArtistService(api, storage)

    service.fetch_and_save_artist_data(genre, output_file)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
