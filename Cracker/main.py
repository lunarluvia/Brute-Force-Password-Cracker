import itertools
import string
import time

# Define all characters to use in the password
chars = string.printable

# Define the password to be cracked
password = "password123"

# Define the maximum password length to try
max_length = 10

# Track the start time of the password cracking process
start_time = time.time()

# Try all possible combinations of characters up to max_length
for length in range(1, max_length + 1):
    for combination in itertools.product(chars, repeat=length):
        # Join the characters in the combination to form a password candidate
        candidate = "".join(combination)
        print("Trying password:", candidate)
        # Check if the candidate matches the password
        if candidate == password:
            # Track the end time of the password cracking process
            end_time = time.time()
            print("Password found:", candidate)
            # Calculate the time taken to crack the password
            time_taken = end_time - start_time
            print("Time taken:", time_taken, "seconds")
            # Terminate the password cracking process
            raise SystemExit
