"""
Assignment 5 - Milestone 3: Model a Playlist Using Object-Oriented Composition
Course: Python Programming (COM-501)
Course Outcome: CO3 | Bloom's Level: 4

Explanation of Object Composition:
Object composition is a structural design technique where complex objects are assembled
from simpler constituent objects (a 'has-a' relationship). Instead of relying on inheritance,
the Playlist class holds and coordinates an internal collection of MediaItem instances.
This allows the Playlist to delegate item-level formatting and attributes to MediaItem while
encapsulating playlist-level behaviors such as calculating total duration and finding the top-rated item.
"""

class MediaItem:
    app_name = "Analytics App"

    def __init__(self, title, creator, media_type, duration_sec, rating):
        self.title = title
        self.creator = creator
        self.media_type = media_type
        self.duration_sec = duration_sec
        self.rating = rating

    def __str__(self):
        return f"{self.title} by {self.creator} [{self.media_type}] - {self.duration_sec}s (Rating: {self.rating})"


class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_duration(self):
        return sum(item.duration_sec for item in self.items)

    def top_rated(self):
        return max(self.items, key=lambda item: item.rating) if self.items else None

    def display_playlist(self):
        for i in self.items:
            print(" - ", i)

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    pl = Playlist("Daily Mix")
    pl.add_item(MediaItem("Track 1", "Artist A", "Song", 180, 4.5))
    pl.add_item(MediaItem("Track 2", "Artist B", "Song", 240, 4.9))
    pl.add_item(MediaItem("Episode 1", "Host C", "Podcast", 1200, 4.2))

    print(f"Playlist: {pl.playlist_name} (Size: {len(pl)})")
    print(f"Total Duration: {pl.total_duration()}s")
    top = pl.top_rated()
    if top:
        print(f"Top Rated Item: {top.title}")
    pl.display_playlist()
