import subprocess
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Set up the environment
env = os.environ.copy()

# Define the function to run the command
def run_docker_command(i):
    command = 'docker run --rm --interactive --user $(id -u):$(id -g) --volume "$(pwd):/kubric" kubricdockerhub/kubruntu /usr/bin/python3 challenges/movi/movi_def_worker.py'
    
    # Run the command
    result = subprocess.run(command, shell=True, env=env)
    
    # Check the result
    if result.returncode == 0:
        print(f"Script executed successfully for shapekey{i}")
    else:
        print(f"Script failed with return code {result.returncode} for shapekey{i}")

# Define the number of threads
# num_threads = os.cpu_count()*0.1  # Adjust based on your system's capabilities
num_threads = 5  # Adjust based on your system's capabilities
print(f'num_threads: {num_threads}')

# Use ThreadPoolExecutor to run tasks in parallel
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Submit all tasks to the executor
    futures = [executor.submit(run_docker_command, i) for i in range(5000)]
    
    # Wait for each task to complete
    for future in tqdm(as_completed(futures)):
        # Just to capture any exceptions raised during execution
        try:
            future.result()
        except Exception as e:
            print(f"An error occurred: {e}")
