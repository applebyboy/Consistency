import matplotlib.pyplot as plt
import numpy as np

# Define a function to plot study data

def plot_study_data(study_data, title):
    fig, ax = plt.subplots(figsize=(12, 10))

    # Initialize lists for each stage
    initial_x, initial_y = [], []
    intermediate_1_x, intermediate_1_y = [], []
    intermediate_2_x, intermediate_2_y = [], []
    intermediate_3_x, intermediate_3_y = [], []

    # Colors and labels for each stage
    stage_colors = ['red', 'blue', 'green', 'purple']
    stage_labels = ['1st CP', '2nd CP', '3rd CP', '4th CP']
    stage_markers = ['X', 'o', '^', 's']

    # Plot data points
    for study, outcomes in study_data.items():
        initial = outcomes['initial']
        intermediates = outcomes['intermediates']
        final = outcomes['final']
        x_values = [initial] + intermediates
        y_values = [final] * len(x_values)

        # Append to respective stage lists
        if len(x_values) > 0:
            initial_x.append(x_values[0])
            initial_y.append(y_values[0])
        if len(x_values) > 1:
            intermediate_1_x.append(x_values[1])
            intermediate_1_y.append(y_values[1])
        if len(x_values) > 2:
            intermediate_2_x.append(x_values[2])
            intermediate_2_y.append(y_values[2])
        if len(x_values) > 3:
            intermediate_3_x.append(x_values[3])
            intermediate_3_y.append(y_values[3])

        # Plot each data point
        for i, (x, y) in enumerate(zip(x_values, y_values)):
            color = stage_colors[min(i, len(stage_colors) - 1)]
            marker = stage_markers[min(i, len(stage_markers) - 1)]
            label = f"{stage_labels[min(i, len(stage_labels) - 1)]} CP" if study == list(study_data.keys())[0] else None
            ax.scatter(x, y, color=color, marker=marker, label=label)

    # Trend lines for each stage
    if initial_x:
        m_initial, b_initial = np.polyfit(initial_x, initial_y, 1)
        ax.plot(np.unique(initial_x), m_initial * np.unique(initial_x) + b_initial, 'r-', linewidth=2, label='Trend - 1st CP')
    if intermediate_1_x:
        m_intermediate_1, b_intermediate_1 = np.polyfit(intermediate_1_x, intermediate_1_y, 1)
        ax.plot(np.unique(intermediate_1_x), m_intermediate_1 * np.unique(intermediate_1_x) + b_intermediate_1, 'b-', linewidth=2, label='Trend - 2nd CP')
    if intermediate_2_x:
        m_intermediate_2, b_intermediate_2 = np.polyfit(intermediate_2_x, intermediate_2_y, 1)
        ax.plot(np.unique(intermediate_2_x), m_intermediate_2 * np.unique(intermediate_2_x) + b_intermediate_2, 'g-', linewidth=2, label='Trend - 3rd CP')
    if intermediate_3_x:
        m_intermediate_3, b_intermediate_3 = np.polyfit(intermediate_3_x, intermediate_3_y, 1)
        ax.plot(np.unique(intermediate_3_x), m_intermediate_3 * np.unique(intermediate_3_x) + b_intermediate_3, 'purple', linewidth=2, label='Trend - 4th CP')

    # Line of agreement
    max_final = max(initial_y + intermediate_1_y + intermediate_2_y + intermediate_3_y)
    min_initial = min(initial_x + intermediate_1_x + intermediate_2_x + intermediate_3_x)
    ax.plot([min_initial, max_final], [min_initial, max_final], 'k--', label='Line of Agreement')

    # Set labels and title
    ax.set_xlabel('Initial/Intermediate Outcome Values (%)')
    ax.set_ylabel('Final Outcome Values (%)')
    ax.set_title(title)

    # Custom legend
    handles, labels = ax.get_legend_handles_labels()
    legend_markers = [
        plt.Line2D([0], [0], marker='X', color='w', markerfacecolor='red', markersize=10, label='1st CP'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='2nd CP'),
        plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='green', markersize=10, label='3rd CP'),
        plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='purple', markersize=10, label='4th CP')
    ]
    ax.legend(handles=legend_markers + handles, loc='upper left')

    # Show plot
    plt.show()

# Example usage
studies_example = {
    'Study 1': {'initial': 67, 'intermediates': [75], 'final': 72.2},
    'Study 2': {'initial': 100, 'intermediates': [67], 'final': 75},
    'Study 3': {'initial': 38, 'intermediates': [], 'final': 60}
}
plot_study_data(studies_example, 'Trend Lines for Clinical Outcomes Across Studies')
