#include <iostream>
#include <cstdlib>
#include <ctime>
#include <mpi.h>
#include <math.h>
#define RED_TEXT "\033[1;31m"
#define RESET_COLOR "\033[0m"


double Sum2SqrtArray(int* data, long int size) {
    double sum = 0.0;
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < size; ++i) {
        sum += sqrt(data[i]) + sqrt(data[i]);
    }
    return sum;
}

double SumCosPlusSinArray(int* data, long int size) {
    double sum = 0.0;
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < size; ++i) {
        sum += cos(data[i]) + sin(data[i]);
    }
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
            MPI_Barrier(MPI_COMM_WORLD);  // Sync all processes

            double startTime = MPI_Wtime();

            // Perform the computation
            double result = Sum2SqrtArray(dataArray, arraySize);

            double result2 = SumCosPlusSinArray(dataArray, arraySize);

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
        std::cout << RED_TEXT << std::endl;
        #ifdef OMPI_MPI_H
        std::cout << "OPENMPI: " << "Size: " << size << ": Average time for " << M*N << " iterations: " << averageOuterTime << " seconds." << std::endl;
        #else
        std::cout << "MPICH: " << "Size: " << size << ": Average time for " << M*N << " iterations: " << averageOuterTime << " seconds." << std::endl;
        #endif
        // Reset color to default
        std::cout << RESET_COLOR << std::endl;
    }

    delete[] dataArray;

    MPI_Finalize();
    return 0;
}