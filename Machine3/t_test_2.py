import scipy.stats as stats

# Sample data for the different optimization levels per MPI library
OPENMPI_process_1 = [0.278873, 0.170631, 0.16774, 0.168032]
MPICH_process_1 = [0.27573, 0.170747, 0.167907, 0.167611]

OPENMPI_process_2 = [0.146919, 0.0918909, 0.0906551, 0.0904525]
MPICH_process_2 = [0.145103, 0.09171, 0.0903249, 0.0904632]

OPENMPI_process_4 = [0.0756706, 0.0478527, 0.0469158, 0.0469448]
MPICH_process_4 = [0.0788536, 0.0516623, 0.0495721, 0.0514623]

OPENMPI_process_6 = [0.0573377, 0.0388018, 0.0383723, 0.0377424]
MPICH_process_6 = [0.0594524, 0.0407338, 0.040284, 0.0407967]

OPENMPI_process_8 = [0.0664791, 0.0476612, 0.0447907, 0.0444305]
MPICH_process_8 = [0.082655, 0.053518, 0.0533646, 0.0538697]


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