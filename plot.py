import matplotlib.pyplot as plt

# Data
sizes = [1, 2, 4, 6, 8]
mpich_times = [0.128932, 0.133389, 0.132948, 0.133803, 0.132718]
openmpi_times = [0.13015, 0.132138, 0.133163, 0.13333, 0.135153]

# Create subplots
fig, ax = plt.subplots()

# Bar width
bar_width = 0.35

# X-axis positions for the bars
x_mpich = [x - bar_width/2 for x in sizes]
x_openmpi = [x + bar_width/2 for x in sizes]

# Create bar plots for MPICH and OPENMPI
plt.bar(x_mpich, mpich_times, bar_width, label='MPICH')
plt.bar(x_openmpi, openmpi_times, bar_width, label='OPENMPI')

# Labels and title
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_title('MPI Benchmarking Results Optimization Level 0')
ax.set_xticks(sizes)
ax.set_xticklabels(sizes)
ax.legend()

# Show the plot
plt.tight_layout()
plt.savefig('plot_Optiomisation0.png')

# clear the plot
plt.clf()

# Data
sizes = [1, 2, 4, 6, 8]
mpich_times = [0.0275379, 0.0293441, 0.0316728, 0.0330372, 0.0356594]
openmpi_times = [0.0273104, 0.0284783, 0.0321579, 0.0349996, 0.0359592]

# Create subplots
fig, ax = plt.subplots()

# Bar width
bar_width = 0.35

# X-axis positions for the bars
x_mpich = [x - bar_width/2 for x in sizes]
x_openmpi = [x + bar_width/2 for x in sizes]

# Create bar plots for MPICH and OPENMPI
plt.bar(x_mpich, mpich_times, bar_width, label='MPICH')
plt.bar(x_openmpi, openmpi_times, bar_width, label='OPENMPI')

# Labels and title
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_title('MPI Benchmarking Results Optimization Level 1')
ax.set_xticks(sizes)
ax.set_xticklabels(sizes)
ax.legend()

# Show the plot
plt.tight_layout()
plt.savefig('plot_Optiomisation1.png')

# clear the plot
plt.clf()


# Data
sizes = [1, 2, 4, 6, 8]
mpich_times = [0.021211, 0.0225312, 0.0258466, 0.029297, 0.0336452]
openmpi_times = [0.0213353, 0.0222505, 0.0241094, 0.0276753, 0.0343092]

# Create subplots
fig, ax = plt.subplots()

# Bar width
bar_width = 0.35

# X-axis positions for the bars
x_mpich = [x - bar_width/2 for x in sizes]
x_openmpi = [x + bar_width/2 for x in sizes]

# Create bar plots for MPICH and OPENMPI
plt.bar(x_mpich, mpich_times, bar_width, label='MPICH')
plt.bar(x_openmpi, openmpi_times, bar_width, label='OPENMPI')

# Labels and title
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_title('MPI Benchmarking Results Optimization Level 2')
ax.set_xticks(sizes)
ax.set_xticklabels(sizes)
ax.legend()

# Show the plot
plt.tight_layout()
plt.savefig('plot_Optiomisation2.png')

# clear the plot
plt.clf()

# Data
sizes = [1, 2, 4, 6, 8]
mpich_times = [0.00453369, 0.00488548, 0.00563334, 0.00727004, 0.00913719]
openmpi_times = [0.00446078, 0.00474323, 0.00583593, 0.00710516, 0.00867222]

# Create subplots
fig, ax = plt.subplots()

# Bar width
bar_width = 0.35

# X-axis positions for the bars
x_mpich = [x - bar_width/2 for x in sizes]
x_openmpi = [x + bar_width/2 for x in sizes]

# Create bar plots for MPICH and OPENMPI
plt.bar(x_mpich, mpich_times, bar_width, label='MPICH')
plt.bar(x_openmpi, openmpi_times, bar_width, label='OPENMPI')

# Labels and title
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Average Time (seconds)')
ax.set_title('MPI Benchmarking Results Optimization Level 3')
ax.set_xticks(sizes)
ax.set_xticklabels(sizes)
ax.legend()

# Show the plot
plt.tight_layout()
plt.savefig('plot_Optiomisation3.png')
