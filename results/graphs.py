import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

f, ax = plt.subplots(figsize=(7, 6))

data = [
    { 'statement': 'The system is useful.', 'true': [3,	4, 3, 4, 5, 3, 3, 2, 3, 3, 4, 2], 'false': [4, 4, 5, 2, 5, 4, 3, 3, 4, 4, 5, 3]},
    { 'statement': 'The system is pleasant.', 'true': [6, 5, 5, 6, 7, 5, 3, 4, 4, 5, 5, 4], 'false': [6, 5, 6, 6, 7, 7, 4, 5, 5, 5, 5, 6]},
    { 'statement': 'The system is friendly.', 'true': [5, 4, 6, 7, 7, 6, 7, 4, 3, 4, 5, 6], 'false': [6, 5, 6, 7, 7, 7, 6, 6, 7, 6, 6, 7]},
    { 'statement': 'I was able to recover easily from errors.', 'true': [3,	3, 3, 3, 2, 5, 4, 5, 2, 3, 2, 3], 'false': [3, 3, 3, 3, 2, 5, 5, 5, 6, 4, 3, 4]},
    { 'statement': 'I enjoyed using the system.', 'true': [4, 5, 6, 7, 7, 6, 3, 4, 3, 4, 4, 5], 'false': [6, 6, 6, 6, 7, 7, 6, 3, 5, 5, 5, 6]},
    { 'statement': 'It is clear how to speak to the system.', 'true': [6, 5, 6, 7, 7, 7, 4, 6, 5, 5, 4, 6], 'false': [6, 5, 6, 7, 7, 7, 6, 6, 6, 6, 6, 7]},
    { 'statement': 'It is easy to learn to use the system.', 'true': [5, 6,	6, 7, 7, 6, 4, 6, 4, 5, 5, 6], 'false': [7, 6, 6, 7, 7, 6, 6, 6, 6, 6, 7, 6]},
    { 'statement': 'I would use this system.', 'true': [3, 4, 4, 2, 3, 5, 2, 3, 2, 3, 4, 3], 'false': [3, 4, 4, 3, 3, 5, 4, 2, 4, 4, 4, 4]},
    { 'statement': 'I felt in control of the interaction with the system.', 'true': [6,	5, 6, 5, 6, 6, 5, 3, 4, 5, 4, 5], 'false': [7, 6, 7, 5, 6, 7, 5, 5, 6, 6, 6, 5]},
]

### TRANSFORM AND PLOT INPUT DATA ###

data_frames = []
for d in data:
    data_frames.append(pd.DataFrame(
        zip(d['true'], d['false'])
    ).assign(Statement=d['statement']))

cdf = pd.concat(data_frames)
mdf = pd.melt(cdf, id_vars=['Statement'], var_name=['Memory']).rename(columns={'value': 'Score'})

sns.boxplot(data=mdf, y='Statement', x='Score', hue="Memory", palette="Blues")

### ADD MEMORY LEGEND ###

handles, labels = ax.get_legend_handles_labels()
memory_legend = ax.legend(handles=handles, labels=['With Emotion Model', 'Without Emotion Model'], bbox_to_anchor=(.35, 1.0))
ax.add_artist(memory_legend)

### ADD SCORE LEGEND ###

handles = [
    mpatches.Patch(label='1: Strongly disagree'),
    mpatches.Patch(label='2: Disagree'),
    mpatches.Patch(label='3: Slightly disagree'),
    mpatches.Patch(label='4: Neutral'),
    mpatches.Patch(label='5: Slightly agree'),
    mpatches.Patch(label='6: Agree'),
    mpatches.Patch(label='7: Strongly agree')
]
score_legend = plt.legend(handles=handles, handlelength=0, handletextpad=0, fancybox=True, bbox_to_anchor=(1.3, 1.0), title='Score')

f.savefig('results.png', bbox_inches='tight', bbox_extra_artists=(memory_legend, score_legend,))