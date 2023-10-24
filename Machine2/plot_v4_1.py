import matplotlib.pyplot as plt
import numpy as np

# Data for Optimization Level 0
sizes_0 = [1, 2, 4]
openmpi_times_0 = [1.42311, 0.705056, 0.374437]
mpich_times_0 = [1.42259, 0.705503, 0.388059]

# Data for Optimization Level 1
sizes_1 = [1, 2, 4]
openmpi_times_1 = [0.776446, 0.377494, 0.201744]
mpich_times_1 = [0.775509, 0.379565, 0.202198]
# Data for Optimization Level 2
sizes_2 = [1, 2, 4]
openmpi_times_2 = [0.774762, 0.377682, 0.202091]
mpich_times_2 = [0.774625, 0.379737, 0.203659]

# Data for Optimization Level 3
sizes_3 = [1, 2, 4]
openmpi_times_3 = [0.781223, 0.379412, 0.201513]
mpich_times_3 = [0.773906, 0.377125, 0.204272]


# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('MPI Benchmarking Results')

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
plt.show()
