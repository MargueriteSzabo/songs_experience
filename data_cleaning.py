import pandas as pd
import math


def data_clean(songs):
    #songs = pd.read_csv(df, decimal=',')

    ####### Conversion colonnes en float

    songs["Song_Hotness"] = songs["Song_Hotness"].astype(float)
    songs["Danceability"] = songs["Danceability"].astype(float)
    songs["Loudness"] = songs["Loudness"].astype(float)
    songs["ArtistLatitude"] = songs["ArtistLatitude"].astype(float)
    songs["ArtistLongitude"] = songs["ArtistLongitude"].astype(float)
    songs["Tempo"] = songs["Tempo"].astype(float)
    songs["Duration"] = songs["Duration"].astype(float)
    songs["Artist_Familiarity"] = songs["Artist_Familiarity"].astype(float)
    songs["Artist_Hotness"] = songs["Artist_Hotness"].astype(float)
    songs["Artist_Terms"] = songs["Artist_Terms"].astype(float)

    ####### Enlever les 'b' des features
    songs.ArtistName = songs.ArtistName.str.lstrip("b'").str.rstrip("'")
    songs.SongID = songs.SongID.str.lstrip("b'").str.rstrip("'")
    songs.AlbumName = songs.AlbumName.str.lstrip("b'").str.rstrip(
        "'").str.rstrip('"')
    songs.ArtistID = songs.ArtistID.str.lstrip("b'").str.rstrip("'")
    songs.ArtistLocation = songs.ArtistLocation.str.lstrip("b'").str.rstrip(
        "'")
    songs.Title = songs.Title.str.lstrip("b'").str.rstrip("'")
    #songs.Track_ID = songs.Track_ID.str.lstrip("b'").str.rstrip("'")
    songs['Tempo'] = songs['Tempo'].astype(float)
    song_less = songs[[
        'Title', 'ArtistName', 'Duration', "Tempo", 'Year', 'AlbumName',
        'ArtistLocation', 'Artist_Familiarity', 'Artist_Hotness'
    ]]

    song_less_year0 = songs[songs['Year'] != 0]
    song_less_year0 = song_less_year0[["Year", "Tempo"]]
    song_less_year0.Year = song_less_year0.Year.apply(
        lambda x: math.floor(x / 10) * 10)

    song_less_year0.sort_values(by=['Year'], ascending=True, inplace=True)

    song_less_year0 = pd.DataFrame(song_less_year0.groupby('Year').mean())
    song_less_year0.Tempo = round(song_less_year0.Tempo, 0)



    return songs
