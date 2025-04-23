import random

class song:
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.next = None
        self.prev = None

class Playlist_Manager:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
#single linked
    def add_song_to_beginning(self, song):
        song.next = self.head
        self.head = song
    
    def add_song_to_end(self, song):
        if not self.head:
            self.head = song
            self.tail = song
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = song
        
    
    def remove_first_song(self):
        if not self.head:
            return None
        removed = self.head
        self.head = self.head.next
        return removed
    
    def remove_last_song(self):
        if not self.head:
            return None
        if not self.head.next:
            removed = self.head
            self.head = None
            self.tail = None
            return removed
        current = self.head
        while current.next != self.tail:
            current = current.next
        
        removed = self.tail
        current.next = None
        self.tail = current

        self.size -=1
        return removed
    
    def get_playlist_duration(self):
        length = 0
        current = self.head
        while current:
            length += current.duration
            current = current.next
        return length
        
    def filter_by_genre(self, genre):
        songs = []
        current = self.head
        while current:
            if current.genre == genre:
                songs.append(current.title)
            current = current.next
        return songs

    def display_playlist(self):
        current = self.head
        while current:
            print(current.title)
            current = current.next

#doubly linked
    def play_next_song(self):
        if self.head and self.head.next:
            self.head = self.head.next
            print(f"Playing: {self.head.title}")

    def play_previous_song(self):
        if self.head and self.head.prev:
            self.head = self.head.prev
            print(f"Playing: {self.head.title}")

    def insert_song_at_position(self, song, position):
        if position <= 0 or not self.head:
            song.next = self.head
            if self.head:
                self.head.prev = song
            self.head = song
            return
        current = self.head
        for _ in range(position - 1):
            if not current.next:
                break
            current = current.next
        song.next = current.next
        song.prev = current
        if current.next:
            current.next.prev = song
        current.next = song

    def remove_song_by_title(self, title):
        current = self.head
        while current:
            if current.title == title:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return current
            current = current.next
        return None

    def shuffle_playlist(self):
        songs = []
        current = self.head
        while current:
            songs.append(current)
            current = current.next
        random.shuffle(songs)
        self.head = self.tail = None
        for song in songs:
            song.next = song.prev = None
            self.add_song_to_end(song)

    def create_playlist_from_favorites(self,favorite_titles):
        favotites_playlist = Playlist_Manager()
        current = self.head
        while current:
            if current.title in favorite_titles:
                favotites_playlist.add_song_to_end(current)
            current = current.next
        return favotites_playlist

song1 = song("song1", "artist", 3.33, "rock")
song2 = song("song2", "guyman", 2.22, "pop")
song3 = song("song3", "rapguy", 4.44, "rap")
song4 = song("song4", "otherrapguy", 2.55, "rap")
song5 = song("song5", "otherguy", 12.20, "pop")

playlist = Playlist_Manager()

#demonstrating functions
playlist.add_song_to_beginning(song1)
playlist.add_song_to_end(song2)
playlist.insert_song_at_position(song3, 1)

print("\nPlaylist after initial add to beginning, end, and insertion.")
playlist.display_playlist()

playlist.remove_first_song()
playlist.remove_last_song()

print("\nPlaylist after removal:")
playlist.display_playlist()

print(f"\nPlaylist Length: {playlist.get_playlist_duration()}")

playlist.add_song_to_end(song4)
playlist.add_song_to_end(song5)

playlist.remove_song_by_title("song3")

print("\nPlaylist after addtional songs added and song3 removed by title")
playlist.display_playlist()

playlist.shuffle_playlist()
print("\nPlaylist after shuffle")
playlist.display_playlist()

pop = playlist.filter_by_genre("pop")
print("\nSongs from filter by pop")
for i in pop:
    print(i)

favs = ["song2"]
favorites = playlist.create_playlist_from_favorites(favs)
print("\nFavorites playlist")
favorites.display_playlist()