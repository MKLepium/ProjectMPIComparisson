import matplotlib.pyplot as plt
import numpy as np

# Data for Optimization Level 0
sizes_0 = [1, 2, 4, 6, 8]
openmpi_times_0 = [0.733291, 0.380658, 0.206561, 0.147777, 0.1193]
mpich_times_0 = [0.73552, 0.37891, 0.208396, 0.151687, 0.128439]

# Data for Optimization Level 1
sizes_1 = [1, 2, 4, 6, 8]
openmpi_times_1 = [0.730339, 0.379691, 0.206213, 0.146102, 0.118869]
mpich_times_1 = [0.730973, 0.37825, 0.211073, 0.155436, 0.128437]

# Data for Optimization Level 2
sizes_2 = [1, 2, 4, 6, 8]
openmpi_times_2 = [0.730973, 0.37825, 0.211073, 0.155436, 0.128437]
mpich_times_2 = [0.735425, 0.377216, 0.208084, 0.155155, 0.128611]

# Data for Optimization Level 3
sizes_3 = [1, 2, 4, 6, 8]
openmpi_times_3 = [0.735425, 0.377216, 0.208084, 0.155155, 0.128611]
mpich_times_3 = [0.735425, 0.377216, 0.208084, 0.155155, 0.128611]

# Calculate the common y-axis range
y_min = min(
    min(mpich_times_0), min(openmpi_times_0),
    min(mpich_times_1), min(openmpi_times_1),
    min(mpich_times_2), min(openmpi_times_2),
    min(mpich_times_3), min(openmpi_times_3)
)
y_max = max(
    max(mpich_times_0), max(openmpi_times_0),
    max(mpich_times_1), max(openmpi_times_1),
    max(mpich_times_2), max(openmpi_times_2),
    max(mpich_times_3), max(openmpi_times_3)
)

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharey=True)
fig.suptitle('MPI Benchmarking Results (Optimization Levels)')

# Subplot 1: Optimization Level 0
ax = axes[0, 0]
bar_width = 0.35
bar_positions = np.arange(len(sizes_0))
ax.bar(bar_positions - bar_width/2, mpich_times_0, bar_width, label='MPICH')
ax.bar(bar_positions + bar_width/2, openmpi_times_0, bar_width, label='OPENMPI', alpha=0.7)
ax.set_title('Optimization Level 0')
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(sizes_0)
ax.set_ylim(y_min, y_max)
ax.legend()

# Subplot 2: Optimization Level 1
ax = axes[0, 1]
bar_positions = np.arange(len(sizes_1))
ax.bar(bar_positions - bar_width/2, mpich_times_1, bar_width, label='MPICH')
ax.bar(bar_positions + bar_width/2, openmpi_times_1, bar_width, label='OPENMPI', alpha=0.7)
ax.set_title('Optimization Level 1')
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(sizes_1)
ax.set_ylim(y_min, y_max)
ax.legend()

# Subplot 3: Optimization Level 2
ax = axes[1, 0]
bar_positions = np.arange(len(sizes_2))
ax.bar(bar_positions - bar_width/2, mpich_times_2, bar_width, label='MPICH')
ax.bar(bar_positions + bar_width/2, openmpi_times_2, bar_width, label='OPENMPI', alpha=0.7)
ax.set_title('Optimization Level 2')
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(sizes_2)
ax.set_ylim(y_min, y_max)
ax.legend()

# Subplot 4: Optimization Level 3
ax = axes[1, 1]
bar_positions = np.arange(len(sizes_3))
ax.bar(bar_positions - bar_width/2, mpich_times_3, bar_width, label='MPICH')
ax.bar(bar_positions + bar_width/2, openmpi_times_3, bar_width, label='OPENMPI', alpha=0.7)
ax.set_title('Optimization Level 3')
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(sizes_3)
ax.set_ylim(y_min, y_max)
ax.legend()

# Adjust subplot spacing
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save the combined plot
plt.savefig('combined_plot.png')

