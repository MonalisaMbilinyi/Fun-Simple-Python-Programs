
import lyricsgenius
lyrics=lyricsgenius.Genius("yqByC2BnkS0kaQjLLG14HZgpYNKSuUral_UXnlWo3Z2hgDDuMD1PSelQ96PorBaG")
name=input("enter the artist name  ")
artist=lyrics.search_artist(name)
song=input("what song are you choosing?  ")
song=artist.song(song)
print(song.lyrics)