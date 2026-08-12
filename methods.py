class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_english = Playlist("English Favorites")
my_english.add_song("Die with a Smile")
my_english.add_song("I wanna be yours")
my_english.show_songs()
hindi = Playlist("hindi favourites")
hindi.add_song("kabira")
hindi.add_song("kun faya kun")
hindi.show_songs()
