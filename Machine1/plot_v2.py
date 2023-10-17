import matplotlib.pyplot as plt
import numpy as np

# Data for Optimization Level 0
sizes_0 = [1, 2, 4, 6, 8]
mpich_times_0 = [0.128932, 0.133389, 0.132948, 0.133803, 0.132718]
openmpi_times_0 = [0.13015, 0.132138, 0.133163, 0.13333, 0.135153]

# Data for Optimization Level 1
sizes_1 = [1, 2, 4, 6, 8]
mpich_times_1 = [0.0275379, 0.0293441, 0.0316728, 0.0330372, 0.0356594]
openmpi_times_1 = [0.0273104, 0.0284783, 0.0321579, 0.0349996, 0.0359592]

# Data for Optimization Level 2
sizes_2 = [1, 2, 4, 6, 8]
mpich_times_2 = [0.021211, 0.0225312, 0.0258466, 0.029297, 0.0336452]
openmpi_times_2 = [0.0213353, 0.0222505, 0.0241094, 0.0276753, 0.0343092]

# Data for Optimization Level 3
sizes_3 = [1, 2, 4, 6, 8]
mpich_times_3 = [0.00453369, 0.00488548, 0.00563334, 0.00727004, 0.00913719]
openmpi_times_3 = [0.00446078, 0.00474323, 0.00583593, 0.00710516, 0.00867222]

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('MPI Benchmarking Results')

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
ax.legend()

# Adjust subplot spacing
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save the combined plot
plt.savefig('combined_plot.png')


