import itertools
import time

# Define characters to use in the password
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Define the password to be cracked
PASSWORD = "password123"

# Define the maximum password length to try
MAX_LENGTH = 10

# Track the start time of the password cracking process
start_time = time.time()

# Try all possible combinations of characters up to MAX_LENGTH
for length in range(1, MAX_LENGTH + 1):
    for combination in itertools.product(CHARS, repeat=length):
        # Join the characters in the combination to form a password candidate
        candidate = "".join(combination)
        print(f"Trying password: {candidate}")
        # Check if the candidate matches the password
        if candidate == PASSWORD:
            # Track the end time of the password cracking process
            end_time = time.time()
            print(f"Password found: {candidate}")
            # Calculate the time taken to crack the password
            time_taken = end_time - start_time
            print(f"Time taken: {time_taken:.2f} seconds")
            # Terminate the password cracking process
            raise SystemExit
