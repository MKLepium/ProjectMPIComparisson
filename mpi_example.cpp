#include <iostream>
#include <cstdlib>
#include <ctime>
#include <mpi.h>
#include <math.h>

double Sum2SqrtArray(int* data, long int size) {
    double local_sum = 0.0;
    double sum = 0.0;

    // Determine the rank and size of the MPI communicator
    int rank, comm_size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &comm_size);

    // Calculate the chunk size for each process
    int chunk_size = size / comm_size;
    //int start = rank * chunk_size;
    // The last process may need to do more work if the total size is not divisible by the number of processes
    //int end = (rank == comm_size - 1) ? size : start + chunk_size;

    // Allocate memory for the local data
    int* local_data = (int*)malloc(chunk_size * sizeof(int));

    // Scatter the data to all processes
    MPI_Scatter(&data[0], chunk_size, MPI_INT, local_data, chunk_size, MPI_INT, 0, MPI_COMM_WORLD);

    // Calculate the local sum for the assigned chunk
    for (int i = 0; i < chunk_size; ++i) {
        // Perform the computation on local data
        local_sum += sqrt(sqrt(local_data[i]) + sqrt(local_data[i]));
    }

    // Reduce local sums to obtain the final sum
    MPI_Reduce(&local_sum, &sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    // Free the allocated memory
    free(local_data);

    return sum;
}

// There is lots of boilerplate code in here.
double SumCosPlusSinArray(int* data, long int size) {
    double local_sum = 0.0;
    double sum = 0.0;

    // Determine the rank and size of the MPI communicator
    int rank, comm_size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &comm_size);

    // Calculate the chunk size for each process
    int chunk_size = size / comm_size;
    //int start = rank * chunk_size;
    // The last process may need to do more work if the total size is not divisible by the number of processes
    //int end = (rank == comm_size - 1) ? size : start + chunk_size;

    // Allocate memory for the local data
    int* local_data = (int*)malloc(chunk_size * sizeof(int));

    // Scatter the data to all processes
    MPI_Scatter(&data[0], chunk_size, MPI_INT, local_data, chunk_size, MPI_INT, 0, MPI_COMM_WORLD);

    // Calculate the local sum for the assigned chunk
    for (int i = 0; i < chunk_size; ++i) {
        // Perform the computation on local data
        local_sum += cos(local_data[i]) + sin(local_data[i]);
    }

    // Reduce local sums to obtain the final sum
    MPI_Reduce(&local_sum, &sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    // Free the allocated memory
    free(local_data);

    return sum;
}


int main(int argc, char** argv) {


    MPI_Init(&argc, &argv);


    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    //std::cout << "Process with rank " << rank << " started." << std::endl;

    const int N = 10;  // Number of times to repeat the whole computation
    const int M = 10;   // Number of times to repeat the inner computation
    const long int arraySize = 10000000;  // Size of the array for computation
    //const long int arraySize = 100000;  // Size of the array for computation

    int* dataArray = new int[arraySize];

    // Initialize the data array with random values
    srand(time(NULL) + rank);
    for (int i = 0; i < arraySize; ++i) {
        dataArray[i] = rand();
    }

    double totalOuterTime = 0.0;

    for (int n = 0; n < N; ++n) {
        double totalInnerTime = 0.0;

        for (int m = 0; m < M; ++m) {
            // distributed
            // check the processes
            // divide the data by the ammount of processes
            // send each process a part of the data
            // run the computation

            MPI_Barrier(MPI_COMM_WORLD);  // Sync all processes


            double startTime = MPI_Wtime();

            // Perform the computation
            double volatile result = Sum2SqrtArray(dataArray, arraySize);
            __asm__ volatile("" : : "g"(result) : "memory");

            double result2 = SumCosPlusSinArray(dataArray, arraySize);
            __asm__ volatile("" : : "g"(result2) : "memory");

            double endTime = MPI_Wtime();
            double elapsedTime = endTime - startTime;
            totalInnerTime += elapsedTime;
        }

        double averageInnerTime = totalInnerTime / M;
        totalOuterTime += averageInnerTime;
        /*if (rank == 0) {
            // print average for openmp
            #ifdef OMPI_MPI_H
            std::cout << "OPENMPI: Average time for " << M << " iterations: " << averageInnerTime << " seconds." << std::endl;
            #else
            std::cout << "MPICH: Average time for " << M << " iterations: " << averageInnerTime << " seconds." << std::endl;
            #endif
        }*/
    }

    // Calculate and print average of averages time
    double averageOuterTime = totalOuterTime / N;
    if (rank == 0) {
        #ifdef OMPI_MPI_H
        std::cout << "OPENMPI: " << "Size: " << size << ": Average time for " << M*N << " iterations: " << averageOuterTime << " seconds." << std::endl;
        #else
        std::cout << "MPICH: " << "Size: " << size << ": Average time for " << M*N << " iterations: " << averageOuterTime << " seconds." << std::endl;
        #endif
    }

    delete[] dataArray;

    MPI_Finalize();
    return 0;
}