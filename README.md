## Brute Force Password Cracker

This Python script implements a brute-force attack to crack a password by trying all possible combinations of characters from a given set of characters. The set of characters used in the password is defined by the `chars` variable, while the password to be cracked is defined by the `password` variable. The maximum password length to try is defined by the `max_length` variable.

The script employs the `itertools` module to generate all possible combinations of characters up to the maximum password length. Each combination is formed by joining the characters using the `join()` method. The resulting combination is then checked against the password to see if there is a match. If a match is found, the script prints the password and the time taken to crack it and terminates.

To provide more advanced password cracking capabilities, the script uses the `time` module to track the start and end time of the password cracking process. The time taken to crack the password is then calculated by subtracting the start time from the end time.

**Note:** This script is intended for educational purposes only and should not be used for malicious purposes. It is important to respect others' privacy and security.
