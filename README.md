# Parallelized Solution of 1D Heat Equation

## Description

This repo contains the collection of codes and results related to the project "Parallelized Solution of 1D Heat Equation". Here are the instructions to replicate the results and graphs presented in the report.

## Environment setup

First, clone this repo. Inside there are 5 folders and this **README.md**:

- **codes_and_jobs**: contains the three C++ implementations, together with the PBS scripts to run the jobs in the cluster. Here you'll need to create 3 empty folders: seq_results, omp_results, and mpi_results. These will contain the temperature distribution results.
- **omp_schedule_test**: the files in this folder can be used if you want to try and test which configuration of the OMP's directive _schedule_ works best.
- **MPI_async**: the files in this folder can be used if you want to try and test the MPI async implementation.
- **plots**: contains the Python codes to generate the graphs.
- **graphs**: contains the actual images used in both the report and the oral presentation.

In order to replicate this project locally, you need to have access to the HPC cluster provided by the University of Trento, then log in either by being connected to the university Wi-Fi or by using the VPN.
Open the terminal and access the university's cluster:

```
ssh name.surname@hpc.unitn.it
```

Then you'll have to insert your Unitn password. Now you should be logged in.

## Load files into HPC cluster

You should now open a local terminal and load the desired folder with:

```
scp -r path_to_directory/codes_and_jobs/ name.surname@hpc.unitn.it:/home/name.surname/
```

Then you'll be asked to put your unitn password. Then the copy to the cluster will begin.

## Jobs submission

Move now to the cluster terminal and enter the folder with _cd_. Now you can start to submit the jobs with the following commands:

```
qsub job_seq.pbs
qsub job_omp.pbs
qsub job_mpi.pbs
```

All the jobs will run in the **short_cpuQ** queue.

You can check anytime the status of your jobs with:

```
qstat -u name.surname
```

## Data collection

Make sure that **every** job in the cluster has ended, use these commands in your local terminal to download all the CSV output files into your local dirctory.

```
scp name.surname@hpc.unitn.it:/home/name.surname/codes_and_jobs/seq_out_results.csv path_to_directory/codes_and_jobs
scp name.surname@hpc.unitn.it:/home/name.surname/codes_and_jobs/omp_out_results.csv path_to_directory/codes_and_jobs
scp name.surname@hpc.unitn.it:/home/name.surname/codes_and_jobs/mpi_out_results.csv path_to_directory/codes_and_jobs
```

These will copy the results of the execution time.

If you also want the temperature distribution results:

```
scp name.surname@hpc.unitn.it:/home/name.surname/codes_and_jobs/seq_results/* path_to_directory/codes_and_jobs/seq_results
scp name.surname@hpc.unitn.it:/home/name.surname/codes_and_jobs/omp_results/* path_to_directory/codes_and_jobs/omp_results
scp name.surname@hpc.unitn.it:/home/name.surname/codes_and_jobs/mpi_results/* path_to_directory/codes_and_jobs/mpi_results
```

Now you should have all the files.

An easier and faster option is to delete your local _codes_and_jobs_ folder and copy the one from the cluster:

```
scp name.surname@hpc.unitn.it:/home/name.surname/codes_and_jobs/ path_to_directory/
```

### Graphs

If you want to recreate the graphs showed and mentioned in the report, be sure to have all the CSV files inside the directory. Then, enter the graphs directory:

```
cd plots
```

Now use these commands to generate the graphs:

- **Sequential times with different sizes**
  ```
  python3 seq_scaling.py
  ```
- **OpenMP times with different threads and sizes**
  ```
  python3 omp_scaling.py
  ```
- **MPI times with different processes and sizes**
  ```
  python3 mpi_scaling.py
  ```
- **Time comparison between sequential, OpenMP, and MPI**
  ```
  python3 time_comparison.py
  ```
- **Speedup and efficiency of OpenMP and MPI**
  ```
  python3 speedup_efficiency.py
  ```
- **Temperature distribution in the rod for all cases**
  ```
  python3 temp_diffusion.py
  ```
- **OpenMP scheduling strategies comparison**
  ```
  python3 omp_scheduling.py
  ```
- **MPI asynchronous VS synchronous**
  ```
  python3 mpi_sync_vs_async.py
  ```

## Conclusion

That was all for what concerned the data processing and collection.
