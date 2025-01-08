from typing import List, Optional


class Track:
    def __init__(self, number: int, title: str, duration: str):
        self.number = number
        self.title = title
        self.duration = duration

    def to_dict(self):
        return {
            "number": self.number,
            "title": self.title,
            "duration": self.duration,
        }


class Album:
    def __init__(self, name: str, year: Optional[int], label: str, styles: List[str], tracks: List[Track]):
        self.name = name
        self.year = year
        self.label = label
        self.styles = styles
        self.tracks = tracks

    def to_dict(self):
        return {
            "name": self.name,
            "year": self.year,
            "label": self.label,
            "styles": self.styles,
            "tracks": [track.to_dict() for track in self.tracks],
        }


class Artist:
    def __init__(self, id: str, name: str, genre: str, members: List[str], websites: List[str], albums: List[Album]):
        self.id = id
        self.name = name
        self.genre = genre
        self.members = members
        self.websites = websites
        self.albums = albums

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "genre": self.genre,
            "members": self.members,
            "websites": self.websites,
            "albums": [album.to_dict() for album in self.albums],
        }
