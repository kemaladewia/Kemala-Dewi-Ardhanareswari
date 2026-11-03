def make_album(artist, title, num_songs=None):
    """Kembalikan dictionary berisi informasi sebuah album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if num_songs:
        album['num_songs'] = num_songs
    return album

album = make_album('dewa 19', 'bintang lima')
print(album)

album = make_album('raisa', 'heart to heart')
print(album)

album = make_album('taylor swift', '1989')
print(album)

album = make_album('the beatles', 'abbey road', num_songs=17)
print(album)