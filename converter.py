import tensorflow_datasets as tfds
import tensorflow as tf
from challenges.movi.movi_f import MoviF, MoviFConfig
from tensorflow_datasets.core import download
import time
import argparse

import os
import subprocess

# Set up the environment with CUDA_VISIBLE_DEVICES
env = os.environ.copy()

group_number = 0

# Create a configuration for the dataset
config = MoviFConfig(
    name=f"custom_512x512_group_{group_number}",
    description=f"A custom MOVi-F dataset in 512x512 resolution for group {group_number}",
    height=512,
    width=512,
    num_frames=64,
    validation_ratio=0,  # Adjust validation ratio as desired
    train_val_path=f""  # Path to the outputs of outputs from runner.py
)

# Initialize the dataset builder
dataset_builder = MoviF(config=config, data_dir=f"/remote_training/richard/a/kubric/saved") # dir to save tfrecords

# Build the dataset (this could take time depending on the size of the dataset)
start_time = time.time()
dataset_builder.download_and_prepare()
end_time = time.time()
elapsed = end_time - start_time
print(f'Time for group {group_number}: {elapsed} seconds')




