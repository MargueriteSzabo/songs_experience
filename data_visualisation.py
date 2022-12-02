import numpy as np
import pandas as pd

from data_cleaning import data_clean
from visualitation_function import get_label_rotation, add_labels

import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('data/SongCSV.csv', decimal=',')

songs= data_clean(data)

songs_wheel = songs[[
    'Duration', 'Year', 'KeySignature', 'Tempo', 'Loudness', 'Mode',
    'Danceability', 'Song_Hotness', 'Artist_Hotness']]



bins = [1950, 1960, 1970, 1980, 1990, 2000, 2010]

plot_decenny_features = songs_wheel.groupby([pd.cut(songs_wheel.Year, bins)
                                             ]).agg({
                                                 'Duration': ['mean'],
                                                 'Tempo': ['mean'],
                                                 'Loudness': ['mean'],
                                                 'Song_Hotness': ['mean'],
                                                 'Artist_Hotness': ['mean']
                                             })

plot_decenny_features.columns = [
    col[0] for col in plot_decenny_features.columns
]

scaler_1 = MinMaxScaler()  # Instanciate Scaler
scaler_1.fit(plot_decenny_features[['Duration']])  # Fit scaler to data
plot_decenny_features['Duration'] = scaler_1.transform(
    plot_decenny_features[['Duration']])

scaler_2 = MinMaxScaler()  # Instanciate Scaler
scaler_2.fit(plot_decenny_features[['Tempo']])  # Fit scaler to data
plot_decenny_features['Tempo'] = scaler_2.transform(
    plot_decenny_features[['Tempo']])

scaler_3 = MinMaxScaler()  # Instanciate Scaler
scaler_3.fit(plot_decenny_features[['Loudness']])  # Fit scaler to data
plot_decenny_features['Loudness'] = scaler_3.transform(
    plot_decenny_features[['Loudness']])

scaler_4 = MinMaxScaler()  # Instanciate Scaler
scaler_4.fit(plot_decenny_features[['Song_Hotness']])  # Fit scaler to data
plot_decenny_features['Song_Hotness'] = scaler_4.transform(
    plot_decenny_features[['Song_Hotness']])

scaler_5 = MinMaxScaler()  # Instanciate Scaler
scaler_5.fit(plot_decenny_features[['Artist_Hotness']])  # Fit scaler to data
plot_decenny_features['Artist_Hotness'] = scaler_5.transform(
    plot_decenny_features[['Artist_Hotness']])

plot_decenny_features = plot_decenny_features.applymap(lambda x: x + 0.2)

plot_decenny_feat = plot_decenny_features.unstack().to_frame().rename(
    columns={0: 'value'})

# Grab the group values
GROUP = ['Duration', 'Tempo', 'Loudness', 'Song_Hotness', 'Artist_Hotness']
VALUES = plot_decenny_feat['value'].values

LABELS = [
    '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '1950s', '1960s',
    '1970s', '1980s', '1990s', '2000s', '1950s', '1960s', '1970s', '1980s',
    '1990s', '2000s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s',
    '1950s', '1960s', '1970s', '1980s', '1990s', '2000s'
]

OFFSET = np.pi / 2

# Add three empty bars to the end of each group

ANGLES_N = len(VALUES)
ANGLES = np.linspace(0, 2 * np.pi, num=ANGLES_N, endpoint=False)
WIDTH = (2 * np.pi) / len(ANGLES)

# Obtaining the right indexes is now a little more complicated
offset = 0
IDXS = []
GROUPS_SIZE = [6, 6, 6, 6, 6]

# Same layout as above
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={"projection": "polar"})

ax.set_theta_offset(OFFSET)
ax.set_ylim(-2, 2)
ax.set_frame_on(False)
ax.xaxis.grid(False)
ax.yaxis.grid(False)
ax.set_xticks([])
ax.set_yticks([])

# Use different colors for each group!

COLORS = [f"C{i}" for i, size in enumerate(GROUPS_SIZE) for _ in range(size)]

# And finally add the bars.
ax.bar(ANGLES,
       VALUES,
       width=WIDTH,
       color=COLORS,
       edgecolor="white",
       linewidth=2)

add_labels(ANGLES, VALUES, LABELS, OFFSET, ax)

for group, size in zip(
    ['Duration', 'Tempo', 'Loudness', 'Song_Hotness', 'Artist_Hotness'],
        GROUPS_SIZE):
    # Add line below bars
    x1 = np.linspace(ANGLES[offset],
                     ANGLES[offset + size - 1],
                     num=35)

    ax.plot(x1, [-0.1] * 35, color="#333333")

    # Add text to indicate group
    ax.text(np.mean(x1),
            -0.82,
            group,
            color="#333333",
            fontsize=14,
            fontweight="bold",
            ha="center",
            va="center")

    offset += size

fig.show()

fig.savefig('wheel_decenny', format = 'jpg')
