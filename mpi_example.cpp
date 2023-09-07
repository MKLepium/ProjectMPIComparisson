#include <iostream>
#include <cstdlib>
#include <ctime>
#include <mpi.h>


double SumArray(int* data, int size) {
    double sum = 0.0;
    for (int i = 0; i < size; ++i) {
        sum += data[i];
    }
    return sum;
}

int main(int argc, char** argv) {


    MPI_Init(&argc, &argv);


    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    const int N = 8;  // Number of times to repeat the whole computation
    const int M = 8;   // Number of times to repeat the inner computation
    const int arraySize = 1000000;  // Size of the array for computation

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
            double result = SumArray(dataArray, arraySize);

            double endTime = MPI_Wtime();
            double elapsedTime = endTime - startTime;
            totalInnerTime += elapsedTime;
        }

        double averageInnerTime = totalInnerTime / M;
        totalOuterTime += averageInnerTime;
        if (rank == 0) {
            std::cout << "Average time for " << M << " iterations: " << averageInnerTime << " seconds." << std::endl;
        }
    }

    // Calculate and print average of averages time
    double averageOuterTime = totalOuterTime / N;
    if (rank == 0) {
        std::cout << "Average of averages time for " << N << " iterations: " << averageOuterTime << " seconds." << std::endl;
    }

    delete[] dataArray;

    MPI_Finalize();
    return 0;
}