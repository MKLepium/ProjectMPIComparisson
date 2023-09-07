# Default MPI implementation (OPENMPI or MPICH)
MPI_IMPL ?= OPENMPI
# Change to MPICH to use MPICH
# change to OPENMPI to use OpenMPI

EXECUTABLE_SUFFIX = 0
# MPI compiler
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

CXXFLAGS = -O2 -Wall

# Source file and output executable
SRC = mpi_example.cpp
EXECUTABLE = my_mpi_program$(EXECUTABLE_SUFFIX)

# Targets
all: $(EXECUTABLE)

$(EXECUTABLE): $(SRC)
	$(MPICXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(EXECUTABLE)

.PHONY: all clean
