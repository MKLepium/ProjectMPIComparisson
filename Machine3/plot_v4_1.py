import matplotlib.pyplot as plt
import numpy as np

# Data for Optimization Level 0
sizes_0 = [1, 2, 4, 6, 8]
openmpi_times_0 = [0.278873, 0.146919, 0.0756706, 0.0573377, 0.0664791]
mpich_times_0 = [0.27573, 0.145103, 0.0788536, 0.0594524, 0.082655]

# Data for Optimization Level 1
sizes_1 = [1, 2, 4, 6, 8]
openmpi_times_1 = [0.170631, 0.0918909, 0.0478527, 0.0388018, 0.0476612]
mpich_times_1 = [0.170747, 0.09171, 0.0516623, 0.0407338, 0.053518]

# Data for Optimization Level 2
sizes_2 = [1, 2, 4, 6, 8]
openmpi_times_2 = [0.16774, 0.0906551, 0.0469158, 0.0383723, 0.0447907]
mpich_times_2 = [0.167907, 0.0903249, 0.0495721, 0.040284, 0.0533646]

# Data for Optimization Level 3
sizes_3 = [1, 2, 4, 6, 8]
openmpi_times_3 = [0.168032, 0.0904525, 0.0469448, 0.0377424, 0.0444305]
mpich_times_3 = [0.167611, 0.0904632, 0.0514623, 0.0407967, 0.0538697]

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('MPI and OpenMP Benchmarking Results')

# Subplot 1: Optimization Level 0
ax = axes[0, 0]
bar_width = 0.2
bar_positions = np.arange(len(sizes_0))
ax.bar(bar_positions - bar_width, mpich_times_0, bar_width, label='MPICH')
ax.bar(bar_positions, openmpi_times_0, bar_width, label='OPENMPI', alpha=0.7)
ax.set_title('Optimization Level 0')
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(sizes_0)
ax.legend()

# Subplot 2: Optimization Level 1
ax = axes[0, 1]
bar_positions = np.arange(len(sizes_1))
ax.bar(bar_positions - bar_width, mpich_times_1, bar_width, label='MPICH')
ax.bar(bar_positions, openmpi_times_1, bar_width, label='OPENMPI', alpha=0.7)
ax.set_title('Optimization Level 1')
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(sizes_1)
ax.legend()

# Subplot 3: Optimization Level 2
ax = axes[1, 0]
bar_positions = np.arange(len(sizes_2))
ax.bar(bar_positions - bar_width, mpich_times_2, bar_width, label='MPICH')
ax.bar(bar_positions, openmpi_times_2, bar_width, label='OPENMPI', alpha=0.7)
ax.set_title('Optimization Level 2')
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(sizes_2)
ax.legend()

# Subplot 4: Optimization Level 3
ax = axes[1, 1]
bar_positions = np.arange(len(sizes_3))
ax.bar(bar_positions - bar_width, mpich_times_3, bar_width, label='MPICH')
ax.bar(bar_positions, openmpi_times_3, bar_width, label='OPENMPI', alpha=0.7)
ax.set_title('Optimization Level 3')
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(sizes_3)
ax.legend()

# Adjust subplot spacing
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save the combined plot
plt.savefig('combined_plot.png')

# Show the plot
