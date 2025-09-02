#!/bin/bash
# Obtain rp_newton and loop_number as input values
rp_newton="$1"
loop_number="$2"
echo "loop number $loop_number"
echo "Running geodesic simulation for rp_newton=$rp_newton, loop=$loop_number"

# Create a separate directory for each job
job_dir="$(pwd)/tde_${loop_number}"
mkdir -p "$job_dir"

# Copy these 4 files. For each job they will be needed.
cp orbit.params "$job_dir/orbit.params"
cp grtest.in "$job_dir/grtest.in"
cp grtest.params "$job_dir/grtest.params"
cp output_00000.dat "$job_dir/output_00000.dat"

# Generate the orbit.params file using Python script
# Path to the generate_orbit_params.py script
generate_script="../utils/write_orbit_params.py"

# Change to the job directory
cd "$job_dir"
python3 "${generate_script}" ${rp_newton} 0.0 "$job_dir"
echo ${job_dir}
# Set the positions, velocities and ev output filenames
export positions_file="${job_dir}/positions_${loop_number}.dat"
export velocities_file="${job_dir}/velocities_${loop_number}.dat"
export ev_file="${job_dir}/ev_${loop_number}.dat"

# Run grtest with the generated orbit.params file
../grtest < orbit.params
../grtest output_00000.dat

echo "Geodesic simulation complete for rp_newton=$rp_newton, loop=$loop_number"
