import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.DataFrame({
    'Month': ['August', 'August', 'August', 'September', 'September', 'September', 'October', 'October', 'November', 'November'],
    'Week': ['Week 1', 'Week 2', 'Week 3-4', 'Week 1-2', 'Week 3', 'Week 4', 'Week 1-2', 'Week 3-4', 'Week 1-2', 'Week 3-4'],
    'Task': [
        'Literature Review: Collect and study related works.',
        'Problem Statement Finalization.',
        'Deep dive into algorithms and methodologies.',
        'Dataset Identification and Preprocessing.',
        'Draft the Review Paper.',
        'Peer Review of the Paper.',
        'Review Paper Finalization and Submission.',
        'Graph Neural Network Model Exploration.',
        'Model Training and Validation (Phase I).',
        'Phase I Report Preparation and Submission.'
    ]
})

# Plotting example
df.plot(kind='bar', x='Month', y='Week', title='Project Timeline')
plt.show()

