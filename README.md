# This is a little C++ example to compare the performance of different MPI libraries.

![Machine1 Plot 1](Machine1/combined_plot_v4_1.png)
![Machine1 Plot 2](Machine1/combined_plot_v4_2.png)

![Machine2 Plot 1](Machine2/combined_plot_v4_1.png)
![Machine2 Plot 2](Machine2/combined_plot_v4_2.png)

![Machine3 Plot 1](Machine3/combined_plot_v4_1.png)
![Machine3 Plot 2](Machine3/combined_plot_v4_2.png)

## How to run

To run the program, run:

```bash
make MPI_IMPL=MPICH run_mpich
```
Or: 
```bash
make MPI_IMPL=OPENMPI run_openmpi
```

Or just:
```bash
make run_both
```


## Prerequisites

- C++ compiler
- OpenMPI and MPICH libraries
- mpiexec
- make
