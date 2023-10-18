#!/bin/bash
# for OPT_LEVEL in 3 2 1 0; do
for OPT_LEVEL in 3 2 1 0; do
    # Set the optimization level in CXXFLAGS
    # make CXXFLAGS="-O$OPT_LEVEL -Wall -fopenmp" run_openmpi_with_different_n > "machine1_openmpi_opt$OPT_LEVEL.txt"
    # make CXXFLAGS="-O$OPT_LEVEL -Wall " run_mpich_with_different_n > "machine1_mpich_opt$OPT_LEVEL.txt"
    make CXXFLAGS="-O$OPT_LEVEL -Wall -fopenmp" SRC="mpi_example_pragma_omp.cpp" run_openmpi_with_different_n > "machine1_openmpi_pragma_opt$OPT_LEVEL.txt"
done