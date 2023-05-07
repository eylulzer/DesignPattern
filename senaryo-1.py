from typing import List, Optional, Callable

class Album:
    def __init__(self, isim: str, sanatci: str, yayin_yili: int):
        self.isim = isim
        self.sanatci = sanatci
        self.yayin_yili = yayin_yili

    def __str__(self):
        return f"{self.isim} - {self.sanatci} ({self.yayin_yili})"

class AlbumIterator:
    def hasNext(self) -> bool:
        pass

    def next(self) -> Optional[Album]:
        pass

class AlbumKoleksiyonu:
    def createIterator(self) -> AlbumIterator:
        pass

class ConcreteAlbumKoleksiyonu(AlbumKoleksiyonu):
    def __init__(self):
        self.albumler = []

    def ekleAlbum(self, album: Album) -> None:
        self.albumler.append(album)

    def createIterator(self) -> AlbumIterator:
        return AllAlbumsIterator(self)

class AllAlbumsIterator(AlbumIterator):
    def __init__(self, album_koleksiyonu: ConcreteAlbumKoleksiyonu):
        self.album_koleksiyonu = album_koleksiyonu
        self.currentIndex = 0

    def hasNext(self) -> bool:
        return self.currentIndex < len(self.album_koleksiyonu.albumler)

    def next(self) -> Optional[Album]:
        if self.hasNext():
            album = self.album_koleksiyonu.albumler[self.currentIndex]
            self.currentIndex += 1
            return album
        return None

class FilteredAlbumIterator(AlbumIterator):
    def __init__(self, album_koleksiyonu: ConcreteAlbumKoleksiyonu, filter_func: Callable[[Album], bool]):
        self.album_koleksiyonu = album_koleksiyonu
        self.filter_func = filter_func
        self.currentIndex = 0

    def hasNext(self) -> bool:
        while self.currentIndex < len(self.album_koleksiyonu.albumler):
            if self.filter_func(self.album_koleksiyonu.albumler[self.currentIndex]):
                return True
            self.currentIndex += 1
        return False

    def next(self) -> Optional[Album]:
        if self.hasNext():
            album = self.album_koleksiyonu.albumler[self.currentIndex]
            self.currentIndex += 1
            return album
        return None

# Kullanım örneği
album_koleksiyonu = ConcreteAlbumKoleksiyonu()
album_koleksiyonu.ekleAlbum(Album("Album1", "Sanatci1", 2010))
album_koleksiyonu.ekleAlbum(Album("Album2", "Sanatci2", 2015))
album_koleksiyonu.ekleAlbum(Album("Album3", "Sanatci1", 2020))

print("Tüm albümler:")
album_iterator = album_koleksiyonu.createIterator()
while album_iterator.hasNext():
    album = album_iterator.next()
    print(album)

sanatci1_filter = lambda album: album.sanatci == "Sanatci1"
print("\nSanatci1'in albümleri:")
sanatci1_iterator = FilteredAlbumIterator(album_koleksiyonu, sanatci1_filter)
while sanatci1_iterator.hasNext():
    album = sanatci1_iterator.next()
    print(album)

yil2015_filter = lambda album: album.yayin_yili < 2015
print("\n2015'ten önce yayınlanan albümler:")
yil2015_iterator = FilteredAlbumIterator(album_koleksiyonu, yil2015_filter)
while yil2015_iterator.hasNext():
    album = yil2015_iterator.next()
    print(album)
