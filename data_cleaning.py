import pandas as pd
import math


def data_clean(songs):

    columns_list = ['Song_Hotness','Danceability','Loudness','ArtistLatitude',
                    'ArtistLongitude', 'Tempo', 'Duration', 'Artist_Familiarity',
                    'Artist_Hotness','Artist_Terms']

    ####### Convert columns into float
    for column in columns_list:
        songs[column] = songs[column].astype(float)


    ####### Remove b in the different columns
    songs.ArtistName = songs.ArtistName.str.lstrip("b'").str.rstrip("'")
    songs.SongID = songs.SongID.str.lstrip("b'").str.rstrip("'")
    songs.AlbumName = songs.AlbumName.str.lstrip("b'").str.rstrip(
        "'").str.rstrip('"')
    songs.ArtistID = songs.ArtistID.str.lstrip("b'").str.rstrip("'")
    songs.ArtistLocation = songs.ArtistLocation.str.lstrip("b'").str.rstrip(
        "'")
    songs.Title = songs.Title.str.lstrip("b'").str.rstrip("'")


    song_less_year0 = songs[songs['Year'] != 0]

    return song_less_year0
