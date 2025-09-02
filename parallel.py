import multiprocessing
import subprocess

# Define the function for each job
def run_job(rp_newton, i):
    print(f"Running job {i} with rp_newton = {rp_newton}")
    subprocess.run(['./jobs.sh', str(rp_newton), str(i)])
    print(f"Job {i} completed with rp_newton = {rp_newton}")

if __name__ == "__main__":

    rp_newton_values = [79.14425847, 47.48655508, 39.57212923, 29.67909693, 26.38141949, 23.74327754]
    rp_newton_values = [79.16076756, 59.37057567, 47.49646054, 39.58038378, 33.92604324, 29.68528783]
    rp_newton_values = [79.16]
    # Write rp_newton and i to a file
    with open("runs_info.txt", "w") as file:
        file.write("rp_newton,i\n")
        for i, rp_newton in enumerate(rp_newton_values):
            file.write(f"{rp_newton},{i}\n")

    # Create a multiprocessing Pool with the desired number of processes (cores)
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    # Map the jobs to the pool to run them in parallel
    pool.starmap(run_job, zip(rp_newton_values, range(len(rp_newton_values))))

    # Close the pool to prevent further tasks
    pool.close()

    # Wait for all processes to finish
    pool.join()
