def make_album(artist, title, num_songs=None):
    """Kembalikan dictionary berisi informasi sebuah album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if num_songs:
        album['num_songs'] = num_songs
    return album

print("Enter 'q' at any time to stop.")

while True:
    print("\nPlease tell me about an album.")
    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")