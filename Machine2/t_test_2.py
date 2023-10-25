import scipy.stats as stats

# Sample data for the different number of processes per MPI library
OPENMPI_process_1 = [1.42311, 0.776446, 0.774762, 0.781223]
MPICH_process_1 = [1.42259, 0.775509, 0.774625, 0.773906]

OPENMPI_process_2 = [0.705056, 0.377494, 0.377682, 0.379412]
MPICH_process_2 = [0.705503, 0.379565, 0.379737, 0.377125]

OPENMPI_process_4 = [0.374437, 0.201744, 0.202091, 0.201513]
MPICH_process_4 = [0.388059, 0.202198, 0.203659, 0.204272]


# Perform the paired t-test
t_statistic_1, p_value_1 = stats.ttest_rel(OPENMPI_process_1, MPICH_process_1)
t_statistic_2, p_value_2 = stats.ttest_rel(OPENMPI_process_2, MPICH_process_2)
t_statistic_4, p_value_4 = stats.ttest_rel(OPENMPI_process_4, MPICH_process_4)

# Print the results
print("Paired T-Test Results for 1 process:")
print(f"T-Statistic: {t_statistic_1}")
print(f"P-Value: {p_value_1}")

print("Paired T-Test Results for 2 processes:")
print(f"T-Statistic: {t_statistic_2}")
print(f"P-Value: {p_value_2}")

print("Paired T-Test Results for 4 processes:")
print(f"T-Statistic: {t_statistic_4}")
print(f"P-Value: {p_value_4}")