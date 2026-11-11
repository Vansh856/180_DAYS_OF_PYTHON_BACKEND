class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

my_playlist = Playlist(["Song 1", "Song 2", "Song 3"])
print(len(my_playlist))  # This will return 3