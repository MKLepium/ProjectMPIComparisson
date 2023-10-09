# Default MPI implementation (OPENMPI or MPICH)
MPI_IMPL ?= OPENMPI
# Change to MPICH to use MPICH
# change to OPENMPI to use OpenMPI

EXECUTABLE_SUFFIX = 0
# MPI compiler
N = 4
ifeq ($(MPI_IMPL),OPENMPI)
  MPICXX = mpicxx.openmpi
  EXECUTABLE_SUFFIX = openmpi.out
  
else ifeq ($(MPI_IMPL),MPICH)
  MPICXX = mpicxx.mpich
  EXECUTABLE_SUFFIX = mpich.out
else
  $(error MPI_IMPL must be either OPENMPI or MPICH)
endif


# Compiler and flags

CXXFLAGS = -O3 -Wall

# Source file and output executable
SRC = mpi_example.cpp
EXECUTABLE = my_mpi_program$(EXECUTABLE_SUFFIX)

# Targets
all: $(EXECUTABLE)

$(EXECUTABLE): $(SRC)
	$(MPICXX) $(CXXFLAGS) -o $@ $<

run_openmpi: $(EXECUTABLE)
#	echo $(EXECUTABLE) 
#	echo $(N)
	mpirun.openmpi -np $(N) ./$(EXECUTABLE)

run_mpich: $(EXECUTABLE)
#	echo $(EXECUTABLE)
#	echo $(N)
	mpirun.mpich -np $(N) ./$(EXECUTABLE)

run_both:
	make MPI_IMPL=OPENMPI run_openmpi
	make MPI_IMPL=MPICH run_mpich
	make clean

run_both_with_different_n:
	make clean
	make N=8 MPI_IMPL=MPICH run_mpich
	make clean
	make N=8 MPI_IMPL=OPENMPI run_openmpi
	make clean
	make N=6 MPI_IMPL=MPICH run_mpich
	make clean
	make N=6 MPI_IMPL=OPENMPI run_openmpi
	make clean
	make N=4 MPI_IMPL=MPICH run_mpich
	make clean
	make N=4 MPI_IMPL=OPENMPI run_openmpi
	make clean
	make N=2 MPI_IMPL=MPICH run_mpich
	make clean
	make N=2 MPI_IMPL=OPENMPI run_openmpi
	make clean
	make N=1 MPI_IMPL=MPICH run_mpich
	make clean
	make N=1 MPI_IMPL=OPENMPI run_openmpi
	make clean


clean:
	rm -f *.out

.PHONY: all clean
