import multiprocessing as mp
import subprocess
import numpy as np
from itertools import product
from pathlib import Path

def run_job(beta_val, phi_val, idx):
    print(f"Running job {idx} with beta = {beta_val} and phi = {phi_val}")
    subprocess.run(["bash", "./jobs_sample.sh", str(beta_val), str(phi_val), str(idx)], check=True)
    print(f"Job {idx} completed (beta = {beta_val}, phi = {phi_val})")

if __name__ == "__main__":
    # Generate parameter grids
    beta_values = np.linspace(0.1, 10, 200).tolist()
    phi_values  = np.linspace(0, np.pi, 400).tolist()

    beta_values = [0.1]
    phi_values = [0.0]

    # Build all (beta, phi, idx) triples
    combos = [(b, p, idx) for idx, (b, p) in enumerate(product(beta_values, phi_values))]

    # Write run info
    with open("runs_info.txt", "w") as f:
        f.write("beta,phi,i\n")
        for b, p, idx in combos:
            f.write(f"{b},{p},{idx}\n")

    # Ensure script exists
    assert Path("jobs_sample.sh").exists(), "jobs_sample.sh not found in current directory."

    with mp.Pool(processes=mp.cpu_count()) as pool:
        # chunksize speeds things up when there are many small tasks
        pool.starmap(run_job, combos, chunksize=100)
