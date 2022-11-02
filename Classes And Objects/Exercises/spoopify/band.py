from classes_and_objects_exercises.spoopify import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        for album in self.albums:

            if album.published:
                return f"Album has been published. It cannot be removed."

            self.albums.remove(album)
            return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}" + "\n"
        for album in self.albums:
            result += album.details() + "\n"

        return result
