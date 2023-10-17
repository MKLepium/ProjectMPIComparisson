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
  MPIRUN = mpirun.openmpi
  
else ifeq ($(MPI_IMPL),MPICH)
  MPICXX = mpicxx.mpich
  EXECUTABLE_SUFFIX = mpich.out
  MPIRUN = mpirun.mpich
else
  $(error MPI_IMPL must be either OPENMPI or MPICH)
endif


UNAME_S := $(shell uname -s)

ifeq ($(UNAME_S),Darwin) # for Mac OS X and openmpi
	ifeq ($(MPI_IMPL),OPENMPI)
		MPICXX = /opt/homebrew/opt/open-mpi/bin/mpicxx
		MPIRUN = /opt/homebrew/opt/open-mpi/bin/mpirun
	endif
	ifeq ($(MPI_IMPL),MPICH)
		MPICXX = /opt/homebrew/opt/mpich/bin/mpicxx
		MPIRUN = /opt/homebrew/opt/mpich/bin/mpirun
	endif
endif



# Compiler and flags

CXXFLAGS = -O3 -Wall -fopenmp

# Source file and output executable
SRC = mpi_example.cpp
EXECUTABLE = my_mpi_program$(EXECUTABLE_SUFFIX)

# Targets
all: $(EXECUTABLE)

$(EXECUTABLE): $(SRC)
	echo $(MPICXX)
	$(MPICXX) $(CXXFLAGS) -o $@ $<

run_openmpi: $(EXECUTABLE)
	echo $(MPIRUN)
	echo $(N)
	echo $(EXECUTABLE)
	echo $(MPICXX)
	$(MPIRUN) -np $(N) ./$(EXECUTABLE)

run_mpich: $(EXECUTABLE)
	echo $(MPIRUN)
	echo $(N)
	echo $(EXECUTABLE)
	echo $(MPICXX)
	$(MPIRUN) -np $(N) ./$(EXECUTABLE)

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

run_openmpi_with_different_n:
	make clean
	make N=8 MPI_IMPL=OPENMPI run_openmpi
	echo "openmpi: done with 8"
	make N=6 MPI_IMPL=OPENMPI run_openmpi
	echo "openmpi: done with 6"
	make N=4 MPI_IMPL=OPENMPI run_openmpi
	echo "openmpi: done with 4"
	make N=2 MPI_IMPL=OPENMPI run_openmpi
	echo "openmpi: done with 2"
	make N=1 MPI_IMPL=OPENMPI run_openmpi
	echo "openmpi: done with 1"
	make clean

run_mpich_with_different_n:
	make clean
	make N=8 MPI_IMPL=MPICH run_mpich
	echo "mpich: done with 8"
	make N=6 MPI_IMPL=MPICH run_mpich
	echo "mpich: done with 6"
	make N=4 MPI_IMPL=MPICH run_mpich
	echo "mpich: done with 4"
	make N=2 MPI_IMPL=MPICH run_mpich
	echo "mpich:done with 2"
	make N=1 MPI_IMPL=MPICH run_mpich
	echo "mpich: done with 1"
	make clean

clean:
	rm -f *.out

.PHONY: all clean run_openmpi run_mpich run_both run_both_with_different_n run_openmpi_with_different_n run_mpich_with_different_n
