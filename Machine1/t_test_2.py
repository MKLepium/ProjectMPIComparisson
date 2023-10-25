import scipy.stats as stats

# Sample data for the different number of processes per MPI library
OPENMPI_process_1 = [2.58251, 0.735614, 0.730339, 0.733291]
MPICH_process_1 = [2.99873, 0.73552, 0.730973, 0.735425]

OPENMPI_process_2 = [1.40789, 0.382622, 0.379691, 0.380658]
MPICH_process_2 = [1.48617, 0.37891, 0.37825, 0.377216]

OPENMPI_process_4 = [0.73091, 0.206561, 0.206213, 0.205773]
MPICH_process_4 = [0.737059, 0.208396, 0.211073, 0.208084]

OPENMPI_process_6 = [0.479457, 0.147777, 0.146102, 0.147576]
MPICH_process_6 = [0.489144, 0.151687, 0.155436, 0.155155]

OPENMPI_process_8 = [0.341295, 0.1193, 0.118869, 0.121611]
MPICH_process_8 = [0.361513, 0.128439, 0.128437, 0.128611]


# Perform the paired t-test
t_statistic_1, p_value_1 = stats.ttest_rel(OPENMPI_process_1, MPICH_process_1)
t_statistic_2, p_value_2 = stats.ttest_rel(OPENMPI_process_2, MPICH_process_2)
t_statistic_4, p_value_4 = stats.ttest_rel(OPENMPI_process_4, MPICH_process_4)
t_statistic_6, p_value_6 = stats.ttest_rel(OPENMPI_process_6, MPICH_process_6)
t_statistic_8, p_value_8 = stats.ttest_rel(OPENMPI_process_8, MPICH_process_8)

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

print("Paired T-Test Results for 6 processes:")
print(f"T-Statistic: {t_statistic_6}")
print(f"P-Value: {p_value_6}")

print("Paired T-Test Results for 8 processes:")
print(f"T-Statistic: {t_statistic_8}")
print(f"P-Value: {p_value_8}")